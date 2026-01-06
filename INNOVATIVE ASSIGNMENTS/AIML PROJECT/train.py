
import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
import joblib
from pathlib import Path

def gen_sample(out_path):
    import random, csv
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in range(1000):
        age = random.randint(18, 80)
        education = random.randint(5, 20)
        urban = random.choice([0,1])
        income = random.randint(5000, 100000)
        prior_vote = random.choice([0,1])
        prob = 0.3 + 0.01*(education-10) + 0.1*urban + 0.05*(prior_vote)
        label = 1 if random.random() < prob else 0
        rows.append([age, education, urban, income, prior_vote, label])
    with open(out_path, 'w', newline='') as f:
        import csv
        w = csv.writer(f)
        w.writerow(['age','education','urban','income','prior_vote','label'])
        w.writerows(rows)
    print('generated', out_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/sample_exitpolls.csv')
    parser.add_argument('--out', default='model/model.pkl')
    parser.add_argument('--quick', action='store_true')
    args = parser.parse_args()

    data_path = Path(args.data)
    if args.quick and not data_path.exists():
        gen_sample(str(data_path))

    df = pd.read_csv(str(data_path))
    X = df[['age','education','urban','income','prior_vote']].values
    y = df['label'].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, preds)
    acc = accuracy_score(y_test, (preds>0.5).astype(int))
    print(f'Trained model AUC={auc:.4f} ACC={acc:.4f}')
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, args.out)
    print('Saved model to', args.out)

if __name__=='__main__':
    main()
