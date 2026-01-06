
from flask import current_app as app, render_template, request, jsonify, redirect, url_for
import os, joblib, json
from pathlib import Path
import numpy as np

MODEL_PATH = Path(__file__).resolve().parents[1] / 'model' / 'model.pkl'

def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or request.form.to_dict()
    try:
        age = float(data.get('age', 40))
        education = float(data.get('education', 12))
        urban = float(data.get('urban', 1))
        income = float(data.get('income', 30000))
        prior_vote = float(data.get('prior_vote', 0))
    except Exception as e:
        return jsonify({'error':'invalid input', 'details': str(e)}), 400

    model = load_model()
    if model is None:
        # attempt quick train
        train_script = Path(__file__).resolve().parents[1] / '..' / 'train.py'
        os.system(f'python {train_script} --quick --out {MODEL_PATH}')

        model = load_model()
        if model is None:
            return jsonify({'error':'model not available'}), 500

    X = np.array([[age, education, urban, income, prior_vote]])
    pred = model.predict_proba(X)[0,1]
    return jsonify({'prediction': float(pred), 'features': {'age':age,'education':education,'urban':urban,'income':income,'prior_vote':prior_vote}})

@app.route('/about')
def about():
    return render_template('about.html')
