import re
import sys
from collections import deque
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup

START = "https://sanand0.github.io/tdsdata/crawl_html/"
DOMAIN = "sanand0.github.io"

def is_same_site(u: str) -> bool:
    try:
        p = urlparse(u)
        return p.netloc == DOMAIN and p.path.startswith("/tdsdata/crawl_html/")
    except Exception:
        return False

def normalize(u: str) -> str:
    u, _ = urldefrag(u)  # remove #fragment
    return u

def filename_starts_j_to_v(u: str) -> bool:
    path = urlparse(u).path
    name = path.rsplit("/", 1)[-1].lower()
    if not name.endswith(".html"):
        return False
    if not name:
        return False
    c = name[0]
    return "j" <= c <= "v"

def main():
    q = deque([START])
    seen = set([START])

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    while q:
        url = q.popleft()
        try:
            r = session.get(url, timeout=20)
            r.raise_for_status()
        except Exception:
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select("a[href]"):
            nxt = urljoin(url, a["href"])
            nxt = normalize(nxt)
            if is_same_site(nxt) and nxt not in seen:
                seen.add(nxt)
                q.append(nxt)

    # count pages (only .html)
    html_pages = [u for u in seen if urlparse(u).path.lower().endswith(".html")]
    count = sum(1 for u in html_pages if filename_starts_j_to_v(u))

    print("TOTAL_REACHABLE_HTML_PAGES =", len(html_pages))
    print("J_TO_V_COUNT =", count)

if __name__ == "__main__":
    main()

