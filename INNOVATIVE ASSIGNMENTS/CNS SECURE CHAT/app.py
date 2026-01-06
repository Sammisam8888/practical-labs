import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room

# NOTE: this file assumes your registration/login flow already exists as earlier.
# It's the same app but with room support and RSA routing for encrypted messages.

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
socketio = SocketIO(app, cors_allowed_origins="*")

DB_NAME = "users.db"

# --- DB helpers (unchanged from before) ---
def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''CREATE TABLE users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
        conn.commit()
        conn.close()

init_db()

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_NAME)
    return g.db

@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# --- Routes (login/register pages) ---
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # simple hashing to keep parity with earlier code
        from werkzeug.security import generate_password_hash
        hashed = generate_password_hash(password)
        try:
            db = get_db()
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            db.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {e}"
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    from werkzeug.security import check_password_hash
    user = get_db().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user and check_password_hash(user[2], password):
        session['username'] = username
        return redirect(url_for('chat'))
    return "Invalid credentials!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('chat.html', username=session['username'])

# Optional endpoint to check if a username exists (client can use to validate)
@app.route('/exists/<username>')
def exists(username):
    u = get_db().execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
    return jsonify({"exists": bool(u)})

# --- Socket.IO events for rooms + RSA message routing ---
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Join a room named after the username (so we can privately send messages)
@socketio.on('join_room')
def handle_join_room(data):
    username = data.get('username')
    if not username:
        return
    join_room(username)
    emit('status', {'msg': f'{username} joined their private room.'}, room=username)
    print(f"User {username} joined room {username}")

@socketio.on('leave_room')
def handle_leave_room(data):
    username = data.get('username')
    if username:
        leave_room(username)
        print(f"User {username} left room {username}")

# Generic text messages (legacy / broadcast)
@socketio.on('message')
def handle_message(data):
    username = data.get('username', 'Anonymous')
    msg = data.get('msg', '')
    emit('message', {'username': username, 'msg': msg}, broadcast=True)

# RSA-encrypted message routing
# Data expected from client:
# {
#   sender: "alice",
#   recipient: "bob",
#   ciphertext: "<base64...>",
#   signature: "<base64...>" (optional),
#   sender_pub: "<sender's public key pem>" (optional, helpful for verification)
# }
@socketio.on('rsa_message')
def handle_rsa_message(data):
    sender = data.get('sender')
    recipient = data.get('recipient')
    ciphertext = data.get('ciphertext')
    signature = data.get('signature')
    sender_pub = data.get('sender_pub')  # optionally broadcast so recipient can verify

    if not sender or not recipient or not ciphertext:
        return

    # Emit the encrypted payload only to the recipient's room and to the sender's room (so both see their copy)
    payload = {
        'sender': sender,
        'recipient': recipient,
        'ciphertext': ciphertext,
        'signature': signature,
        'sender_pub': sender_pub
    }
    # send to recipient
    emit('rsa_message', payload, room=recipient)
    # also send to sender (so sender UI can show its own encrypted message)
    emit('rsa_message', payload, room=sender)
    print(f"Routed RSA message from {sender} to {recipient}")

if __name__ == '__main__':
    cert = os.path.join(os.getcwd(), 'cert.pem')
    key = os.path.join(os.getcwd(), 'key.pem')
    port = int(os.environ.get('PORT', 8443))
    if os.path.exists(cert) and os.path.exists(key):
        print(f"Running with HTTPS/TLS on port {port}")
        socketio.run(app, host='0.0.0.0', port=port, ssl_context=(cert, key))
    else:
        print("Running without SSL (dev mode only)")
        socketio.run(app, host='0.0.0.0', port=port)
