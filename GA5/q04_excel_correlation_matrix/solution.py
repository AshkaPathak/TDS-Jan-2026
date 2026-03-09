# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy"]
# ///

import pandas as pd

df = pd.read_csv("q-correlation-excel.csv")

corr = df.corr()

print("Correlation Matrix:\n")
print(corr)

# remove diagonal
corr_values = corr.where(~(corr == 1.0))

# find max correlation
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
