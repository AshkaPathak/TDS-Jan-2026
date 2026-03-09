# GA5 — Q8: Exponential Moving Average (EMA) for Stock Momentum

## Problem Summary

The objective of this task was to compute the **21-day Exponential Moving Average (EMA)** for multiple technology stocks and identify which stock has the **highest EMA on the most recent trading day**.

The dataset contained daily closing prices for five tickers:

- AAPL
- MSFT
- GOOGL
- AMZN
- META

Each ticker had approximately **126 trading days (~6 months)** of historical price data.

The goal was to:

1. Compute the **21-day EMA** for each ticker.
2. Identify the **latest date in the dataset**.
3. Determine which ticker had the **highest EMA value on that date**.
4. Submit the **EMA value (rounded to 2 decimal places) and ticker symbol**.

---

## Dataset

Input file:

```
q-stock-prices-ema.csv
```

Repository location:

```
GA5/q08_python_exponential_moving_average/q-stock-prices-ema.csv
```

Columns included:

```
Date
Ticker
Close_Price
```

---

## EMA Formula

The **Exponential Moving Average** gives higher weight to recent prices.

Multiplier:

```
k = 2 / (span + 1)
```

For a **21-day EMA**:

```
k = 2 / 22 ≈ 0.0909
```

Recursive formula:

```
EMA[i] = Price[i] × k + EMA[i-1] × (1 - k)
```

---

## Approach

### Step 1 — Load Dataset

The CSV file was loaded using pandas.

```
df = pd.read_csv("q-stock-prices-ema.csv")
```

---

### Step 2 — Compute 21-Day EMA per Ticker

The EMA must be calculated **separately for each stock**.

Pandas `groupby()` ensures calculations are performed independently per ticker.

```
df["EMA_21"] = df.groupby("Ticker")["Close_Price"].transform(
    lambda x: x.ewm(span=21, adjust=False).mean()
)
```

Using `adjust=False` ensures the **standard recursive EMA formula**.

---

### Step 3 — Identify the Most Recent Date

```
last_date = df["Date"].max()
```

---

### Step 4 — Filter Records from the Last Day

```
last_day = df[df["Date"] == last_date]
```

---

### Step 5 — Find the Stock with Highest EMA

```
row = last_day.loc[last_day["EMA_21"].idxmax()]
```

---

### Step 6 — Format Output

The EMA value was rounded to **two decimal places**.

```
ema = round(row["EMA_21"], 2)
ticker = row["Ticker"]
```

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas"]
# ///

import pandas as pd

df = pd.read_csv("q-stock-prices-ema.csv")

df["EMA_21"] = df.groupby("Ticker")["Close_Price"].transform(
    lambda x: x.ewm(span=21, adjust=False).mean()
)

last_date = df["Date"].max()
last_day = df[df["Date"] == last_date]

row = last_day.loc[last_day["EMA_21"].idxmax()]

ema = round(row["EMA_21"], 2)
ticker = row["Ticker"]

print(f"{ema}, {ticker}")
```

---

## Script Output

Running the script:

```
uv run solution.py
```

produced:

```
591.93, AMZN
```

---

## Final Answer Submitted

```
591.93, AMZN
```

---

## Repository Structure

```
GA5/q08_python_exponential_moving_average/
├── q-stock-prices-ema.csv
├── solution.py
└── q08_python_exponential_moving_average.md
```

---

## Conclusion

After computing the **21-day EMA for each ticker** and comparing values on the most recent trading day, the stock with the **highest EMA** was:

```
591.93, AMZN
```
