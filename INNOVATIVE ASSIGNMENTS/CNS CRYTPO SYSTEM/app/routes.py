from flask import current_app as app, render_template, request, jsonify, redirect, url_for, flash
from . import db, login_manager
from .models import SimulationResult, User, Transaction
from .simulate import (run_sample_simulation, summarize_result,
                       generate_tx, simulate_pow_block, monte_carlo_double_spend,
                       attack_graph_simple, estimate_max_throughput, simulate_pos_epoch)
from flask_login import login_user, logout_user, login_required, current_user
import json, datetime, hashlib

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

# ------------- Authentication ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    form = request.form
    name = form.get('name', '').strip()
    email = form.get('email', '').strip().lower()
    password = form.get('password', '')
    if not (name and email and password):
        flash('All fields are required.', 'error')
        return redirect(url_for('register'))
    if User.query.filter_by(email=email).first():
        flash('Email already registered.', 'error')
        return redirect(url_for('register'))
    u = User(name=name, email=email)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    flash('Account created. Please login.', 'success')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    form = request.form
    email = form.get('email','').strip().lower()
    password = form.get('password','')
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash('Invalid credentials', 'error')
        return redirect(url_for('login'))
    login_user(user)
    flash('Logged in successfully', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('index'))

# ------------- Dashboard & Sim --------------
@app.route('/dashboard')
@login_required
def dashboard():
    sims = SimulationResult.query.order_by(SimulationResult.created_at.desc()).limit(10).all()
    txs = Transaction.query.order_by(Transaction.timestamp.desc()).limit(10).all()
    return render_template('dashboard.html', sims=sims, txs=txs)

@app.route('/simulate', methods=['POST'])
@login_required
def simulate():
    payload = request.json or {}
    name = payload.get('name', 'Quick Simulation')
    params = payload.get('params', {})
    # run sample simulation (fast & deterministic)
    result = run_sample_simulation(params)
    summary = summarize_result(result)
    sim = SimulationResult(name=name, parameters=json.dumps(params), result_json=json.dumps(result))
    db.session.add(sim)
    db.session.commit()
    return jsonify({'status':'ok','id': sim.id, 'summary': summary, 'result': result})

# extended simulate endpoint for PoW/PoS & Monte Carlo
@app.route('/simulate/advanced', methods=['POST'])
@login_required
def simulate_advanced():
    payload = request.json or {}
    name = payload.get('name', 'Advanced Simulation')
    params = payload.get('params', {})

    # Example inputs:
    # params: { mode:'pow'/'pos', miners_hash:[...], stakes:[...], runs:1000, tx_rate:5.0 }
    mode = params.get('mode','pow')
    tx_rate = float(params.get('tx_rate', 5.0))
    # if pow: miners_hash list expected (attacker at index 0)
    # if pos: stakes list expected
    res = {}
    if mode == 'pow':
        miners_hash = params.get('miners_hash') or [1.0] + [1.0]*9
        # run a short sample block mining session
        blk = simulate_pow_block(miners_hash, difficulty=float(params.get('difficulty',1.0)))
        res['pow_sample'] = blk
    else:
        stakes = params.get('stakes') or [10.0] + [5.0]*9
        validator = simulate_pos_epoch(stakes)
        res['pos_sample'] = validator

    # Monte Carlo:
    runs = int(params.get('runs', 500))
    mc_kwargs = dict(num_nodes=int(params.get('num_nodes',50)),
                     honest_ratio=float(params.get('honest_ratio',0.8)),
                     tx_rate=tx_rate)
    if mode == 'pow':
        mc_kwargs['miners_hash'] = params.get('miners_hash') or [1.0] + [1.0]*9
        mc_kwargs['pow'] = True
    else:
        mc_kwargs['stakes'] = params.get('stakes') or [10.0] + [5.0]*9
        mc_kwargs['pow'] = False

    mc = monte_carlo_double_spend(runs=runs, **mc_kwargs)
    res['monte_carlo'] = mc
    # attack graph & throughput estimate
    res['attack_graph'] = attack_graph_simple(num_nodes=int(params.get('num_nodes',10)), attacker_index=0, honest_ratio=float(params.get('honest_ratio',0.8)))
    res['throughput_estimate'] = estimate_max_throughput(int(params.get('num_nodes',50)),
                                                         tx_size_bytes=int(params.get('tx_size',250)),
                                                         block_size_bytes=int(params.get('block_size',1_000_000)),
                                                         block_interval=float(params.get('block_interval',10.0)))
    # save
    sim = SimulationResult(name=name, parameters=json.dumps(params), result_json=json.dumps(res))
    db.session.add(sim)
    db.session.commit()
    return jsonify({'status':'ok','id': sim.id, 'result': res})

# --------------- Transactions ----------------
@app.route('/tx/create', methods=['POST'])
@login_required
def create_tx():
    data = request.json or request.form or {}
    sender = data.get('sender') or current_user.email
    receiver = data.get('receiver') or data.get('to') or 'recipient@example.com'
    amount = float(data.get('amount') or 0.0)
    tx = generate_tx(sender, receiver, amount)
    # store in DB
    t = Transaction(tx_hash=tx['tx_hash'], sender=sender, receiver=receiver, amount=amount, meta=json.dumps(tx))
    db.session.add(t)
    db.session.commit()
    return jsonify({'status':'ok', 'tx':tx})

@app.route('/tx/list')
@login_required
def list_txs():
    txs = Transaction.query.order_by(Transaction.timestamp.desc()).limit(200).all()
    result = []
    for t in txs:
        result.append({
            'id': t.id, 'tx_hash': t.tx_hash, 'sender': t.sender, 'receiver': t.receiver,
            'amount': t.amount, 'ts': t.timestamp.isoformat(), 'confirmed': t.confirmed
        })
    return jsonify({'txs': result})

@app.route('/tx/confirm_batch', methods=['POST'])
@login_required
def confirm_batch():
    """
    Toy endpoint: mark a batch of txs as confirmed (simulate block inclusion).
    Accepts JSON: { tx_ids: [1,2,3] }
    """
    data = request.json or {}
    tx_ids = data.get('tx_ids', [])
    updated = []
    for tid in tx_ids:
        tx = Transaction.query.get(tid)
        if tx:
            tx.confirmed = True
            updated.append(tx.id)
    db.session.commit()
    return jsonify({'updated': updated})

@app.route('/tx/<int:tx_id>')
@login_required
def view_tx(tx_id):
    tx = Transaction.query.get_or_404(tx_id)
    return render_template('transaction.html', tx=tx)

@app.route('/tx/confirm/<int:tx_id>', methods=['POST'])
@login_required
def confirm_tx(tx_id):
    tx = Transaction.query.get_or_404(tx_id)
    tx.confirmed = True
    db.session.commit()
    flash(f'Transaction {tx.tx_hash[:10]}... confirmed.', 'success')
    return redirect(url_for('view_tx', tx_id=tx.id))

# view a saved simulation

@app.route('/simulation/<int:sim_id>')
@login_required
def view_simulation(sim_id):
    sim = SimulationResult.query.get_or_404(sim_id)
    result_data = json.loads(sim.result_json or "{}")
    return render_template('report.html', sim=sim, result_data=result_data)