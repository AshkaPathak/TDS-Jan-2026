# GA5 — Q10: Geospatial Analysis — Nearest Warehouse Assignment

## Problem Summary

A logistics company operates **3 warehouses across India**:

| Warehouse | Latitude | Longitude |
|----------|----------|-----------|
| Delhi | 28.6139 | 77.2090 |
| Mumbai | 19.0760 | 72.8777 |
| Chennai | 13.0827 | 80.2707 |

We are given a dataset of **50 deliveries** (`q-geospatial-nearest-warehouse.csv`) with the columns:

- `Delivery_ID`
- `Latitude`
- `Longitude`
- `Weight_Kg`

The goal is to determine **which warehouse handles the most deliveries** by assigning each delivery to its **nearest warehouse** using the **Haversine distance formula**.

---

# Approach

The solution consists of the following steps:

1. **Load the dataset** using pandas.
2. **Compute Haversine distance** between each delivery location and each warehouse.
3. Create **three distance columns**:
   - Distance to Delhi
   - Distance to Mumbai
   - Distance to Chennai
4. For each delivery, determine the **minimum distance warehouse**.
5. Count the number of deliveries assigned to each warehouse.
6. Identify the **warehouse with the highest delivery count**.

---

# Haversine Formula

The **Haversine formula** calculates the great-circle distance between two points on the Earth.

\[
a = \sin^2(\frac{\Delta \phi}{2}) + \cos(\phi_1)\cos(\phi_2)\sin^2(\frac{\Delta \lambda}{2})
\]

\[
c = 2 \cdot \arctan2(\sqrt{a}, \sqrt{1-a})
\]

\[
distance = R \cdot c
\]

Where:

- \(R = 6371\) km (Earth radius)
- \(\phi\) = latitude in radians
- \(\lambda\) = longitude in radians

---

# Python Implementation

```python
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

# Haversine distance function
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

# Determine nearest warehouse
df["Nearest"] = df[["Delhi", "Mumbai", "Chennai"]].idxmin(axis=1)

# Count deliveries per warehouse
counts = df["Nearest"].value_counts()

# Identify busiest warehouse
warehouse = counts.idxmax()
count = counts.max()

print(f"{warehouse}, {count}")
```

---

# Result

After computing the distances and assigning each delivery to the nearest warehouse, the delivery counts were calculated.

Final result:

```
Delhi, 19
```

This means:

- **Delhi warehouse handled the most deliveries**
- **Total deliveries assigned = 19**

---

# Why This Works

The algorithm correctly assigns deliveries because:

- Haversine distance accounts for **Earth's curvature**
- Each delivery is assigned to the **warehouse with the minimum geographic distance**
- Counting assignments reveals the **busiest warehouse**

This approach is commonly used in:

- Logistics optimization
- Delivery routing
- Supply chain distribution
- Ride-sharing dispatch systems
---

# Conclusion

Using geospatial distance calculations with the Haversine formula, we assigned each delivery to its nearest warehouse and determined the busiest location.

Final Answer:

```
Delhi, 19
```

✔ Accurate geographic distance calculation  
✔ Correct nearest-warehouse assignment  
✔ Delhi handles the highest number of deliveries
