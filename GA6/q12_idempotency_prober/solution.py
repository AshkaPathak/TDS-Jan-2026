import pandas as pd
import numpy as np

df = pd.read_csv("23f3002663_ds_study_iitm_ac_in_records.csv")

def preprocess(df, monotone_col):
    result = df.copy()
    for col in result.select_dtypes(include="number").columns:
        result[col] = result[col].clip(0, 100)
    result = result.ffill().fillna(0)
    return result

processed1 = preprocess(df, "value_a")
processed2 = preprocess(processed1, "value_a")

# 1) Idempotency violations
num_cols = processed1.select_dtypes(include="number").columns.tolist()
other_cols = [c for c in processed1.columns if c not in num_cols]

idempotency_violations = 0
for i in range(len(df)):
    violated = False

    for c in num_cols:
        a = processed1.iloc[i][c]
        b = processed2.iloc[i][c]
        if pd.isna(a) and pd.isna(b):
            continue
        if abs(a - b) > 1e-9:
            violated = True
            break

    if not violated:
        for c in other_cols:
            if processed1.iloc[i][c] != processed2.iloc[i][c]:
                violated = True
                break

    if violated:
        idempotency_violations += 1

# 2) Monotonicity violations
orig = df["value_a"]
proc = processed1["value_a"]

monotonicity_violations = 0
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        if pd.isna(orig.iloc[i]) or pd.isna(orig.iloc[j]):
            continue

        if orig.iloc[i] > orig.iloc[j]:
            if not (proc.iloc[i] > proc.iloc[j]):
                monotonicity_violations += 1
        elif orig.iloc[j] > orig.iloc[i]:
            if not (proc.iloc[j] > proc.iloc[i]):
                monotonicity_violations += 1

# 3) Null stability violations
null_stability_violations = 0
for i in range(len(df)):
    if df.iloc[i].isna().sum() == 0 and processed1.iloc[i].isna().sum() > 0:
        null_stability_violations += 1

print(f"{idempotency_violations},{monotonicity_violations},{null_stability_violations}")
