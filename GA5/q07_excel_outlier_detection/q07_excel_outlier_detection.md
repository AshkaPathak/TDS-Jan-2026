# GA5 — Q7: Outlier Detection with Excel Z-Score Method

## Problem Summary

The objective of this task was to identify **statistical outliers** in delivery time data using the **Z-score method**.

The dataset contained **200 delivery times** (in minutes) stored in a single column:

```
Delivery_Minutes
```

The task required computing the Z-score for each value and counting how many observations satisfied:

```
|Z| > 2
```

This threshold is commonly used to flag observations that lie **more than two standard deviations away from the mean**, indicating potential anomalies.

The final answer must be **the count of such outliers**.

---

## Dataset

The input file used was:

```
q-outlier-detection-excel.csv
```

Repository location:

```
GA5/q07_excel_outlier_detection/q-outlier-detection-excel.csv
```

The dataset contains **200 delivery time records**.

---

## Z-Score Formula

The Z-score for each observation is computed as:

```
Z = (Value − Mean) / StandardDeviation
```

Where:

- **Mean** = average of all values
- **StandardDeviation** = sample standard deviation

The problem explicitly required using Excel’s **STDEV** function, which corresponds to the **sample standard deviation (n−1)**.

---

## Approach

### Step 1 — Load the Dataset

The CSV file was loaded using pandas.

```
df = pd.read_csv("q-outlier-detection-excel.csv")
```

---

### Step 2 — Compute Mean and Standard Deviation

The mean and sample standard deviation of the delivery times were computed.

In Python, the sample standard deviation equivalent to Excel’s `STDEV` is:

```
values.std(ddof=1)
```

---

### Step 3 — Compute Z-Scores

The Z-score for each record was calculated using:

```
z_scores = (values - mean) / std
```

---

### Step 4 — Identify Outliers

A delivery time was flagged as an outlier if:

```
|Z| > 2
```

The total number of such records was counted.

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy"]
# ///

import pandas as pd
import numpy as np

df = pd.read_csv("q-outlier-detection-excel.csv")

values = df["Delivery_Minutes"]

mean = values.mean()
std = values.std(ddof=1)

z_scores = (values - mean) / std

outliers = np.sum(np.abs(z_scores) > 2)

print("Outliers:", int(outliers))
```

---

## Script Output

Running the script:

```
uv run solution.py
```

produced:

```
Outliers: 9
```

---

## Final Answer Submitted

```
9
```

---

## Repository Structure

```
GA5/q07_excel_outlier_detection/
├── q-outlier-detection-excel.csv
├── solution.py
└── q07_excel_outlier_detection.md
```

---

## Conclusion

Using the **Z-score method with |Z| > 2** and the **sample standard deviation**, the number of anomalous delivery times identified in the dataset was:

```
9
```

This value was submitted as the final answer.
