# GA3 — Q14: Sum Table Values with Playwright

## Problem Statement

DataDash validates generated reports by sampling numeric tables.  
QA engineers scrape several tables and verify aggregated metrics.

Visit each seed link (58 to 67), compute the sum of all numbers in all tables, and enter the total.

---

## Approach Overview

The pages dynamically render numeric tables using JavaScript.  
Therefore:

- Simple HTTP requests are insufficient.
- A headless browser is required.
- Playwright was used to render and scrape tables.

Steps:
1. Launch Chromium in headless mode.
2. Visit each seed URL.
3. Extract all text inside `<table>` elements.
4. Extract all integers using regex.
5. Sum numbers per page.
6. Accumulate grand total across all seeds.

---

## Setup

### 1. Initialize Playwright Project

```bash
mkdir -p playwright
cd playwright
npm init -y
npm i playwright
npx playwright install --with-deps chromium
```

---

## Scraper Implementation

Create `scrape.js`:

```javascript
const { chromium } = require("playwright");

async function sumNumbersOnPage(page, url) {
  await page.goto(url, { waitUntil: "domcontentloaded" });

  const tableTexts = await page.$$eval("table", tables =>
    tables.map(t => t.innerText || "")
  );

  let sum = 0;

  for (const text of tableTexts) {
    const numbers = text.match(/-?\d+/g);
    if (numbers) {
      sum += numbers.map(Number).reduce((a, b) => a + b, 0);
    }
  }

  return sum;
}

(async () => {
  const seedUrls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=58",
    "https://sanand0.github.io/tdsdata/js_table/?seed=59",
    "https://sanand0.github.io/tdsdata/js_table/?seed=60",
    "https://sanand0.github.io/tdsdata/js_table/?seed=61",
    "https://sanand0.github.io/tdsdata/js_table/?seed=62",
    "https://sanand0.github.io/tdsdata/js_table/?seed=63",
    "https://sanand0.github.io/tdsdata/js_table/?seed=64",
    "https://sanand0.github.io/tdsdata/js_table/?seed=65",
    "https://sanand0.github.io/tdsdata/js_table/?seed=66",
    "https://sanand0.github.io/tdsdata/js_table/?seed=67"
  ];

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  let grandTotal = 0;

  for (const url of seedUrls) {
    const pageSum = await sumNumbersOnPage(page, url);
    console.log(url, "=>", pageSum);
    grandTotal += pageSum;
  }

  await browser.close();

  console.log("\nGRAND_TOTAL =", grandTotal);
})();
```

---

## Execution

Run:

```bash
node scrape.js
```

Output:

```
https://sanand0.github.io/tdsdata/js_table/?seed=58 => 257770
https://sanand0.github.io/tdsdata/js_table/?seed=59 => 245522
https://sanand0.github.io/tdsdata/js_table/?seed=60 => 251786
https://sanand0.github.io/tdsdata/js_table/?seed=61 => 243147
https://sanand0.github.io/tdsdata/js_table/?seed=62 => 248922
https://sanand0.github.io/tdsdata/js_table/?seed=63 => 241221
https://sanand0.github.io/tdsdata/js_table/?seed=64 => 243716
https://sanand0.github.io/tdsdata/js_table/?seed=65 => 261372
https://sanand0.github.io/tdsdata/js_table/?seed=66 => 249556
https://sanand0.github.io/tdsdata/js_table/?seed=67 => 239174

GRAND_TOTAL = 2482186
```

---

## Final Answer

**2482186**

---

## Why Playwright Was Required

The tables were generated dynamically using JavaScript.

Playwright:
- Executes page JavaScript
- Waits for DOM rendering
- Allows querying rendered elements
- Ensures accurate scraping of dynamic content

A simple HTTP-based scraper would not have worked.

---

## GitHub Submission Steps

From repository root:

```bash
git add GA3/q14_sum_table_values_playwright
git commit -m "GA3 Q14: Sum table values using Playwright (Grand total = 2482186)"
git push
```

---

## Conclusion

The problem required:
- Understanding dynamic page rendering
- Using a headless browser
- Extracting numeric values via regex
- Aggregating results across multiple pages

Final Result:

✔ Dynamic scraping handled  
✔ All seeds processed  
✔ Correct grand total computed  
✔ Submitted successfully
