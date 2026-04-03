# GA7 — Q7: Headline Rewriting: Description vs Finding

## Problem Summary

The task is to classify six chart headlines as either **finding** or **description** using only the dataset table, and for every headline labeled as **description**, rewrite it into a proper **finding** backed by the data.

The required submission format is:

`index|label|rewrite`

Where:
- `label` is either `finding` or `description`
- `rewrite` is included only for descriptions
- exactly one line must be provided for each headline number

---

## Dataset Table

Metric context: **Share (%)**

| Period | Solar | Wind | Coal |
|--------|-------|------|------|
| 2021   | 12    | 21   | 43   |
| 2022   | 14    | 23   | 39   |
| 2023   | 18    | 25   | 34   |

---

## Step 1 — Identify the trends in the table

From the dataset:

- **Solar** rises from **12** in 2021 to **18** in 2023
- **Wind** rises from **21** in 2021 to **25** in 2023
- **Coal** falls from **43** in 2021 to **34** in 2023

So the clear insights are:

- Solar increased by **6 percentage points**
- Wind increased by **4 percentage points**
- Coal decreased by **9 percentage points**
- Wind remains larger than solar in every year
- Coal is still above one-third in 2023 because **34 > 33.33**

---

## Step 2 — Apply the classification rule

A headline is a **finding** if it makes a specific, data-verifiable claim.

A headline is a **description** if it is generic, structural, or only names the chart contents without stating an actual takeaway.

---

## Step 3 — Classify each headline

### 1. Coal fell below one-third only in 2023
This is a specific claim, so it is a **finding** in headline type, even though the claim is factually incorrect because coal is **34%** in 2023, not below one-third.

**Label:** finding

### 2. Share of Solar, Wind and Coal
This only describes what the chart contains. It does not communicate any takeaway.

**Label:** description

### 3. Generation Mix by Source
This is a generic chart title and does not state any data-backed insight.

**Label:** description

### 4. Wind remained the largest renewable source
This is a specific claim supported by the table because wind is greater than solar in 2021, 2022, and 2023.

**Label:** finding

### 5. Solar gained 6 points in two years
This is directly supported by the table because solar rises from 12 to 18, which is a gain of 6 percentage points.

**Label:** finding

### 6. Annual Energy Source Trends
This is a broad descriptive title and does not state any clear finding.

**Label:** description

---

## Step 4 — Rewrite the description headlines as findings

### 2. Share of Solar, Wind and Coal
Rewrite as a finding:
**Wind had the highest share among the listed sources each year, rising from 21% to 25%, while solar also increased steadily**

### 3. Generation Mix by Source
Rewrite as a finding:
**Coal fell from 43% to 34% while both solar and wind increased from 2021 to 2023**

### 6. Annual Energy Source Trends
Rewrite as a finding:
**Coal declined by 9 points while solar rose by 6 points over 2021 to 2023**

---

## Final Submission

```text
1|finding|
2|description|Wind had the highest share among the listed sources each year, rising from 21% to 25%, while solar also increased steadily
3|description|Coal fell from 43% to 34% while both solar and wind increased from 2021 to 2023
4|finding|
5|finding|
6|description|Coal declined by 9 points while solar rose by 6 points over 2021 to 2023
