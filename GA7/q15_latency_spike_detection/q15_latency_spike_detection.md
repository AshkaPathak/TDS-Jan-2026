# GA7 — Q15: Service Latency Spike Detection & Scaling Decisions

## Problem Summary

The task is to detect latency spikes using a statistical threshold based on population standard deviation, then assign a scaling decision for each spike and output the results in sorted tuple format.

---

## Step 1 — Spike Detection

- Compute mean of all 60 latency values  
- Compute **population standard deviation** (divide by N = 60)  
- Threshold = mean + 2 × std  

A row is a spike if:

Latency (ms) > threshold

---

## Step 2 — Threshold Calculation

- Mean ≈ 58.82  
- Population std ≈ 13.08  
- Threshold ≈ 84.99  

---

## Step 3 — Identify Spike Rows

Rows where latency exceeds threshold:

- Row 5 → 96  
- Row 7 → 96  
- Row 21 → 96  
- Row 38 → 91  
- Row 54 → 93  

---

## Step 4 — Scaling Decision

Rule:

- If max(CPU Util, RAM Util) ≥ 80 → SCALE_UP  
- Otherwise → MONITOR  

Applying:

- Row 5 → max(64, 67) → MONITOR  
- Row 7 → max(87, 63) → SCALE_UP  
- Row 21 → max(64, 40) → MONITOR  
- Row 38 → max(69, 95) → SCALE_UP  
- Row 54 → max(73, 45) → MONITOR  

---

## Final Answer

```text
[(5, "MONITOR"), (7, "SCALE_UP"), (21, "MONITOR"), (38, "SCALE_UP"), (54, "MONITOR")]
