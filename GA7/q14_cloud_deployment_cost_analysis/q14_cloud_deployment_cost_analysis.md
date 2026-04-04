# GA7 — Q14: Cloud Deployment Cost & Performance Analysis

## Problem Summary

The task is to determine the cheapest viable cloud instance type that satisfies all 28 deployment requests under the given latency model and strict latency thresholds.

---

## Instance Catalogue

- A → 2 vCPU, 4 GB RAM, $0.05/hour
- B → 4 vCPU, 8 GB RAM, $0.10/hour
- C → 8 vCPU, 16 GB RAM, $0.20/hour

---

## Latency Formula

For each request and each instance type:

`latency_ms = 50 × max(1, cpu_req / inst_vCPU + ram_req / inst_RAM)`

A request is satisfied only if:

`latency_ms <= Latency Threshold`

An instance type is viable only if it satisfies **all 28 requests**.

---

## Step 1 — Check Instance A

Using 2 vCPU and 4 GB RAM, several requests exceed their latency thresholds.

So:

- A is **not viable**

---

## Step 2 — Check Instance B

Using 4 vCPU and 8 GB RAM, some requests still exceed their latency thresholds.

So:

- B is **not viable**

---

## Step 3 — Check Instance C

Using 8 vCPU and 16 GB RAM, all 28 requests satisfy:

`latency_ms <= Latency Threshold`

So:

- C is **viable**

---

## Step 4 — Choose the Cheapest Viable Instance

Since:

- A is not viable
- B is not viable
- C is viable

the cheapest viable instance is:

`("C", 0.20)`

---

## Final Answer

```text
("C", 0.20)
