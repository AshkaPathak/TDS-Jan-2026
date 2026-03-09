# GA5 — Q4: Correlation Matrix with Excel Data Analysis ToolPak

## Problem Summary

The objective of this task was to compute the **Pearson correlation matrix** for a dataset containing behavioral and performance metrics for **120 students**, and identify the **strongest positive correlation between two different variables**.

The dataset included the following columns:

- Study_Hours — daily hours spent studying  
- Sleep_Hours — nightly sleep hours  
- Screen_Time — daily recreational screen hours  
- Attendance_Percent — lecture attendance percentage  
- Exam_Score — final exam score (0–100)

The task required:

1. Generate the full **5 × 5 correlation matrix**
2. Ignore the **diagonal values (1.0)** since a variable is perfectly correlated with itself
3. Identify the **highest positive off-diagonal correlation**
4. Submit the result in the format:

```
Variable1, Variable2, 0.XXXX
```

---

## Dataset

The dataset used was:

```
q-correlation-excel.csv
```

Repository location:

```
GA5/q04_excel_correlation_matrix/q-correlation-excel.csv
```

The dataset contains **120 rows** representing individual students and their behavioral metrics.

---

## Approach

### Step 1 — Load the Dataset

The dataset was loaded using **pandas**:

```python
df = pd.read_csv("q-correlation-excel.csv")
```

---

### Step 2 — Compute the Correlation Matrix

The Pearson correlation matrix was computed using:

```python
corr = df.corr()
```

This generated the full **5 × 5 correlation matrix**.

---

### Step 3 — Ignore Diagonal Values

The diagonal elements equal **1.0**, representing a variable correlated with itself. These values were ignored when searching for the strongest relationship.

---

### Step 4 — Find the Strongest Positive Correlation

All variable pairs were iterated through to find the **largest off-diagonal correlation coefficient**.

The highest value identified was:

```
Study_Hours ↔ Exam_Score
```

with correlation:

```
0.9362
```

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy"]
# ///

import pandas as pd

df = pd.read_csv("q-correlation-excel.csv")

corr = df.corr()

print("Correlation Matrix:\n")
print(corr)

max_pair = None
max_value = -1

for col1 in corr.columns:
    for col2 in corr.columns:
        if col1 != col2:
            value = corr.loc[col1, col2]
            if value > max_value:
                max_value = value
                max_pair = (col1, col2)

print("\nStrongest correlation:")
print(max_pair[0], max_pair[1], round(max_value,4))
```

---

## Script Output

Running the script:

```bash
uv run solution.py
```

produced:

```
Strongest correlation:
Study_Hours Exam_Score 0.9362
```

---

## Final Answer Submitted

```
Study_Hours, Exam_Score, 0.9362
```

---

## Repository Structure

```
GA5/q04_excel_correlation_matrix/
├── q-correlation-excel.csv
├── solution.py
└── q04_excel_correlation_matrix.md
```

---

## Conclusion

The strongest positive relationship in the dataset occurs between:

```
Study_Hours and Exam_Score
```

with Pearson correlation:

```
0.9362
```

This indicates a **very strong positive relationship between study time and exam performance**.
