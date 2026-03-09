# GA5 — Q6: Seasonal Forecasting with Excel FORECAST.ETS

## Problem Summary

The objective of this task was to forecast the number of website visitors for **Month 37** using historical traffic data.

The dataset contained **36 months of visitor counts** and the forecasting had to be performed using **Excel’s FORECAST.ETS function**, which implements **triple exponential smoothing (Holt-Winters)** to model:

- Level
- Trend
- Seasonality

The data shows a clear **yearly seasonal pattern**, so the seasonal period is **12 months**.

The required forecast formula in Excel is:

```
=FORECAST.ETS(37, B2:B37, A2:A37, 12)
```

Where:

- `37` → the month to forecast  
- `B2:B37` → historical visitor counts  
- `A2:A37` → timeline (months 1–36)  
- `12` → seasonal cycle (12 months per year)

The final answer must be:

- **rounded to the nearest integer**

---

## Dataset

The input file used was:

```
q-forecasting-excel.csv
```

Repository location:

```
GA5/q06_excel_seasonal_forecast/q-forecasting-excel.csv
```

The dataset contains two columns:

```
Month
Visitors
```

with **36 monthly observations**.

---

## Approach

### Step 1 — Load the Dataset

The CSV file was loaded using pandas.

```python
df = pd.read_csv("q-forecasting-excel.csv")
```

The `Visitors` column contains the historical traffic values used for forecasting.

---

### Step 2 — Fit an ETS Model

Excel’s `FORECAST.ETS` is equivalent to **Holt-Winters exponential smoothing** with:

- additive trend
- additive seasonality
- seasonal period = 12

This was implemented in Python using:

```
statsmodels.tsa.holtwinters.ExponentialSmoothing
```

with parameters:

```
trend = "add"
seasonal = "add"
seasonal_periods = 12
```

---

### Step 3 — Generate the Forecast

Once the model was fitted on the 36 historical values, the forecast for **Month 37** was generated using:

```
forecast = model.forecast(1)
```

The predicted value was then rounded to the nearest integer as required.

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "statsmodels"]
# ///

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("q-forecasting-excel.csv")

visitors = df["Visitors"]

model = ExponentialSmoothing(
    visitors,
    trend="add",
    seasonal="add",
    seasonal_periods=12
).fit()

forecast = model.forecast(1)

print("Forecast Month 37:", round(forecast.iloc[0]))
```

---

## Script Output

Running the script:

```
uv run solution.py
```

produced:

```
Forecast Month 37: 15873
```

---

## Final Answer Submitted

```
15873
```

---

## Repository Structure

```
GA5/q06_excel_seasonal_forecast/
├── q-forecasting-excel.csv
├── solution.py
└── q06_excel_seasonal_forecast.md
```

---

## Conclusion

Using seasonal exponential smoothing with a **12-month seasonal period**, the predicted number of website visitors for **Month 37** was:

```
15873
```

This value was rounded to the nearest integer and submitted as the final answer.
