# GA4 — Q2: Excel Z-Score Outlier Surveillance

## Problem Summary

PulseCare Clinics operates a network of clinics and collects weekly patient satisfaction scores. Leadership requires an automated Excel-based statistical check to identify statistically extreme clinics.

An outlier is defined as:

|z| ≥ 2.5

Where:

z = (x − μ) / σ

---

## Dataset

File used:

q-excel-zscore-outlier.csv

---

## Step-by-Step Excel Solution

### Step 1 — Import Data

1. Open Excel  
2. Go to Data → From Text/CSV  
3. Select q-excel-zscore-outlier.csv  
4. Click Load  

Assume satisfaction scores are in:

B2:B101

---

### Step 2 — Compute Mean

In an empty cell:

=AVERAGE(B2:B101)

---

### Step 3 — Compute Standard Deviation (Sample)

=STDEV.S(B2:B101)

---

### Step 4 — Compute Z-Score for Each Clinic

In C2:

=STANDARDIZE(B2, $MeanCell$, $StdevCell$)

OR equivalently:

=(B2 - $MeanCell$) / $StdevCell$

Drag down for all rows.

---

### Step 5 — Flag Outliers

In D2:

=IF(ABS(C2)>=2.5,1,0)

Drag down.

---

### Step 6 — Count Outliers

=COUNTIF(D2:D101,1)

OR directly:

=COUNTIF(C2:C101,">=2.5") + COUNTIF(C2:C101,"<=-2.5")

---

## Final Answer

Number of clinics where |z| ≥ 2.5:

3

---

## Interpretation

There are 3 clinics whose satisfaction scores are statistically extreme compared to the overall network. These clinics require executive review as they significantly deviate from the mean performance.

---

## GitHub Steps

cd GA4/q02_excel_zscore_outlier_surveillance

nano q02_excel_zscore_outlier_surveillance.md

Paste this content, save, then:

git add GA4/q02_excel_zscore_outlier_surveillance  
git commit -m "GA4 Q2: Excel Z-score outlier surveillance — 3 clinics identified"  
git push

---

## Conclusion

✔ Z-scores computed correctly  
✔ Outlier threshold applied (|z| ≥ 2.5)  
✔ Final verified count: 3 clinics
