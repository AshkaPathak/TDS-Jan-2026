# GA4 — Q6: JSON Sensor Roll-Up Analytics

## Problem Summary

ThermalWatch aggregates IoT telemetry from industrial plants. Each device emits a JSON document per minute with nested metrics.

The objective was to compute the **normalized average temperature (°C)** for:

- Site: **Plant-02**
- Devices starting with: **pump**
- Time window:  
  2024-06-19T19:37:11.945Z  
  through  
  2024-07-03T19:37:11.945Z
- Excluding records where status is **maintenance** or **offline**
- Converting all temperature readings to **Celsius**
- Rounding final result to **two decimal places**

---

## Dataset

File used:

q-json-sensor-rollup.jsonl

---

## Data Cleaning & Processing Logic

### 1) Stream JSONL file
Process line-by-line to avoid loading entire dataset into memory.

### 2) Filter Conditions

Apply filters:

- `site == "Plant-02"`
- `device` starts with `"pump"`
- `captured_at` within specified UTC window
- `status` NOT IN ("maintenance", "offline")

---

### 3) Extract Nested Temperature

Temperature structure:

```
metrics.temperature.value
metrics.temperature.unit
```

---

### 4) Convert Fahrenheit → Celsius

Formula:

C = (F − 32) × 5/9

Only convert when unit == "F".

---

### 5) Compute Average

- Sum all cleaned Celsius values
- Count valid records
- Compute:

average = total / count

- Round to 2 decimal places

---

## Final Answer

Average temperature (°C) for pump devices at Plant-02 in the specified window:

**83.24**

---

## Conclusion

✔ JSON streamed safely  
✔ Nested fields handled correctly  
✔ Time window applied precisely  
✔ Maintenance/offline records excluded  
✔ Fahrenheit converted to Celsius  
✔ Rounded to two decimals  
✔ Final validated result: **83.24 °C**
