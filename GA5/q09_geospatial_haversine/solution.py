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

# store coordinates
lat2 = np.radians(df["Latitude"])
lon2 = np.radians(df["Longitude"])

# haversine formula
dlat = lat2 - lat1
dlon = lon2 - lon1

a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))

distance = 6371 * c

df["Distance_Km"] = distance

corr = df["Distance_Km"].corr(df["Monthly_Revenue"])

print(round(corr,4))
