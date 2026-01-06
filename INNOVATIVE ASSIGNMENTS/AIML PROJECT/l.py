# Creating the Election Exit-Poll Predictor project (using kagglehub in train script) and zipping it.
# This will write files to /mnt/data/election_project_kagglehub and create /mnt/data/election_project_kagglehub.zip
import os, zipfile, textwrap, json, shutil, pathlib

root = "./election_project_kagglehub"
if os.path.exists(root):
    shutil.rmtree(root)
os.makedirs(root, exist_ok=True)

files = {}

files["README.md"] = textwrap.dedent("""
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
""")

files["requirements.txt"] = "\n".join([
    "flask>=2.0",
    "pandas>=1.0",
    "scikit-learn>=1.0",
    "numpy>=1.18",
    "joblib>=1.0",
    "kagglehub>=0.1.0"
])

# app.py
files["app.py"] = textwrap.dedent("""
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
""")

# train.py
files["train.py"] = textwrap.dedent("""
import argparse, json, os
import pandas as pd, numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path

def load_dataset_df(data_csv=None):
    if data_csv and Path(data_csv).exists():
        print('Loading dataset from', data_csv)
        return pd.read_csv(data_csv)
    local = Path('data/election_all.csv')
    if local.exists():
        print('Loading dataset from', local)
        return pd.read_csv(local)
    # try kagglehub
    try:
        import kagglehub
        from kagglehub import KaggleDatasetAdapter
        print('Attempting to download dataset via kagglehub...')
        df = kagglehub.load_dataset(KaggleDatasetAdapter.PANDAS, 'asmitkumar12/election-data-vs-exit-poll-1999-2019', 'election_all.csv')
        Path('data').mkdir(parents=True, exist_ok=True)
        df.to_csv('data/election_all.csv', index=False)
        return df
    except Exception as e:
        raise RuntimeError('Could not load dataset: ' + str(e))

def prepare_features(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    df = df.dropna(subset=['Year','Party','ExitPoll','Actual'])
    df['Party'] = df['Party'].astype(str)
    parties = sorted(df['Party'].unique().tolist())
    party_map = {p:i+1 for i,p in enumerate(parties)}
    df['Party_code'] = df['Party'].map(party_map).fillna(0).astype(int)
    X = df[['Year','Party_code','ExitPoll']].values
    y = df['Actual'].values
    meta = {'party_map': party_map, 'parties': parties, 'year_mean': int(df['Year'].median())}
    return X, y, meta, df

def train_and_save_model(df, out='model/model_reg.pkl'):
    X, y, meta, dfclean = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    # winner prediction accuracy over years
    years = sorted(dfclean['Year'].unique())
    correct = 0
    total = 0
    for yr in years:
        sub = dfclean[dfclean['Year']==yr]
        if len(sub) < 2: continue
        X_sub = sub[['Year','Party_code','ExitPoll']].values
        preds_sub = model.predict(X_sub)
        pred_idx = int(np.argmax(preds_sub))
        actual_idx = int(np.argmax(sub['Actual'].values))
        if sub.iloc[pred_idx]['Party'] == sub.iloc[actual_idx]['Party']:
            correct += 1
        total += 1
    acc = float(correct/total) if total>0 else 0.0
    outp = Path(out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, outp)
    meta_path = outp.parent / 'metadata.json'
    meta_to_save = {'party_map': meta['party_map'], 'year_mean': meta['year_mean'], 'r2': float(r2), 'mse': float(mse), 'winner_acc': acc}
    meta_path.write_text(json.dumps(meta_to_save))
    metrics = {'mse': float(mse), 'r2': float(r2), 'winner_acc': acc}
    print('Training complete. Metrics:', metrics)
    return model, metrics

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_csv', default=None)
    parser.add_argument('--out', default='model/model_reg.pkl')
    parser.add_argument('--evaluate', action='store_true')
    args = parser.parse_args()
    df = load_dataset_df(args.data_csv)
    model, metrics = train_and_save_model(df, out=args.out)
    if args.evaluate:
        print('Eval metrics:', metrics)
""")

# templates
os.makedirs(os.path.join(root, "templates"), exist_ok=True)
files["templates/index.html"] = textwrap.dedent("""
{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block content %}
<div class="space-y-6">
  <div>
    <h1 class="text-3xl font-bold">Election Exit-Poll → Winner Predictor</h1>
    <p class="text-gray-400">Enter parties and their exit-poll numbers; the model predicts Actual votes and selects a winner.</p>
  </div>

  <div class="grid md:grid-cols-3 gap-6">
    <div class="card p-6 rounded">
      <h3 class="font-semibold mb-2">Input</h3>
      <form method="post" action="/predict" id="predForm">
        <div class="mb-3"><label class="text-sm text-gray-300">Year</label><input name="year" value="{{ metrics.year_mean if metrics else 2019 }}" class="mt-1 block w-40 rounded bg-gray-800 px-3 py-2"></div>
        <div class="grid grid-cols-1 gap-3">
          {% for i in range(1,7) %}
          <div>
            <label class="text-sm text-gray-300">Party name</label>
            <input name="party_name_{{i}}" class="mt-1 block w-full rounded bg-gray-800 px-3 py-2" placeholder="BJP">
            <label class="text-sm text-gray-300 mt-2">Exit poll</label>
            <input name="exited_{{i}}" class="mt-1 block w-full rounded bg-gray-800 px-3 py-2" placeholder="120">
          </div>
          {% endfor %}
        </div>
        <div class="pt-4"><button class="px-4 py-2 bg-green-500 rounded">Predict Winner</button></div>
      </form>
    </div>

    <div class="card p-6 rounded col-span-2">
      <h3 class="font-semibold mb-2">Dataset preview</h3>
      <div class="text-sm text-gray-300">
        {% if preview and preview|length>0 %}
          <table class="w-full text-sm"><thead><tr><th>Year</th><th>Party</th><th>ExitPoll</th><th>Actual</th></tr></thead>
            <tbody>
            {% for r in preview %}
              <tr><td>{{ r.Year }}</td><td>{{ r.Party }}</td><td>{{ r.ExitPoll }}</td><td>{{ r.Actual }}</td></tr>
            {% endfor %}
            </tbody>
          </table>
        {% else %}
          <div>No dataset preview available. Place CSV at data/election_all.csv or ensure kagglehub can download the dataset.</div>
        {% endif %}
      </div>
      <div class="mt-4 text-sm text-gray-400">
        Model metrics (from training): MSE={{ metrics.mse if metrics else 'N/A' }}, R²={{ metrics.r2 if metrics else 'N/A' }}, Winner-accuracy={{ metrics.winner_acc if metrics else 'N/A' }}
      </div>
    </div>
  </div>
</div>
{% endblock %}
""")

files["templates/base.html"] = textwrap.dedent("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{% block title %}Election Predictor{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style> body{background:#0f172a;color:#e5e7eb} .card{background:rgba(15,23,42,0.7);padding:1rem;border-radius:.5rem;} </style>
  </head>
  <body class="p-6">
    <main class="max-w-5xl mx-auto">
      {% block content %}{% endblock %}
    </main>
  </body>
</html>
""")

files["templates/result.html"] = textwrap.dedent("""
{% extends 'base.html' %}
{% block title %}Result{% endblock %}
{% block content %}
<div class="space-y-6">
  <div>
    <h1 class="text-2xl font-bold">Prediction Result</h1>
    <p class="text-gray-400">Predicted winner based on model's estimated Actual votes.</p>
  </div>
  <div class="card">
    <h3 class="font-semibold">Winner</h3>
    <div class="mt-2 text-lg">{{ winner.party }} — predicted votes: {{ '%.0f'|format(winner.predicted_actual) }}</div>
  </div>

  <div class="card">
    <h3 class="font-semibold">Breakdown</h3>
    <table class="w-full text-sm"><thead><tr><th>Party</th><th class="text-right">ExitPoll</th><th class="text-right">Predicted Actual</th></tr></thead>
    <tbody>
      {% for e in entries %}
      <tr><td>{{ e.party }}</td><td class="text-right">{{ e.exit }}</td><td class="text-right">{{ '%.0f'|format(e.predicted_actual) }}</td></tr>
      {% endfor %}
    </tbody>
    </table>
  </div>

  <div class="card text-sm text-gray-400">
    <h3 class="font-semibold">Model metrics</h3>
    <div>MSE: {{ metrics.mse }}</div>
    <div>R²: {{ metrics.r2 }}</div>
    <div>Winner-accuracy (dataset estimate): {{ metrics.winner_acc }}</div>
  </div>

  <div><a href="/" class="px-3 py-2 bg-gray-700 rounded">Back</a></div>
</div>
{% endblock %}
""")

# create model metadata placeholder
os.makedirs(os.path.join(root, "model"), exist_ok=True)
meta = {"party_map":{}, "year_mean":2019, "r2":0.0, "mse":0.0, "winner_acc":0.0}
with open(os.path.join(root, "model", "metadata.json"), "w") as f:
    json.dump(meta, f)

# write files
for path, content in files.items():
    full = os.path.join(root, path)
    d = os.path.dirname(full)
    os.makedirs(d, exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)

# zip
zip_path = "./election_project_kagglehub.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for folder, subs, filelist in os.walk(root):
        for fn in filelist:
            full = os.path.join(folder, fn)
            arc = os.path.relpath(full, root)
            zf.write(full, arc)

print(json.dumps({"zip": zip_path, "root": root}, indent=2))


