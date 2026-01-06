#!/usr/bin/env bash
# Helper to create venv, install and run (dev)
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
if [ ! -f cert.pem ] || [ ! -f key.pem ]; then
  echo "cert.pem/key.pem missing — generating self-signed cert (development)"
  ./generate_cert.sh
fi
python app.py
