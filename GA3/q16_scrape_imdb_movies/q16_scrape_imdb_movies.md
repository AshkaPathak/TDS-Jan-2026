# GA3 — Q16: IMDb Low-Rated Movies (2.0–4.0) → JSON (First 25)

## Problem Statement

StreamFlix requires automation to identify movies on IMDb with user ratings between **2 and 4**.

Task:
- Use IMDb Advanced Search
- Filter: Rating 2.0 to 4.0
- Title Type: Feature films only
- Extract first 25 titles
- Output JSON array containing:
  - id
  - title (with ranking prefix)
  - year
  - rating

---

## Search URL Used

```
https://www.imdb.com/search/title/?title_type=feature&user_rating=2.0,4.0&count=25&sort=moviemeter,asc
```

---

## Approach

- Used Playwright to render dynamic IMDb results.
- Handled consent popups automatically.
- Extracted:
  - IMDb ID from title link
  - Title text
  - Year (4-digit extraction)
  - Displayed rating (rounded to 1 decimal)
- Added ranking prefix (`1.`, `2.`, etc.) to match grader format.

---

## Setup

```bash
cd ~/TDS-Jan-2026/GA3/q16_scrape_imdb_movies
npm init -y
npm i playwright
npx playwright install --with-deps chromium
```

---

## Run Script

```bash
node scrape_imdb.js > answer.json
```

---

## Verification

```bash
python3 - <<'PY'
import json
d=json.load(open("answer.json"))
print("Count:", len(d))
print("First:", d[0])
PY
```

Expected:
- Count = 25
- First id = tt30842022

---

## Final Output

The generated `answer.json` was submitted to the portal and validated successfully.

---

## GitHub Steps

```bash
cd ~/TDS-Jan-2026

git add GA3/q16_scrape_imdb_movies/q16_scrape_imdb_movies.md
git add GA3/q16_scrape_imdb_movies/scrape_imdb.js
git add GA3/q16_scrape_imdb_movies/answer.json

git commit -m "GA3 Q16: Scrape IMDb movies rated 2–4 (ranked, formatted JSON output)"
git push
```

---

## Conclusion

Using Playwright ensured reliable scraping of IMDb advanced search results, handling dynamic rendering and formatting the output precisely as required by the grader.
