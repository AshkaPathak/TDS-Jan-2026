# GA1 — Q22: Hidden HTML Trick Question

## Problem Summary
The visible question asked:

"How many continents are there?"

Submitting the obvious answer (7) was marked incorrect.

The platform indicated this was a trick question and suggested investigating further.

---

## Issue Identified
The displayed question was not the real question.

The hint stated:
"Sometimes the real question isn't what it appears to be."

This implies hidden content in the HTML.

---

## Investigation Strategy
1. Open Developer Tools.
2. Inspect the DOM.
3. Search for hidden elements (`display: none`).
4. Look for comments or concealed text.

Inside a hidden `<div style="display: none;">`, the actual question was found.

---

## Real Question (Hidden in HTML)
"In Python, what symbol is used to represent a comment?"

---

## Final Answer
#

## Result
PASS