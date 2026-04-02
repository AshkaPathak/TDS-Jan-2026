# GA7 — Q1: Fix the Color Encoding Mismatch

## Problem Summary
The chart displays Net Promoter Score (NPS) by region, with values ranging from **-45 to +72**.  
However, it uses an incorrect color encoding that misrepresents the data.

---

## Key Observation
- The data includes both **negative and positive values**
- There is a **meaningful midpoint at 0**
- This means the data is **not purely sequential**
- Instead, it requires a scheme that distinguishes direction relative to zero

---

## Mismatch Explanation
The current one-directional color ramp makes negative NPS scores appear as low-positive satisfaction rather than net-detractor regions. It incorrectly treats the data as a single increasing sequence, hiding the critical distinction between negative and positive values.

---

## Correct Color Scheme
**Diverging**

### Why?
- The dataset has a **natural midpoint (0)**
- Values diverge in two directions:
  - Negative → detractors
  - Positive → promoters
- A diverging palette clearly separates these two sides

---

## Fix Applied
Replaced the incorrect categorical/sequential palette with a **red–white–green diverging palette**:

- Red → negative values (detractors)
- White → neutral midpoint (0)
- Green → positive values (promoters)

### Final Color Palette
```js
["#d73027","#f46d43","#fdae61","#ffffff","#a6d96a","#66bd63","#1a9850"]
```

---

## Corrected HTML
```html
<!--
Mismatch:
The current one-directional color ramp makes negative NPS scores appear as low-positive satisfaction rather than net-detractor regions. It incorrectly treats the data as a single increasing sequence, hiding the critical distinction between negative and positive values.

Correct scheme:
Diverging — because the data has a meaningful midpoint at 0 with negative and positive directions.

Fix:
Applied a red–white–green diverging palette where:
- red = negative (detractors)
- white = neutral (0)
- green = positive (promoters)
-->

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Net Promoter Score by Region</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
</head>
<body>

<h2>Net Promoter Score by Region</h2>
<p>Net Promoter Score (NPS) by region, ranging from -45 to +72</p>

<canvas id="chart"></canvas>

<script>
const colors = ["#d73027","#f46d43","#fdae61","#ffffff","#a6d96a","#66bd63","#1a9850"];

new Chart(document.getElementById('chart'), {
  type: 'bar',
  data: {
    labels: ["North","South","East","West","Central","Urban","Rural"],
    datasets: [{
      label: 'Net Promoter Score by Region',
      data: [-45,-20,-5,12,30,50,72],
      backgroundColor: colors,
      borderColor: colors,
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: { y: { beginAtZero: false } }
  }
});
</script>

</body>
</html>
```

---

## Conclusion
The issue was not with the data but with the encoding.  
Using a **diverging color scheme** correctly represents the semantic meaning of NPS values, clearly separating negative and positive regions and preventing misinterpretation.

