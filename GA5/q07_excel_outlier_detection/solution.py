# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy"]
# ///

import pandas as pd
import numpy as np

df = pd.read_csv("q-outlier-detection-excel.csv")

values = df["Delivery_Minutes"]

mean = values.mean()
std = values.std(ddof=1)   # sample standard deviation

z_scores = (values - mean) / std

outliers = np.sum(np.abs(z_scores) > 2)

print("Outliers:", int(outliers))
