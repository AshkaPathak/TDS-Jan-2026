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
