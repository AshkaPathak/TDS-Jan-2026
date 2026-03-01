const { chromium } = require("playwright");

function extractNumbersFromText(s) {
  // captures integers, negatives too. (If decimals exist, change regex to /-?\d+(\.\d+)?/g)
  const matches = s.match(/-?\d+/g);
  if (!matches) return [];
  return matches.map(Number);
}

async function sumNumbersOnPage(page, url) {
  await page.goto(url, { waitUntil: "domcontentloaded" });

  // grab text from ALL tables (covers multiple tables, nested tables)
  const tableTexts = await page.$$eval("table", tables =>
    tables.map(t => t.innerText || t.textContent || "")
  );

  let sum = 0;
  for (const txt of tableTexts) {
    const nums = txt.match(/-?\d+/g);
    if (nums) sum += nums.map(Number).reduce((a, b) => a + b, 0);
  }
  return sum;
}

(async () => {
  // ✅ IMPORTANT: paste the exact seed URLs from the portal (copy link address)
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
    "https://sanand0.github.io/tdsdata/js_table/?seed=67",
  ];

  if (seedUrls.length !== 10) {
    console.error("Put exactly 10 seed URLs (58 to 67) in seedUrls[]");
    process.exit(1);
  }

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  let grandTotal = 0;

  for (const url of seedUrls) {
    const s = await sumNumbersOnPage(page, url);
    console.log(url, "=>", s);
    grandTotal += s;
  }

  await browser.close();

  console.log("\nGRAND_TOTAL =", grandTotal);
})();
