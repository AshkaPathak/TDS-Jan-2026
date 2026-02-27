const { chromium } = require("playwright");

const START_URL =
  "https://sanand0.github.io/tdsdata/cdp_trap/index.html?student=23f3002663%40ds.study.iitm.ac.in";

const WAIT_MS_AFTER_LOAD = 3500;

function pageNumber(name) {
  // index.html => 0, page_1.html => 1, ...
  if (name === "index.html") return 0;
  const m = name.match(/^page_(\d+)\.html$/);
  return m ? parseInt(m[1], 10) : 9999;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const visited = [];
  const errorPages = new Set();
  let currentPageName = null;

  // ONLY uncaught JS exceptions
  page.on("pageerror", () => {
    if (currentPageName) errorPages.add(currentPageName);
  });

  // 1) Load index
  await page.goto(START_URL, { waitUntil: "domcontentloaded" });
  currentPageName = "index.html";
  visited.push("index.html");
  await page.waitForTimeout(WAIT_MS_AFTER_LOAD);

  // 2) Collect links from index
  const hrefs = await page.$$eval("a", (as) =>
    as.map((a) => a.getAttribute("href")).filter(Boolean)
  );

  // 3) Normalize to filenames like page_1.html, page_2.html ...
  const pageNames = [...new Set(hrefs.map((h) => h.split("?")[0]))]
    .filter((n) => n.endsWith(".html"))
    .sort((a, b) => pageNumber(a) - pageNumber(b));

  // 4) Visit in sorted order
  for (const name of pageNames) {
    const url = new URL(name, START_URL).toString();
    currentPageName = name;

    await page.goto(url, { waitUntil: "domcontentloaded" });
    visited.push(name);

    await page.waitForTimeout(WAIT_MS_AFTER_LOAD);
  }

  await browser.close();

  const totalPages = visited.length; // should be 15
  const totalErrors = errorPages.size; // should be 4

  // portal expects first error based on THIS traversal order
  const firstErrorPage = visited.find((p) => errorPages.has(p)) || "";

  console.log(`TOTAL_PAGES_VISITED=${totalPages}`);
  console.log(`TOTAL_ERRORS=${totalErrors}`);
  console.log(`FIRST_ERROR_PAGE=${firstErrorPage}`);
})();
