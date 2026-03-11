# GA5 — Q21: Rideshare Geospatial Revenue Analysis

## Problem Summary

RapidRide is analyzing rideshare trip data to identify the **top-performing driver during peak evening hours for long-distance trips**.

The analysis combines:

- Time filtering
- Geospatial distance calculation (Haversine formula)
- Revenue aggregation

---

# Dataset

File: `rideshare_trips.csv`

| Column | Description |
|------|-------------|
| trip_id | Unique trip identifier |
| driver_id | Driver identifier |
| start_time | Trip start timestamp (UTC) |
| pickup_lat | Pickup latitude |
| pickup_lon | Pickup longitude |
| dropoff_lat | Dropoff latitude |
| dropoff_lon | Dropoff longitude |
| fare_amount | Trip fare in USD |

Total records: **50,000 trips**

---

# Parameters

Peak hours:

```
17:00 – 20:59 UTC
```

Distance threshold:

```
Distance > 4 km
```

---

# Step 1 — Filter by Peak Hours

Extract the hour from `start_time` and keep rows where:

```
hour >= 17 and hour < 21
```

---

# Step 2 — Compute Haversine Distance

Distance between pickup and dropoff coordinates is calculated using the **Haversine formula**.

```
R = 6371 km

Δlat = lat2 - lat1
Δlon = lon2 - lon1

a = sin²(Δlat/2) + cos(lat1) × cos(lat2) × sin²(Δlon/2)

distance = R × 2 × atan2( √a , √(1−a) )
```

Trips are kept only if:

```
distance > 4 km
```

---

# Step 3 — Aggregate Driver Revenue

For the remaining trips:

```
GROUP BY driver_id
SUM(fare_amount)
```

The driver with the **maximum total fare** is selected.

---

# Python Implementation

```python
import pandas as pd
import math

df = pd.read_csv("rideshare_trips.csv")

df["start_time"] = pd.to_datetime(df["start_time"])
df["hour"] = df["start_time"].dt.hour

# Step A: peak hours
peak = df[(df["hour"] >= 17) & (df["hour"] < 21)]

# Haversine
def haversine(row):
    R = 6371
    lat1, lon1 = math.radians(row["pickup_lat"]), math.radians(row["pickup_lon"])
    lat2, lon2 = math.radians(row["dropoff_lat"]), math.radians(row["dropoff_lon"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

peak["dist_km"] = peak.apply(haversine, axis=1)

# Step B: distance filter
long_trips = peak[peak["dist_km"] > 4]

# Step C: top driver
result = long_trips.groupby("driver_id")["fare_amount"].sum()

top_driver = result.idxmax()
top_fare = round(result.max(), 2)

print(top_driver, top_fare)
```

---

# Final Result

```
DRV-065, 888.94
```

This indicates that **driver DRV-065 generated the highest total fare during peak evening hours for trips longer than 4 km**.
