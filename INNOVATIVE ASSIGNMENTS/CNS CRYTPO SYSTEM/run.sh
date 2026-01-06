
#!/bin/bash

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
python -m flask run --host=0.0.0.0 --port=5000
