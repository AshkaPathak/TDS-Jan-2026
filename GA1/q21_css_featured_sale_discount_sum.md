# GA1 — Q21: CSS Featured-Sale Discount Sum

## Problem Summary
The task was to calculate the total `data-discount` percentage for all products that are tagged with both `featured` and `sale` classes using a single CSS selector.

Each product is represented as an `<li>` element with:
- Promotional classes (e.g., `featured`, `sale`)
- A `data-discount` attribute containing the discount percentage

We must:
- Target elements that contain BOTH classes
- Use one CSS selector
- Sum their `data-discount` values

---

## Key Concept
In CSS, when an element has multiple classes, they can be targeted together using:

.featured.sale

This selector matches elements that simultaneously have:
- `featured`
- `sale`

It does NOT match elements with only one of the two classes.

---

## Console Approach
Using the browser console:

1. Select matching elements:
   document.querySelectorAll(".featured.sale")

2. Extract the `data-discount` values

3. Convert them to numbers

4. Compute the total sum

---

## Working Console Code
```js
const total = [...document.querySelectorAll(".featured.sale")]
  .reduce((sum, el) => sum + Number(el.dataset.discount), 0);

total;
```

## Final answer
174

## Result
PASS