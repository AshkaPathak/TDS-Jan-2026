# GA5 — Q5: Multiple Linear Regression with Excel Data Analysis ToolPak

## Problem Summary

The objective of this task was to build a **multiple linear regression model** to predict residential property prices using historical housing data.

The dataset contained **200 properties** with the following columns:

- `Area_SqFt`
- `Bedrooms`
- `Age_Years`
- `Distance_City_Center_Km`
- `Price`

The task required fitting a regression model with:

- **Dependent variable:** `Price`
- **Predictor variables:** `Area_SqFt`, `Bedrooms`, `Age_Years`, `Distance_City_Center_Km`

Then, using the fitted coefficients, the price had to be predicted for the following property:

- `Area_SqFt = 1800`
- `Bedrooms = 3`
- `Age_Years = 10`
- `Distance_City_Center_Km = 5`

The required submission format was a **numeric value rounded to 2 decimal places**.

---

## Dataset

The input file used was:

```text
q-regression-excel.csv
```

Repository location:

```text
GA5/q05_excel_multiple_regression/q-regression-excel.csv
```

The dataset contained 200 rows representing historical residential property sale data.

---

## Approach

## Step 1 — Load the Dataset

The CSV file was loaded using pandas.

```python
df = pd.read_csv("q-regression-excel.csv")
```

---

## Step 2 — Define Predictors and Target

The predictor variables were:

- `Area_SqFt`
- `Bedrooms`
- `Age_Years`
- `Distance_City_Center_Km`

The target variable was:

- `Price`

---

## Step 3 — Add the Intercept

A constant term was added to the predictor matrix to represent the regression intercept.

```python
X = sm.add_constant(X)
```

---

## Step 4 — Fit the Multiple Linear Regression Model

An OLS regression model was fit using `statsmodels`.

```python
model = sm.OLS(y, X).fit()
```

This produced the following coefficients:

- Intercept (`const`) = `95869.259958`
- `Area_SqFt` = `196.988117`
- `Bedrooms` = `7478.022321`
- `Age_Years` = `-669.569200`
- `Distance_City_Center_Km` = `-3068.284366`

---

## Step 5 — Compute the Prediction

The predicted price was calculated using:

```text
Predicted_Price = Intercept
                + Coef_Area × 1800
                + Coef_Bedrooms × 3
                + Coef_Age × 10
                + Coef_Distance × 5
```

Substituting the coefficients:

```text
Predicted_Price = 95869.259958
                + 196.988117 × 1800
                + 7478.022321 × 3
                - 669.569200 × 10
                - 3068.284366 × 5
```

This gave the final predicted price:

```text
450844.82
```

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "statsmodels"]
# ///

import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("q-regression-excel.csv")

X = df[["Area_SqFt", "Bedrooms", "Age_Years", "Distance_City_Center_Km"]]
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

print("\nPredicted price:", round(prediction, 2))
```

---

## Script Output

Running the script:

```bash
uv run solution.py
```

produced:

```text
const                      95869.259958
Area_SqFt                    196.988117
Bedrooms                    7478.022321
Age_Years                   -669.569200
Distance_City_Center_Km    -3068.284366
dtype: float64

Predicted price: 450844.82
```

---

## Final Answer Submitted

```text
450844.82
```

---

## Repository Structure

```text
GA5/q05_excel_multiple_regression/
├── q-regression-excel.csv
├── solution.py
└── q05_excel_multiple_regression.md
```

---

## Conclusion

Using a multiple linear regression model with `Price` as the dependent variable and the four given predictors, the predicted property price for the specified input values was:

```text
450844.82
```

This was the final submitted answer.
