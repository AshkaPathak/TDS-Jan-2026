# GA2 — Q5: Host a JSON Data API on GitHub Pages

## Problem Summary

The task was to host a static JSON file on **GitHub Pages** that behaves like a simple JSON API for a product catalog.

The JSON file must include:

- A `metadata` object at the root
- Exactly 24 products
- Pre-computed `aggregations` for each category
- Correct `inventoryValue` computed as (price × stock)
- Hosted via a valid `https://` GitHub Pages URL

---

## Step 1: Create Deployable JSON File

GitHub Pages can serve static files from `/` or `/docs`.

To maintain repository structure and allow deployment, the JSON file was created at:

```
docs/api/catalog.json
```

Commands used:

```bash
mkdir -p docs/api
nano docs/api/catalog.json
```

---

## Step 2: Add Required JSON Structure

The root JSON structure:

```json
{
  "metadata": {
    "email": "23f3002663@ds.study.iitm.ac.in",
    "version": "62ef635e"
  },
  "products": [...24 products...],
  "aggregations": {...}
}
```

### Aggregation Rules

For each category:

- `count` = number of products in that category
- `inventoryValue` = sum(price × stock)

Final computed values:

| Category     | Count | inventoryValue |
|-------------|-------|----------------|
| electronics | 5     | 185369.03999999998 |
| clothing    | 7     | 157491.99000000002 |
| books       | 4     | 100375.22 |
| sports      | 6     | 230648.83000000002 |
| home        | 2     | 43246.89 |

These values were computed directly from the provided product dataset without rounding, matching the grader’s floating-point precision.

---

## Step 3: Commit and Push

```bash
git add docs/api/catalog.json
git commit -m "GA2 Q5: add static JSON API with correct aggregations"
git push
```

---

## Step 4: GitHub Pages Deployment

GitHub Pages is configured to deploy from:

- Branch: `main`
- Folder: `/docs`

Because the file is located at:

```
docs/api/catalog.json
```

It is served at:

```
https://AshkaPathak.github.io/TDS-Jan-2026/api/catalog.json
```

If CDN caching delays updates, use a cache buster:

```
https://AshkaPathak.github.io/TDS-Jan-2026/api/catalog.json?v=4
```

---

## Final Submitted URL

```
https://AshkaPathak.github.io/TDS-Jan-2026/api/catalog.json
```

