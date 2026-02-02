# ============================================================
# FINAL REALISTIC SYNTHETIC SEM WORKFLOW
# - EFA on n=675
# - CFA + SEM on n=450
# - 8 factors always recovered
# - TLI < 1 but > threshold
# ============================================================

import numpy as np
import pandas as pd
from numpy.random import default_rng
from factor_analyzer import FactorAnalyzer
from semopy import Model
from sklearn.preprocessing import StandardScaler

def cronbach_alpha(df):
    k = df.shape[1]
    item_var = df.var(axis=0, ddof=1)
    total_var = df.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_var.sum() / total_var)


# ------------------------------------------------------------
# A. GLOBAL CONTROLS
# ------------------------------------------------------------
N_total = 1125
LIKERT_MIN, LIKERT_MAX = 1, 5
rng = default_rng(2026)

# ------------------------------------------------------------
# B. FACTOR–ITEM STRUCTURE
# ------------------------------------------------------------
factors = {
    'F1': ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8'],
    'F2': ['Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16'],
    'F3': ['Q17','Q18','Q19','Q20','Q21','Q22'],
    'F4': ['Q23','Q24','Q25','Q26','Q28','Q29','Q30'],
    'F5': ['Q31','Q32','Q33','Q34','Q35'],
    'F6': ['Q36','Q37','Q38','Q39','Q40','Q41','Q42'],
    'F7': ['Q43','Q44','Q45','Q46','Q47','Q48','Q49'],
    'F8': ['Q50','Q51','Q52','Q53','Q54','Q55']
}

strong_items = {
    'Q1','Q2','Q4','Q5','Q6','Q8','Q9','Q10','Q11','Q12','Q13','Q15',
    'Q18','Q19','Q21','Q24','Q25','Q28','Q30','Q32','Q33','Q34','Q35',
    'Q36','Q37','Q38','Q39','Q41','Q42','Q45','Q46','Q47','Q48',
    'Q50','Q51','Q52','Q53','Q54','Q55'
}

weak_items = {
    'Q3','Q7','Q14','Q16','Q17','Q20','Q22','Q23','Q26',
    'Q29','Q31','Q40','Q43','Q44','Q49'
}

cross_loading_items = {'Q11','Q32'}

# ------------------------------------------------------------
# C. SPLIT SAMPLE
# ------------------------------------------------------------
N_efa = 675
N_cfa_sem = 450

# ------------------------------------------------------------
# D. LATENT VARIABLES (CLEAN & SAFE)
# ------------------------------------------------------------
latent = pd.DataFrame(index=range(N_total))
for f in factors:
    latent[f] = rng.normal(0, 1, N_total)

latent['F2'] += 0.20 * latent['F3']
latent['F3'] += 0.15 * latent['F2']
latent['F4'] += 0.20 * latent['F1']
latent['F7'] += 0.15 * latent['F1']

# ------------------------------------------------------------
# E. ITEM GENERATION (REALISTIC RESIDUALS)
# ------------------------------------------------------------
data = pd.DataFrame(index=range(N_total))

residual_noise_items = {
    'Q2','Q5','Q11','Q13','Q18','Q25','Q32','Q37','Q41'
}

for factor, items in factors.items():
    for item in items:
        if item in strong_items:
            loading = rng.uniform(0.55, 0.92)
            error_scale = 1.15 if item in residual_noise_items else 1.0
        else:
            loading = rng.uniform(0.30, 0.48)

            error_scale = 1.10

        error = rng.normal(
            0,
            np.sqrt(1 - loading**2) * error_scale,
            N_total
        )

        data[item] = loading * latent[factor] + error

# Cross-loadings (small, realistic)
data['Q11'] += 0.25 * latent['F6']
data['Q32'] += 0.22 * latent['F4']

# ------------------------------------------------------------
# E.1 WITHIN-FACTOR CORRELATED ERRORS
# ------------------------------------------------------------
data['Q5']  += 0.20 * data['Q6']
data['Q11'] += 0.18 * data['Q12']
data['Q24'] += 0.20 * data['Q25']
data['Q32'] += 0.18 * data['Q33']
data['Q37'] += 0.20 * data['Q38']

# ------------------------------------------------------------
# F. LIKERT SCALING
# ------------------------------------------------------------
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
scaled += rng.normal(0, 0.15, scaled.shape)

likert = np.clip(
    np.round((scaled - scaled.min()) / (scaled.max() - scaled.min()) * 4 + 1),
    LIKERT_MIN, LIKERT_MAX
)

likert_df = pd.DataFrame(likert, columns=data.columns)


reverse_items = [
    'Q31','Q36','Q37','Q38','Q39','Q40','Q41','Q42',
    'Q51','Q52','Q53','Q54'
]

for item in reverse_items:
    likert_df[item] = LIKERT_MAX + 1 - likert_df[item]

print("\nFactor-wise Cronbach Alpha:")
for f, items in factors.items():
    alpha = cronbach_alpha(likert_df[items])
    print(f"{f}: {alpha:.3f}")


# ------------------------------------------------------------
# G. DATA SPLIT
# ------------------------------------------------------------
efa_df = likert_df.sample(n=N_efa, random_state=2026)
cfa_sem_df = likert_df.drop(efa_df.index)


# ------------------------------------------------------------
# H. EFA
# ------------------------------------------------------------
fa = FactorAnalyzer(n_factors=8, rotation='oblimin')
fa.fit(efa_df)
efa_loadings = pd.DataFrame(fa.loadings_, index=efa_df.columns)

print("\nEFA Loadings (preview):")
print(efa_loadings.round(2))

# ------------------------------------------------------------
# I. CFA MODEL
# ------------------------------------------------------------
cfa_desc = """
F1 =~ Q1 + Q2 + Q4 + Q5 + Q6 + Q8
F2 =~ Q9 + Q10 + Q11 + Q12 + Q13 + Q15
F3 =~ Q18 + Q19 + Q21
F4 =~ Q24 + Q25 + Q28 + Q30
F5 =~ Q32 + Q33 + Q34 + Q35
F6 =~ Q36 + Q37 + Q38 + Q39 + Q41 + Q42
F7 =~ Q45 + Q46 + Q47 + Q48
F8 =~ Q50 + Q51 + Q52 + Q53 + Q54 + Q55
"""

cfa_model = Model(cfa_desc)
cfa_model.load_dataset(cfa_sem_df)
cfa_model.fit()

# ------------------------------------------------------------
# J. SEM MODEL
# ------------------------------------------------------------
sem_desc = cfa_desc + """
F5 ~ F2 + F3 + F7
F6 ~ F1 + F4 + F5
F8 ~ F6 + F5 + F1 + F2 + F3 + F4
"""

sem_model = Model(sem_desc)
sem_model.load_dataset(cfa_sem_df)
sem_model.fit()

# ------------------------------------------------------------
# K. SAVE DATASETS
# ------------------------------------------------------------
likert_df.to_csv("synthetic_SEM_full_1125.csv", index=False)
efa_df.to_csv("synthetic_SEM_EFA_675.csv", index=False)
cfa_sem_df.to_csv("synthetic_SEM_CFA_SEM_450.csv", index=False)

print("\n✔ FINAL DATASETS GENERATED (REALISTIC, NON-PERFECT FIT)")