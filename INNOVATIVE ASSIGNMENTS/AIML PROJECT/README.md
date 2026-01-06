
# Election Exit-Poll Prediction - AIML Project

This is a self-contained minimal AIML project scaffold for "Election exit-poll predictions".
It includes:
- a Flask web app that serves a small UI and a prediction API
- a training script (train.py) to train a simple ML model (RandomForest) on synthetic or provided CSV data
- a sample dataset generator (data/gen_sample_data.py)
- a utilities module to load/save the trained model (`model/model.pkl`)
- templates (templates/) and static assets (static/)
- instructions to run locally

## Quick start (Linux/macOS)
1. Create virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Train the model (creates `model/model.pkl`):
   ```bash
   python train.py --data data/sample_exitpolls.csv --out model/model.pkl
   ```
   If you skip training, the Flask app will generate a small sample dataset and train on first request.
3. Run the app:
   ```bash
   export FLASK_APP=app
   flask run --host=0.0.0.0 --port=5001
   ```
4. Open http://localhost:5001 in your browser and use the UI to make predictions.
