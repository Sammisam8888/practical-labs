#!/usr/bin/env bash
# Generate a self-signed certificate for localhost (development only)
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
echo "Generated cert.pem and key.pem"
