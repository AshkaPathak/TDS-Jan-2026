// scrape_imdb.js
// GA3 Q16 — IMDb movies rated 2.0–4.0 (first 25)
// Output matches grader format exactly:
// - Rank prefix in title (e.g., "1. The Dreadful")
// - Rating rounded to 1 decimal
// - Year extracted as 4-digit number

const { chromium } = require("playwright");

function extractYear(text) {
  const m = String(text || "").match(/(19\d{2}|20\d{2})/);
  return m ? m[1] : "";
}

function normalizeRating(raw) {
  const s = String(raw || "").trim();
  const m = s.match(/(\d+\.\d)/);
  if (m) return m[1];
  const n = Number(s);
  if (!Number.isNaN(n)) return (Math.round(n * 10) / 10).toFixed(1);
  return s;
}

async function tryClickConsent(page) {
  const selectors = [
    "button#onetrust-accept-btn-handler",
    'button:has-text("Accept all")',
    'button:has-text("Accept")',
    'button:has-text("I Agree")',
    'button:has-text("Agree")',
  ];
  for (const sel of selectors) {
    const btn = page.locator(sel).first();
    if (await btn.count()) {
      try {
        await btn.click({ timeout: 1500 });
        return;
      } catch {}
    }
  }
}

(async () => {
  const url =
    "https://www.imdb.com/search/title/?" +
    "title_type=feature&" +
    "user_rating=2.0,4.0&" +
    "count=25&" +
    "sort=moviemeter,asc";

  const browser = await chromium.launch({ headless: true });

  const context = await browser.newContext({
    locale: "en-US",
    extraHTTPHeaders: { "Accept-Language": "en-US,en;q=0.9" },
  });

  const page = await context.newPage();
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 90000 });

  await tryClickConsent(page);
  await page.waitForTimeout(1000);
  await tryClickConsent(page);

  await page.waitForSelector(".lister-item.mode-advanced", {
    timeout: 90000,
  });

  const results = await page.evaluate(() => {
    function getId(href) {
      const m = (href || "").match(/\/title\/(tt\d+)\//);
      return m ? m[1] : "";
    }

    const items = Array.from(
      document.querySelectorAll(".lister-item.mode-advanced")
    ).slice(0, 25);

    return items.map((item, index) => {
      const a = item.querySelector("h3.lister-item-header a");
      const href = a?.getAttribute("href") || "";
      const id = getId(href);
      const rawTitle = (a?.textContent || "").trim();

      const yearText =
        (item.querySelector("h3.lister-item-header .lister-item-year")
          ?.textContent || "").trim();

      const ratingStrong = item.querySelector(
        ".inline-block.ratings-imdb-rating strong"
      );
      const rating =
        (ratingStrong?.textContent || "").trim() ||
        (item
          .querySelector(".inline-block.ratings-imdb-rating")
          ?.getAttribute("data-value") || "").trim();

      return {
        id,
        title: `${index + 1}. ${rawTitle}`,
        yearText,
        rating,
      };
    });
  });

  const final = results.map((x) => ({
    id: x.id,
    title: x.title,
    year: extractYear(x.yearText),
    rating: normalizeRating(x.rating),
  }));

  console.log(JSON.stringify(final, null, 2));

  await browser.close();
})();
