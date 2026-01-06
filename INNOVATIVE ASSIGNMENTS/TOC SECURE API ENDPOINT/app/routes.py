from flask import current_app as app, render_template, request, redirect, url_for, jsonify, send_file
from .models import Endpoint
from . import db
from .dfa_engine import simulate_dfa_on_spec
import json, io

@app.route('/')
def index():
    eps = Endpoint.query.order_by(Endpoint.created_at.desc()).all()
    return render_template('endpoints.html', endpoints=eps)

@app.route('/endpoint/new', methods=['GET','POST'])
def new_endpoint():
    if request.method == 'GET':
        return render_template('endpoint_edit.html')
    form = request.form
    name = form.get('name','').strip()
    path = form.get('path','').strip()
    method = form.get('method','POST').strip().upper()
    q = form.get('query_schema','{}')
    b = form.get('body_schema','{}')
    r = form.get('response_schema','{}')
    try:
        qj = json.loads(q)
        bj = json.loads(b)
        rj = json.loads(r)
    except Exception as e:
        return f'Invalid JSON: {e}', 400
    ep = Endpoint(name=name, path=path, method=method, query_schema=json.dumps(qj), body_schema=json.dumps(bj), response_schema=json.dumps(rj))
    db.session.add(ep)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/endpoint/<int:ep_id>')
def view_endpoint(ep_id):
    ep = Endpoint.query.get_or_404(ep_id)
    spec = {
        'name': ep.name,
        'path': ep.path,
        'method': ep.method,
        'query_schema': ep.query_schema_dict(),
        'body_schema': ep.body_schema_dict(),
        'response_schema': ep.response_schema_dict()
    }
    dfa = simulate_dfa_on_spec(spec)
    return render_template('endpoint_view_full.html', ep=ep, spec=spec, dfa=dfa)

@app.route('/api/endpoint/<int:ep_id>/dfa_json')
def dfa_json(ep_id):
    ep = Endpoint.query.get_or_404(ep_id)
    spec = {
        'name': ep.name,
        'path': ep.path,
        'method': ep.method,
        'query_schema': ep.query_schema_dict(),
        'body_schema': ep.body_schema_dict(),
        'response_schema': ep.response_schema_dict()
    }
    dfa = simulate_dfa_on_spec(spec)
    return jsonify(dfa)

@app.route('/endpoint/<int:ep_id>/export')
def export_spec(ep_id):
    ep = Endpoint.query.get_or_404(ep_id)
    spec = {
        'name': ep.name,
        'path': ep.path,
        'method': ep.method,
        'query_schema': ep.query_schema_dict(),
        'body_schema': ep.body_schema_dict(),
        'response_schema': ep.response_schema_dict()
    }
    dfa = simulate_dfa_on_spec(spec)
    out = json.dumps(dfa['final_spec'], indent=2)
    return send_file(io.BytesIO(out.encode('utf-8')), download_name=f"secured_spec_{ep.id}.json", as_attachment=True)
