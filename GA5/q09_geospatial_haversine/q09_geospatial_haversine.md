# GA5 — Q9: Geospatial Analysis using Haversine Distance and Correlation

## Problem Summary

The goal of this task was to analyze whether **distance from the company headquarters affects store revenue**.

The dataset contains **30 store locations across India** with the following columns:

```
Store_ID
Latitude
Longitude
Monthly_Revenue
```

The headquarters location is:

```
Latitude = 28.6139
Longitude = 77.209
(New Delhi)
```

The task required:

1. Computing the **Haversine distance (in km)** between each store and headquarters.
2. Creating a new column **Distance_Km**.
3. Computing the **Pearson correlation coefficient** between:
   
```
Distance_Km
Monthly_Revenue
```

The final result must be **rounded to 4 decimal places**.

---

# Haversine Distance Formula

The Haversine formula calculates the **great-circle distance between two points on a sphere** using latitude and longitude.

```
a = sin²(Δφ / 2) + cos(φ1) * cos(φ2) * sin²(Δλ / 2)

c = 2 * atan2( √a , √(1 − a) )

distance = R * c
```

Where:

```
R = 6371 km (Earth radius)
φ = latitude in radians
λ = longitude in radians
```

---

# Approach

## Step 1 — Load the dataset

```
df = pd.read_csv("q-geospatial-haversine-correlation.csv")
```

---

## Step 2 — Convert coordinates to radians

The trigonometric functions require angles in **radians**.

```
lat1 = radians(28.6139)
lon1 = radians(77.209)

lat2 = radians(store latitude)
lon2 = radians(store longitude)
```

---

## Step 3 — Compute Haversine distance

```
dlat = lat2 - lat1
dlon = lon2 - lon1
```

```
a = sin(dlat/2)^2 + cos(lat1)*cos(lat2)*sin(dlon/2)^2
c = 2*atan2(√a, √(1-a))
```

```
distance = 6371 * c
```

This produced the **Distance_Km column**.

---

## Step 4 — Compute correlation

The Pearson correlation between distance and revenue was calculated using:

```
corr = df["Distance_Km"].corr(df["Monthly_Revenue"])
```

The result was rounded to **4 decimal places**.

---

# Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy"]
# ///

import pandas as pd
import numpy as np

df = pd.read_csv("q-geospatial-haversine-correlation.csv")

# HQ coordinates (New Delhi)
lat1 = np.radians(28.6139)
lon1 = np.radians(77.209)

lat2 = np.radians(df["Latitude"])
lon2 = np.radians(df["Longitude"])

dlat = lat2 - lat1
dlon = lon2 - lon1

a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))

df["Distance_Km"] = 6371 * c

corr = df["Distance_Km"].corr(df["Monthly_Revenue"])

print(round(corr,4))
```

---

# Script Output

Running the script:

```
uv run solution.py
```

produced:

```
-0.9057
```

---

# Interpretation

The correlation coefficient is:

```
-0.9057
```

This indicates a **very strong negative relationship** between store distance from headquarters and monthly revenue.

Meaning:

```
Stores farther from HQ tend to have significantly lower revenue.
```

---

# Final Answer Submitted

```
-0.9057
```

---

# Repository Structure

```
GA5/q09_geospatial_haversine_correlation/

solution.py
q-geospatial-haversine-correlation.csv
q09_geospatial_haversine_correlation.md
```
