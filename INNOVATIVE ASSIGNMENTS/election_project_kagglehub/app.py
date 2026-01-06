
import os, json
from flask import Flask, render_template, request, redirect, url_for
import joblib, numpy as np, pandas as pd
from pathlib import Path
from train import load_dataset_df, prepare_features, train_and_save_model

MODEL_PATH = Path('model/model_reg.pkl')
META_PATH = Path('model/metadata.json')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','devkey')

def ensure_model():
    if MODEL_PATH.exists() and META_PATH.exists():
        model = joblib.load(MODEL_PATH)
        meta = json.loads(META_PATH.read_text())
        print('Loaded model and metadata.')
        return model, meta
    # train if missing
    print('Model missing - training now (this may take a minute)...')
    df = load_dataset_df()
    model, metrics = train_and_save_model(df, out=str(MODEL_PATH))
    meta = json.loads(Path('model').joinpath('metadata.json').read_text())
    return model, meta

MODEL, META = ensure_model()

@app.route('/')
def index():
    # show some dataset info if available
    data_preview = None
    try:
        df = load_dataset_df()
        data_preview = df.head(8).to_dict(orient='records')
    except Exception as e:
        data_preview = []
    return render_template('index.html', preview=data_preview, metrics=META)

@app.route('/predict', methods=['POST'])
def predict():
    entries = []
    for i in range(1,7):
        p = request.form.get(f'party_name_{i}', '').strip()
        e = request.form.get(f'exited_{i}', '').strip()
        if p and e != '':
            try:
                e_val = float(e)
            except:
                return "Invalid exit poll number for party " + p, 400
            entries.append({'party': p, 'exit': e_val})
    if not entries:
        return redirect(url_for('index'))

    party_map = META.get('party_map', {})
    year = int(request.form.get('year', META.get('year_mean', 2019)))
    rows = []
    for ent in entries:
        party = ent['party']
        exit_v = ent['exit']
        party_code = party_map.get(party, 0)
        rows.append({'Year': year, 'Party_code': party_code, 'ExitPoll': exit_v})

    X = pd.DataFrame(rows)[['Year','Party_code','ExitPoll']].values
    preds = MODEL.predict(X)
    for i,ent in enumerate(entries):
        ent['predicted_actual'] = float(preds[i])

    winner = max(entries, key=lambda x: x['predicted_actual'])
    return render_template('result.html', entries=entries, winner=winner, metrics=META)

if __name__ == '__main__':
    app.run(debug=True)
