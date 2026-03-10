import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Load data
warehouses = pd.read_csv("q-geospatial-python-closest-warehouses.csv")
orders = pd.read_csv("q-geospatial-python-closest-orders.csv")

# Haversine distance in km
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Assign each order to nearest warehouse
assignments = []

for _, order in orders.iterrows():
    best_wh = None
    best_dist = float("inf")

    for _, wh in warehouses.iterrows():
        d = haversine(
            order["latitude"],
            order["longitude"],
            wh["latitude"],
            wh["longitude"]
        )

        if d < best_dist:
            best_dist = d
            best_wh = wh["warehouse_id"]

    assignments.append(best_wh)

orders["assigned_wh"] = assignments

# Count assignments
counts = orders["assigned_wh"].value_counts()

top_wh = counts.idxmax()
top_count = counts.max()

print(f"{top_wh}, {top_count}")
