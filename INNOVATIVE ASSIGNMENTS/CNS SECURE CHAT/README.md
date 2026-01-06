# Secure Web Chat (Flask + Flask-SocketIO)

This project is a minimal, secure (HTTPS/WSS) web chat demo written with:
- Backend: Flask + Flask-SocketIO
- Frontend: Plain HTML, CSS and vanilla JS (Socket.IO client)

**What I included**
- `app.py` — Flask app with Socket.IO chat handlers
- `templates/index.html` — Landing / username page
- `templates/chat.html` — Chat UI
- `static/css/styles.css` — Professional-ish CSS (no frameworks)
- `static/js/chat.js` — Client JS to connect over WSS
- `requirements.txt` — Python deps
- `run.sh` — Helpful run script (generates cert using openssl if available)
- `generate_cert.sh` — openssl command to generate self-signed cert
- `LICENSE.txt`

## Quick start (development)

1. Create and activate a virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Generate a self-signed certificate (development only). You can use the provided script:
   ```bash
   chmod +x generate_cert.sh
   ./generate_cert.sh
   ```
   or run:
   ```bash
   openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
   ```
3. Run the app (this starts HTTPS + WSS):
   ```bash
   python app.py
   ```
4. Open `https://localhost:8443` in your browser and accept the self-signed certificate warning.

## Notes
- For production use, obtain certificates from Let's Encrypt or a trusted CA.
- This demo uses Flask-SocketIO and will default to using its best async mode if available.
- The server requires `cert.pem` and `key.pem` in the project root to run in HTTPS/WSS mode. See `generate_cert.sh`.
