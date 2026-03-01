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
      nums.forEach(n => (total += Number(n)));
    });
    return total;
  });
}

async function main() {
  if (URLS.some(u => u.startsWith("PASTE_"))) {
    throw new Error("Replace the placeholder Seed URLs in scrape.js");
  }

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

main().catch(err => {
  console.error("FAILED:", err);
  process.exit(1);
});
