# GA5 — Q14: Python — Multi-Depot Nearest Warehouse Assignment

## Problem Summary

SwiftDeliver operates **5 warehouses** across a metro region.  
Each incoming customer order is automatically assigned to the **nearest warehouse using Haversine distance**.

We are given two datasets:

**1. Warehouses**
```
q-geospatial-python-closest-warehouses.csv
```

Columns:

- `warehouse_id`
- `latitude`
- `longitude`

**2. Orders**
```
q-geospatial-python-closest-orders.csv
```

Columns:

- `order_id`
- `latitude`
- `longitude`

The task is to:

1. Load both datasets in Python.
2. Compute the **Haversine distance** from each order to all 5 warehouses.
3. Assign each order to the **nearest warehouse**.
4. Count how many orders are assigned to each warehouse.
5. Identify the warehouse handling the **highest number of orders**.

---

# Haversine Distance Formula

Because coordinates are on the Earth's surface, Euclidean distance is inaccurate.  
The **Haversine formula** computes great-circle distance between two latitude-longitude points.

\[
a = \sin^2(\Delta\phi/2) + \cos(\phi_1)\cos(\phi_2)\sin^2(\Delta\lambda/2)
\]

\[
c = 2 \cdot atan2(\sqrt{a}, \sqrt{1-a})
\]

\[
distance = R \cdot c
\]

Where:

- \(R = 6371\) km (Earth radius)
- \(\phi\) = latitude
- \(\lambda\) = longitude

---

# Python Implementation

```python
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Load datasets
warehouses = pd.read_csv("q-geospatial-python-closest-warehouses.csv")
orders = pd.read_csv("q-geospatial-python-closest-orders.csv")

# Haversine function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


assignments = []

# Determine nearest warehouse for each order
for _, order in orders.iterrows():

    nearest_wh = None
    min_distance = float("inf")

    for _, wh in warehouses.iterrows():

        d = haversine(
            order["latitude"],
            order["longitude"],
            wh["latitude"],
            wh["longitude"]
        )

        if d < min_distance:
            min_distance = d
            nearest_wh = wh["warehouse_id"]

    assignments.append(nearest_wh)

orders["assigned_wh"] = assignments


# Count assignments per warehouse
counts = orders["assigned_wh"].value_counts()

top_wh = counts.idxmax()
top_count = counts.max()

print(top_wh, top_count)
```

---

# Result

After computing distances and assigning orders to the nearest warehouse, the order distribution was calculated.

The warehouse with the highest number of assigned orders is:

```
WH-01, 18 orders
```

---

# Why This Works

This solution correctly identifies the busiest warehouse because:

- Haversine distance accounts for Earth's curvature
- Each order is assigned to the **closest fulfillment center**
- Counting assignments reveals which warehouse handles the most orders

This same approach is widely used in:

- e-commerce fulfillment routing
- logistics optimization
- ride-sharing dispatch systems
- delivery fleet planning

---

# Final Answer

```
WH-01, 18 orders
```
