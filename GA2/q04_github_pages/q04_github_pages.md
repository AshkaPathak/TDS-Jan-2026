# GA2 — Q4: Host Your Portfolio on GitHub Pages

## Problem Summary

The task was to publish a simple portfolio page using **GitHub Pages** and ensure that the IITM email address `23f3002663@ds.study.iitm.ac.in` appears in the page’s HTML source.

Since GitHub Pages is served via Cloudflare (which may obfuscate email addresses), the email must be wrapped using the special comment format:

```
<!--email_off-->23f3002663@ds.study.iitm.ac.in<!--/email_off-->
```

The submission requires a valid `https://` GitHub Pages URL.

---

## Step 1: Create the Portfolio HTML File

Create a folder for Q4:

```bash
mkdir -p GA2/q04_github_pages
```

Create the HTML file:

```bash
nano GA2/q04_github_pages/index.html
```

Add the required content:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>TDS GA2 Q4 - Portfolio</title>
</head>
<body>
  <h1>TDS GA2 — Q4</h1>
  <p>GitHub Pages portfolio page.</p>

  <!--email_off-->23f3002663@ds.study.iitm.ac.in<!--/email_off-->

</body>
</html>
```

---

## Step 2: Prepare `/docs` Folder for GitHub Pages Deployment

GitHub Pages deploys only from the repository root (`/`) or the `/docs` folder.

To keep the GA2 structure clean, copy the file into `/docs`:

```bash
mkdir -p docs
cp GA2/q04_github_pages/index.html docs/index.html
```

---

## Step 3: Commit and Push Changes

```bash
git add GA2/q04_github_pages/index.html docs/index.html
git commit -m "GA2 Q4: add GitHub Pages portfolio with wrapped email"
git push
```

---

## Step 4: Enable GitHub Pages

On GitHub:

1. Open repository → **Settings**
2. Navigate to **Pages**
3. Under *Build and deployment*:
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/docs`
4. Save

GitHub generates the live URL.

---

## Step 5: Verify Email in HTML Source

Open the GitHub Pages URL.

Right click → **View Page Source**

Confirm the exact string appears:

```
23f3002663@ds.study.iitm.ac.in
```

---

## Final Answer (Submitted URL)

```
https://AshkaPathak.github.io/TDS-Jan-2026/
```

