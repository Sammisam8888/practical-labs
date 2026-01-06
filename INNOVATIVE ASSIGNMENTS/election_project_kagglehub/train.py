
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
