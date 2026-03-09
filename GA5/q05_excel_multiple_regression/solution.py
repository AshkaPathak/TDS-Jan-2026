# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "statsmodels"]
# ///

import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("q-regression-excel.csv")

X = df[["Area_SqFt","Bedrooms","Age_Years","Distance_City_Center_Km"]]
y = df["Price"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.params)

intercept = model.params["const"]
coef_area = model.params["Area_SqFt"]
coef_bed = model.params["Bedrooms"]
coef_age = model.params["Age_Years"]
coef_dist = model.params["Distance_City_Center_Km"]

prediction = (
    intercept
    + coef_area * 1800
    + coef_bed * 3
    + coef_age * 10
    + coef_dist * 5
)

print("\nPredicted price:", round(prediction,2))
