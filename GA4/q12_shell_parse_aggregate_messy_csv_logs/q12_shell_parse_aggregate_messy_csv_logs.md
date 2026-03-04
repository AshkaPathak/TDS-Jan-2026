# GA4 — Q12: Shell Parse and Aggregate Messy CSV Transaction Logs

## Problem Summary
We are given a messy transaction log CSV file with inconsistent formatting. The dataset contains mixed separators (`|` and `,`), extra whitespace, missing category fields, and possibly additional junk columns. The task is to clean this dataset using shell tools and compute the total transaction amount for each category.

The final output must follow this exact format:

Category:Amount|Category:Amount|...

Requirements:
- Ignore rows with missing category data
- Handle mixed separators (`|` and `,`)
- Remove extra whitespace
- Aggregate total transaction amount per category
- Sort categories alphabetically
- Ensure amounts are printed with exactly **2 decimal places**
- No scientific notation
- Final output must be a single line separated by `|`

---

## Input File
transactions_23f3002663@ds.study.iitm.ac.in.csv

---

## Strategy
To solve the problem using shell utilities:

1. Convert mixed separators (`|`) into commas so the file becomes consistent.
2. Use `awk` to parse the CSV fields.
3. Trim leading and trailing whitespace from category and amount fields.
4. Filter out rows where category or amount is missing.
5. Aggregate the transaction amounts for each category.
6. Format the totals with exactly two decimal places.
7. Sort categories alphabetically.
8. Join the results into a single `|` separated line.

---

## Shell Pipeline Solution

Run the following command in the directory containing the CSV file:

```bash
cat "transactions_23f3002663@ds.study.iitm.ac.in.csv" \
| tr '|' ',' \
| awk -F',' '
{
    gsub(/^[ \t]+|[ \t]+$/, "", $2)
    gsub(/^[ \t]+|[ \t]+$/, "", $3)

    if ($2 == "" || $3 == "") next

    sum[$2] += ($3 + 0)
}
END {
    for (c in sum) {
        printf "%s:%.2f\n", c, sum[c]
    }
}
' \
| LC_ALL=C sort \
| paste -sd'|' -
```

---

## Final Output

Beauty:2609561.80|Books:2576221.38|Clothing:2623633.99|Electronics:2590831.99|Furniture:2566334.66|Groceries:2640232.66|Sports:2616898.77|Toys:2646608.50

This output satisfies all requirements:
- Categories sorted alphabetically
- Exactly two decimal places
- No scientific notation
- Pipe-separated single line

---
