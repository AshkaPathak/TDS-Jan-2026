# GA3 — Q8: Browser Runtime Diagnostics using DevTools Instrumentation

## Problem Summary

A monitoring site simulates real-world frontend behavior across 15 interconnected pages.

The objective was to:

- Open the assigned monitoring URL using browser automation
- Navigate all 15 pages using the provided navigation links
- Capture runtime events inside the browser
- Count ONLY uncaught JavaScript exceptions (not console.error logs)
- Wait for delayed asynchronous failures (~1–3 seconds)
- Generate a strict diagnostic report in key=value format

Assigned URL:

https://sanand0.github.io/tdsdata/cdp_trap/index.html?student=23f3002663%40ds.study.iitm.ac.in

---

## Key Insight

Static HTTP scraping (requests / BeautifulSoup) does NOT execute JavaScript.

Runtime-only failures:
- occur after page load
- are triggered asynchronously
- are not visible in HTML source
- can only be detected inside a real browser

Therefore:
- Use Playwright (Chromium)
- Listen to `pageerror` events
- Wait after each page load
- Traverse pages in deterministic navigation order

Only count:
Uncaught JavaScript exceptions via `page.on("pageerror")`

Do NOT count:
- console.error()
- warnings
- debug logs

---

## Final Diagnostic Output (Submitted to Portal)

```
TOTAL_PAGES_VISITED=15
TOTAL_ERRORS=4
FIRST_ERROR_PAGE=page_1.html
```

---

## Implementation Strategy

1. Launch Chromium using Playwright
2. Visit index.html
3. Extract navigation links
4. Sort pages in natural order (page_1 → page_14)
5. Visit pages sequentially
6. Wait 3.5 seconds to capture async runtime errors
7. Record pages where `pageerror` fires
8. Determine first error page based on visit order

---

## Complete Script (crawl.js)

```js
const { chromium } = require("playwright");

const START_URL =
  "https://sanand0.github.io/tdsdata/cdp_trap/index.html?student=23f3002663%40ds.study.iitm.ac.in";

const WAIT_MS_AFTER_LOAD = 3500;

function pageNumber(name) {
  if (name === "index.html") return 0;
  const match = name.match(/^page_(\d+)\.html$/);
  return match ? parseInt(match[1], 10) : 9999;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const visited = [];
  const errorPages = new Set();
  let currentPageName = null;

  // Count ONLY uncaught JS exceptions
  page.on("pageerror", () => {
    if (currentPageName) {
      errorPages.add(currentPageName);
    }
  });

  // Step 1: Visit index.html
  await page.goto(START_URL, { waitUntil: "domcontentloaded" });
  currentPageName = "index.html";
  visited.push("index.html");
  await page.waitForTimeout(WAIT_MS_AFTER_LOAD);

  // Step 2: Extract navigation links
  const hrefs = await page.$$eval("a", (anchors) =>
    anchors.map((a) => a.getAttribute("href")).filter(Boolean)
  );

  const pageNames = [...new Set(hrefs.map((h) => h.split("?")[0]))]
    .filter((name) => name.endsWith(".html"))
    .sort((a, b) => pageNumber(a) - pageNumber(b));

  // Step 3: Visit pages in sorted order
  for (const name of pageNames) {
    const url = new URL(name, START_URL).toString();
    currentPageName = name;

    await page.goto(url, { waitUntil: "domcontentloaded" });
    visited.push(name);

    // Wait for async runtime errors
    await page.waitForTimeout(WAIT_MS_AFTER_LOAD);
  }

  await browser.close();

  const totalPages = visited.length;
  const totalErrors = errorPages.size;
  const firstErrorPage =
    visited.find((page) => errorPages.has(page)) || "";

  console.log(`TOTAL_PAGES_VISITED=${totalPages}`);
  console.log(`TOTAL_ERRORS=${totalErrors}`);
  console.log(`FIRST_ERROR_PAGE=${firstErrorPage}`);
})();
```

---

## Installation & Run Commands

```bash
npm init -y
npm install playwright
npx playwright install chromium
node crawl.js
```

---

## Final Result

- TOTAL_PAGES_VISITED = 15  
- TOTAL_ERRORS = 4  
- FIRST_ERROR_PAGE = page_1.html  

---

## Conclusion

Using Playwright runtime instrumentation and `page.on("pageerror")`:

- All 15 pages were navigated
- 4 pages contained uncaught JavaScript runtime exceptions
- The first error occurred on page_1.html

Browser automation is mandatory because runtime failures are invisible to static scraping.
