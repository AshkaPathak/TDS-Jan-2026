# GA3 — Q6: Data Sourcing with Google Dorks (1 Mark)

## Problem Summary

Construct a single Google Dork query that:

1. Restricts results to the domain `worldbank.org`
2. Targets downloadable dataset formats (Excel, CSV, or PDF)
3. Uses precision operators to locate datasets related to World Bank data for Japan
4. Uses multiple Google Dork operators
5. Is at least 40 characters long

---

## Final Google Dork Query

```
site:worldbank.org filetype:xlsx intitle:"Japan" "World Bank data"
```

---

## Operator Breakdown

- `site:worldbank.org`  
  Restricts search results to the official World Bank domain.

- `filetype:xlsx`  
  Targets Excel dataset files (downloadable structured data).

- `intitle:"Japan"`  
  Ensures the word "Japan" appears in the page title for higher relevance.

- `"World Bank data"`  
  Exact phrase matching for precision.

---

## Why This Query Works

- Uses multiple Google Dork operators.
- Restricts to the correct domain.
- Targets structured downloadable datasets.
- Applies keyword precision through title and phrase operators.
- Exceeds the 40-character minimum requirement.

---

## Conclusion

A precise Google Dork query was constructed to reliably surface downloadable datasets related to World Bank data for Japan from the official domain
