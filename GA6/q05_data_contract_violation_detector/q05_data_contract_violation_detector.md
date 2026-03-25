# GA6 — Q5: Data Contract Violation Detector

## Problem Summary

A data pipeline processes IoT sensor readings daily.

- Day 1 dataset is clean and defines the expected data contract
- Day 2 dataset contains violations introduced upstream

The task is to:

Count how many rows in Day 2 are anomalous.

A row is anomalous if at least one of its column values violates a rule derived from Day 1.

Each row must be counted only once, even if multiple columns fail.

---

## Key Idea

Day 1 is treated as the source of truth.

For each column:
- Infer its type (numeric, date, categorical)
- Derive constraints from Day 1
- Apply those constraints to Day 2
- Collect violating row indices using a set (to avoid duplicates)

---

## Rules Used

### Rule 1 — Null Check
If a column has 0 nulls in Day 1:
- Any null in Day 2 is anomalous

### Rule 2 — Numeric Column
If more than 95% of Day 1 values can be parsed as numbers:
- Treat as numeric
- Flag if value is:
  - less than Day 1 minimum
  - greater than Day 1 maximum

### Rule 3 — Date Column
If more than 90% of Day 1 values can be parsed as dates:
- Treat as date
- Flag if value is after today

### Rule 4 — Categorical Column
If Day 1 has ≤ 20 unique values:
- Treat as categorical
- Flag if value does not appear in Day 1

---

## Important Notes

- Rules are applied in order: null → numeric → date → categorical
- Once a type is detected, further checks for that column stop
- A set is used to ensure each anomalous row is counted only once

---

## Implementation

```python
import pandas as pd

day1 = pd.read_csv("23f3002663_ds_study_iitm_ac_in.day1.csv")
day2 = pd.read_csv("23f3002663_ds_study_iitm_ac_in.day2.csv")

anomalous_rows = set()
today = pd.Timestamp.today().normalize()

for col in day1.columns:

    # Rule 1: Null check
    if day1[col].isna().sum() == 0:
        bad_nulls = day2[day2[col].isna()].index
        anomalous_rows.update(bad_nulls)

    # Rule 2: Numeric detection
    day1_num = pd.to_numeric(day1[col], errors="coerce")
    if day1_num.notna().mean() > 0.95:
        day2_num = pd.to_numeric(day2[col], errors="coerce")

        bad_numeric = day2[
            (day2_num < day1_num.min()) |
            (day2_num > day1_num.max())
        ].index

        anomalous_rows.update(bad_numeric)
        continue

    # Rule 3: Date detection
    day1_dt = pd.to_datetime(day1[col], errors="coerce")
    if day1_dt.notna().mean() > 0.90:
        day2_dt = pd.to_datetime(day2[col], errors="coerce")

        bad_dates = day2[day2_dt > today].index
        anomalous_rows.update(bad_dates)
        continue

    # Rule 4: Categorical detection
    if day1[col].nunique(dropna=True) <= 20:
        allowed_values = set(day1[col].dropna().unique())

        bad_categorical = day2[~day2[col].isin(allowed_values)].index
        anomalous_rows.update(bad_categorical)

print(len(anomalous_rows))
```

---

## Final Answer

87

---

## Why This Works

- Automatically infers column types from Day 1
- Applies strict validation rules based on observed data
- Uses set union to prevent duplicate row counting
- Covers all violation types:
  - null violations
  - numeric range violations
  - future date violations
  - unseen categorical values

---

## Conclusion

The solution correctly identifies anomalous rows by:

- Deriving constraints from Day 1
- Applying rule-based validation on Day 2
- Aggregating violations using a set

Final Result:

✔ Accurate  
✔ No double counting  
✔ Fully aligned with data contract rules  

Answer: 87
