# GA3 — Q10: AI Expense Tracker (Multi-Page PDF) — Total for 9 January

## Problem Summary
Given a multi-page PDF containing expense records in mixed date formats (e.g., 9Jan, 09January, Jan 9, January 9, 9JAN, JAN9) and amounts in Rupees and Dollars, compute the total expenses for 9th January. All pages must be included. All date format variants for 9 January must be matched. Dollar amounts must be converted using 1 Dollar = 80 Rupees. Final output must be the total in Rupees.

## Issue Faced
The Gemini API approach failed due to quota limitations (RESOURCE_EXHAUSTED, free-tier quota = 0). Therefore, a deterministic local parsing approach was implemented using pdfplumber.

Initial local attempts overcounted because multiple dates and amounts appeared on the same line. The fix was to:
1. Detect every January date occurrence in a line.
2. When a 9 January token is found, extract only the text segment AFTER that date and BEFORE the next date.
3. Extract the first money value inside that segment.
4. Convert USD to INR.
5. Sum across all pages.

## Installation
cd ~/TDS-Jan-2026/GA3/q10_ai_expense_tracker_multi_page_pdf_analysis
python3 -m venv .venv
source .venv/bin/activate
pip install pdfplumber

## Final Solver Script (local_sum_v3.py)
import re
import sys
import pdfplumber

USD_TO_INR = 80

DATE_ANY_RE = re.compile(
    r"(?i)\b("
    r"(?P<d1>\d{1,2})\s*Jan(?:uary)?|"
    r"Jan(?:uary)?\s*(?P<d2>\d{1,2})|"
    r"(?P<d3>\d{1,2})\s*JAN\b|"
    r"JAN\s*(?P<d4>\d{1,2})\b"
    r")\b"
)

MONEY_RE = re.compile(
    r"(?P<cur>Rs|INR|Rupees|\$|USD|Dollar|Dollars)\s*"
    r"(?P<amt>\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"|(?P<amt2>\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)\s*"
    r"(?P<cur2>Rs|INR|Rupees|USD|Dollar|Dollars)\b",
    re.IGNORECASE,
)

def to_float(s: str) -> float:
    return float(s.replace(",", ""))

def to_inr(amount: float, currency: str) -> float:
    c = currency.strip().lower()
    if c in ["$", "usd", "dollar", "dollars"]:
        return amount * USD_TO_INR
    return amount

def extract_day(m: re.Match) -> int:
    for g in ("d1", "d2", "d3", "d4"):
        v = m.group(g)
        if v:
            return int(v)
    return -1

def first_money_in_segment(seg: str):
    for m in MONEY_RE.finditer(seg):
        cur = m.group("cur") or m.group("cur2")
        amt = m.group("amt") or m.group("amt2")
        if cur and amt:
            return cur, amt
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python local_sum_v3.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    total = 0.0
    used = 0
    no_amount_after_9jan = 0

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            for line in text.splitlines():
                dates = []
                for dm in DATE_ANY_RE.finditer(line):
                    day = extract_day(dm)
                    if day != -1:
                        dates.append((dm.start(), dm.end(), day))

                if not dates:
                    continue

                for idx, (s, e, day) in enumerate(dates):
                    if day != 9:
                        continue

                    next_start = dates[idx + 1][0] if idx + 1 < len(dates) else len(line)
                    segment = line[e:next_start]

                    money = first_money_in_segment(segment)
                    if not money:
                        no_amount_after_9jan += 1
                        continue

                    cur, amt = money
                    total += to_inr(to_float(amt), cur)
                    used += 1

    print("USED_9JAN_ENTRIES:", used)
    print("NO_AMOUNT_AFTER_9JAN:", no_amount_after_9jan)
    print(f"TOTAL_RUPEES_FOR_JAN_9: {total:.2f}")

if __name__ == "__main__":
    main()

## Run Command
python local_sum_v3.py expenses_23f3002663.pdf

## Output
USED_9JAN_ENTRIES: 18
NO_AMOUNT_AFTER_9JAN: 0
TOTAL_RUPEES_FOR_JAN_9: 483598.00

## Final Answer Submitted
483598
