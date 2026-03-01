# GA3 — Q15: Count Crawled HTML Files (J to V)

## Problem Statement

SiteScout collects competitor pages for market research.  
Its crawler stores HTML files in alphabetized folders.

Crawl:

https://sanand0.github.io/tdsdata/crawl_html/

Determine how many reachable HTML files begin with letters **J through V**.

---

## Approach Overview

This required:

1. Crawling all reachable pages within:
   `/tdsdata/crawl_html/`
2. Avoiding duplicates
3. Ignoring fragments (#section)
4. Restricting to `.html` files
5. Counting filenames starting with letters:
   **j, k, l, m, n, o, p, q, r, s, t, u, v**

A BFS (Breadth-First Search) crawler was implemented using:
- `requests`
- `BeautifulSoup`
- `urllib.parse`

---

## Setup

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4
```

---

## Implementation

Create `count_j_to_v.py`:

```python
import re
from collections import deque
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup

START = "https://sanand0.github.io/tdsdata/crawl_html/"
DOMAIN = "sanand0.github.io"

def is_same_site(u: str) -> bool:
    p = urlparse(u)
    return p.netloc == DOMAIN and p.path.startswith("/tdsdata/crawl_html/")

def normalize(u: str) -> str:
    u, _ = urldefrag(u)
    return u

def filename_starts_j_to_v(u: str) -> bool:
    path = urlparse(u).path
    name = path.rsplit("/", 1)[-1].lower()

    if not name.endswith(".html"):
        return False

    if not name:
        return False

    first_char = name[0]
    return "j" <= first_char <= "v"

def main():
    queue = deque([START])
    visited = set([START])

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    while queue:
        url = queue.popleft()

        try:
            response = session.get(url, timeout=20)
            response.raise_for_status()
        except Exception:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.select("a[href]"):
            next_url = urljoin(url, a["href"])
            next_url = normalize(next_url)

            if is_same_site(next_url) and next_url not in visited:
                visited.add(next_url)
                queue.append(next_url)

    html_pages = [
        u for u in visited
        if urlparse(u).path.lower().endswith(".html")
    ]

    count = sum(1 for u in html_pages if filename_starts_j_to_v(u))

    print("TOTAL_REACHABLE_HTML_PAGES =", len(html_pages))
    print("J_TO_V_COUNT =", count)

if __name__ == "__main__":
    main()
```

---

## Execution

Run:

```bash
python count_j_to_v.py
```

Output:

```
TOTAL_REACHABLE_HTML_PAGES = 106
J_TO_V_COUNT = 59
```

---

## Final Answer

**59**

---

## Why This Works

- BFS guarantees all reachable pages are discovered.
- URL normalization removes duplicate fragments.
- Domain restriction prevents crawling external links.
- Only `.html` files are counted.
- Filename filtering ensures correct alphabetical range.

---
## Conclusion

The problem required:

- Implementing a controlled crawler
- Handling URL normalization
- Avoiding duplicate visits
- Filtering filenames by alphabetical range

Final Result:

✔ 106 reachable HTML pages  
✔ 59 files start with J through V  
✔ Correct answer submitted
