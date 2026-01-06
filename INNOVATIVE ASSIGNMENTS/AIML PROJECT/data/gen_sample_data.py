
from pathlib import Path
import csv, random
def gen(out='data/sample_exitpolls.csv', n=1000):
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in range(n):
        age = random.randint(18,80)
        education = random.randint(5,20)
        urban = random.choice([0,1])
        income = random.randint(5000,100000)
        prior_vote = random.choice([0,1])
        prob = 0.3 + 0.01*(education-10) + 0.1*urban + 0.05*(prior_vote)
        label = 1 if random.random() < prob else 0
        rows.append([age, education, urban, income, prior_vote, label])
    with open(out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['age','education','urban','income','prior_vote','label'])
        w.writerows(rows)
    print('written', out)
if __name__=='__main__':
    gen()
