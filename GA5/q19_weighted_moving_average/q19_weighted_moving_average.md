# GA5 — Q19: Weighted Moving Average (WMA) — Regional Revenue Analysis

## Problem Summary

A retail chain operates across four regions: **North, South, East, and West**.  
The analytics team uses a **Weighted Moving Average (WMA)** to smooth revenue trends, giving higher importance to recent weeks.

For this task, the assigned region is:

**East**

The dataset `q-wma-regional-sales.csv` contains weekly sales data for all regions across **26 weeks**.

---

## Dataset Columns

| Column | Description |
|------|-------------|
| Region | Sales region (North / South / East / West) |
| Week | Week number (1–26) |
| Units_Sold | Number of units sold that week |
| Unit_Price | Average selling price |
| Revenue | Precomputed value = Units_Sold × Unit_Price |

---

## Objective

Compute the **5-week Weighted Moving Average (WMA)** of **Revenue** for **Week 26** in the **East region**.

The WMA uses the following weights:

| Week | Weight |
|----|----|
| Week 22 | 1 |
| Week 23 | 2 |
| Week 24 | 3 |
| Week 25 | 4 |
| Week 26 | 5 |

The divisor is the sum of weights:

\[
1 + 2 + 3 + 4 + 5 = 15
\]

---

## WMA Formula

\[
WMA = \frac{(1\times R_{22}) + (2\times R_{23}) + (3\times R_{24}) + (4\times R_{25}) + (5\times R_{26})}{15}
\]

Where:

- \(R_{22}\) = Revenue in Week 22  
- \(R_{23}\) = Revenue in Week 23  
- \(R_{24}\) = Revenue in Week 24  
- \(R_{25}\) = Revenue in Week 25  
- \(R_{26}\) = Revenue in Week 26  

---

## Steps Performed

1. Loaded `q-wma-regional-sales.csv`.
2. Filtered rows where **Region = East**.
3. Sorted the data by **Week (ascending)**.
4. Extracted the **Revenue values for weeks 22–26**.
5. Applied the **Weighted Moving Average formula** using weights `[1,2,3,4,5]`.

---

## Example Python Calculation

```python
import pandas as pd

df = pd.read_csv("q-wma-regional-sales.csv")

east = df[df["Region"] == "East"].sort_values("Week")

revenues = east[east["Week"].isin([22,23,24,25,26])]["Revenue"].values

wma = (1*revenues[0] + 2*revenues[1] + 3*revenues[2] + 4*revenues[3] + 5*revenues[4]) / 15

print(round(wma, 2))
```

---

## Final Answer

```
22622.44
```

This represents the **5-week Weighted Moving Average of revenue for Week 26 in the East region**, rounded to **2 decimal places**.
