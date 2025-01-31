import pandas as pd

# Load datasets
demo = pd.read_sas("P_DEMO.XPT", format='xport')[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH3']]
biopro = pd.read_sas("P_BIOPRO.XPT", format='xport')[['SEQN', 'LBXSCR']]
alb_cr = pd.read_sas("P_ALB_CR.XPT", format='xport')[['SEQN', 'URXUMA', 'URXUCR']]
ghb = pd.read_sas("P_GHB.XPT", format='xport')[['SEQN', 'LBXGH']]
cbc = pd.read_sas("P_CBC.XPT", format='xport')[['SEQN', 'LBXHGB']]
bpx = pd.read_sas("P_BPXO.XPT", format='xport')[['SEQN', 'BPXOSY1', 'BPXODI1']]  # Updated
bmx = pd.read_sas("P_BMX.XPT", format='xport')[['SEQN', 'BMXBMI', 'BMXWAIST']]
diq = pd.read_sas("P_DIQ.XPT", format='xport')[['SEQN', 'DIQ010']]
mcq = pd.read_sas("P_MCQ.XPT", format='xport')[['SEQN', 'MCQ160B', 'MCQ160C']]
smq = pd.read_sas("P_SMQ.XPT", format='xport')[['SEQN', 'SMQ020']]

# Merge datasets
merged = demo.merge(biopro, on='SEQN', how='left') \
             .merge(alb_cr, on='SEQN', how='left') \
             .merge(ghb, on='SEQN', how='left') \
             .merge(cbc, on='SEQN', how='left') \
             .merge(bpx, on='SEQN', how='left') \
             .merge(bmx, on='SEQN', how='left') \
             .merge(diq, on='SEQN', how='left') \
             .merge(mcq, on='SEQN', how='left') \
             .merge(smq, on='SEQN', how='left')

# Exclude participants <20 years old
merged = merged[merged['RIDAGEYR'] >= 20]

# Calculate eGFR (CKD-EPI formula)
def calculate_egfr(row):
    scr = row['LBXSCR']
    age = row['RIDAGEYR']
    is_female = row['RIAGENDR'] == 2
    is_black = row['RIDRETH3'] == 4

    if is_female:
        k, alpha = 0.7, -0.329
    else:
        k, alpha = 0.9, -0.411

    scr_k = scr / k
    egfr = 141 * (scr_k ** alpha) * (0.993 ** age)
    egfr *= 1.018 if is_female else 1
    egfr *= 1.159 if is_black else 1

    return egfr

merged['eGFR'] = merged.apply(calculate_egfr, axis=1)

# Calculate ACR
merged['ACR'] = (merged['URXUMA'] / (merged['URXUCR'] / 100))  # mg/g

# Remove missing eGFR/ACR
merged = merged.dropna(subset=['eGFR', 'ACR'])

# Define CKD
merged['CKD'] = ((merged['eGFR'] < 60) | (merged['ACR'] >= 30)).astype(int)

# Save
merged.to_csv("nhanes_ckd_2017_2020.csv", index=False)
print("Dataset saved. Final shape:", merged.shape)