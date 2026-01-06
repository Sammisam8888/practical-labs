
Election Exit-Poll Predictor (Kaggle dataset)
============================================

This project trains a RandomForest regressor to predict Actual votes from ExitPoll numbers
and picks a predicted winner among user-supplied parties. The training script will attempt to
download the dataset via kagglehub if no local CSV is provided.

Quick start:
1. Create venv and install deps:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Train model (optional - app will auto-train if model missing):
   python train.py --out model/model_reg.pkl --evaluate

3. Run app:
   export FLASK_APP=app.py
   flask run --port=5003

Notes:
- The training script uses 'kagglehub' to fetch 'asmitkumar12/election-data-vs-exit-poll-1999-2019' dataset.
- If you prefer to use a local CSV, place it at data/election_all.csv or pass --data_csv to train.py.
