# GA4 — Q10: Google Sheets AI Formula to Extract Zip Codes from Noisy Addresses

## Problem Summary

This task demonstrates how the Google Sheets **AI formula (`=AI()`)** can be used to extract structured data from messy, real-world text.

We are given a dataset of **100 addresses** containing inconsistent formats. Some addresses include valid ZIP codes while others do not.

The objective is to extract the **ZIP code (postal code)** from each address.

If an address does not contain a ZIP code, the result should return **"N/A"**.

---

## Dataset

File used:

addresses_23f3002663@ds.study.iitm.ac.in.csv

The dataset contains 100 rows of addresses with inconsistent formatting.

---

## Method Used

### Step 1 — Import the dataset

The CSV file was imported into **Google Sheets**.

Column structure:

| Column | Description |
|------|-------------|
| A | Address |
| B | Extracted ZIP Code |

---

### Step 2 — Apply the AI extraction formula

In **cell B2** the following AI formula was used:

```excel
=AI("Extract the zip code (or postal code) from this address. If none exists, return N/A: " & A2)
```

The formula was then **filled down to B101** to process all 100 addresses.

---

### Step 3 — Concatenate the results

To produce the final output required by the assignment, the extracted ZIP codes were concatenated using:

```excel
=TEXTJOIN(",", TRUE, B2:B101)
```

This combines all ZIP code results into a **single comma-separated string**.

---

## Final Result

```
N/A,75001,10002,28202,N/A,90210,33101,43085,19101,19101,N/A,30302,N/A,33102,75001,N/A,N/A,43085,N/A,62704,33101,N/A,N/A,28203,28203,N/A,19101,62704,N/A,N/A,30301,19102,N/A,43086,33102,90210,48202,N/A,48202,30302,62704,33101,N/A,48201,90210,77001,30301,19102,30302,10001,N/A,94105,33102,19101,19102,N/A,33101,10001,19102,62704,10001,77001,N/A,N/A,33102,48202,48201,30301,N/A,60601,19102,33101,N/A,48201,28202,43085,94105,43086,10001,75001,N/A,N/A,28203,28203,33101,90210,N/A,33101,19102,30301,48202,48202,43086,48202,48201,94105,N/A,10002,43086,90210
```
---

## Conclusion

Using the **Google Sheets AI formula**, ZIP codes were successfully extracted from messy address strings and consolidated into a single comma-separated result for submission.
