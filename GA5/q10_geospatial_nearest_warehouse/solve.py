import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Load dataset
df = pd.read_csv("q-geospatial-nearest-warehouse.csv")

# Warehouse coordinates
warehouses = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Chennai": (13.0827, 80.2707)
}

# Haversine function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


# Compute distances to each warehouse
for name, (wlat, wlon) in warehouses.items():
    df[name] = df.apply(
        lambda row: haversine(row["Latitude"], row["Longitude"], wlat, wlon),
        axis=1
    )

# Find nearest warehouse
df["Nearest"] = df[["Delhi", "Mumbai", "Chennai"]].idxmin(axis=1)

# Count assignments
counts = df["Nearest"].value_counts()

# Get busiest warehouse
warehouse = counts.idxmax()
count = counts.max()

print(f"{warehouse}, {count}")
