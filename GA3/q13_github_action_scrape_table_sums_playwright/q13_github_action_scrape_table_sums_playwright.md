# GA3 — Q13: Scrape Table Sums with Playwright (GitHub Action)

## Problem Summary

Create a GitHub Action that:

- Uses **Playwright** to visit dynamic table pages for:
  - Seed 32
  - Seed 33
  - Seed 34
  - Seed 35
  - Seed 36
  - Seed 37
  - Seed 38
  - Seed 39
  - Seed 40
  - Seed 41
- Scrapes **all numbers inside all `<table>` elements**
- Computes the total sum
- Prints the final total in GitHub Actions logs
- Includes a workflow step whose name contains:

```
23f3002663@ds.study.iitm.ac.in
```

---

## Final Computed Result

After scraping all 10 seed pages:

```
TOTAL_SUM: 2523310
```

---

## Implementation Overview

### 1. Browser Automation

- Playwright with Chromium (headless)
- Wait for dynamic content using `networkidle`
- Extract all `<table>` inner text
- Use regex to capture numeric values
- Convert to `Number`
- Accumulate into a grand total

---

## Playwright Script

**File:**  
`GA3/q13_github_action_scrape_table_sums_playwright/playwright/scrape.js`

```javascript
import { chromium } from "playwright";

const URLS = [
  "https://sanand0.github.io/tdsdata/js_table/?seed=32",
  "https://sanand0.github.io/tdsdata/js_table/?seed=33",
  "https://sanand0.github.io/tdsdata/js_table/?seed=34",
  "https://sanand0.github.io/tdsdata/js_table/?seed=35",
  "https://sanand0.github.io/tdsdata/js_table/?seed=36",
  "https://sanand0.github.io/tdsdata/js_table/?seed=37",
  "https://sanand0.github.io/tdsdata/js_table/?seed=38",
  "https://sanand0.github.io/tdsdata/js_table/?seed=39",
  "https://sanand0.github.io/tdsdata/js_table/?seed=40",
  "https://sanand0.github.io/tdsdata/js_table/?seed=41"
];

async function sumTables(page) {
  await page.waitForLoadState("networkidle");

  return await page.evaluate(() => {
    let total = 0;
    document.querySelectorAll("table").forEach(table => {
      const text = table.innerText.replace(/,/g, "");
      const nums = text.match(/-?\d+(\.\d+)?/g) || [];
      nums.forEach(n => total += Number(n));
    });
    return total;
  });
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  let grandTotal = 0;

  for (const url of URLS) {
    console.log("Visiting:", url);
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60000 });
    const pageSum = await sumTables(page);
    console.log("Page sum:", pageSum);
    grandTotal += pageSum;
  }

  await browser.close();

  console.log("=================================");
  console.log("TOTAL_SUM:", grandTotal);
  console.log("=================================");
}

main();
```

---

## package.json

**File:**  
`GA3/q13_github_action_scrape_table_sums_playwright/playwright/package.json`

```json
{
  "name": "ga3-q13-playwright",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "dependencies": {
    "playwright": "^1.41.0"
  },
  "scripts": {
    "start": "node scrape.js"
  }
}
```

---

## GitHub Action Workflow

**File:**  
`.github/workflows/ga3_q13_playwright.yml`

```yaml
name: GA3 Q13 Playwright Scraper

on:
  workflow_dispatch:

jobs:
  scrape:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        working-directory: GA3/q13_github_action_scrape_table_sums_playwright/playwright
        run: npm install

      - name: Install Playwright Chromium
        working-directory: GA3/q13_github_action_scrape_table_sums_playwright/playwright
        run: npx playwright install --with-deps chromium

      - name: 23f3002663@ds.study.iitm.ac.in - run scraper
        working-directory: GA3/q13_github_action_scrape_table_sums_playwright/playwright
        run: npm run start
```

---

## Execution in GitHub Actions

Workflow steps:

1. Checkout repository  
2. Setup Node.js  
3. Install dependencies  
4. Install Chromium browser  
5. Run Playwright scraper  
6. Print total sum in logs  

Successful run prints:

```
TOTAL_SUM: 2523310
```

---

## Final Answer

```
2523310
```

---

## Status

✔ Workflow placed in root `.github/workflows`  
✔ Correct working directory configured  
✔ Playwright installed in CI  
✔ Email present in step name  
✔ Workflow executed successfully (green status)  
✔ Total sum correctly computed  
