# GA7 — Q2: Chartjunk Removal and Data-Ink Ratio Repair

## Problem Summary
The given bar chart contains multiple decorative and redundant elements (chartjunk) that obscure the data and reduce clarity.  
The goal is to remove unnecessary visual elements and improve the **data-ink ratio**, ensuring that only meaningful information remains.

---

## Chartjunk Identification

### Ink Waste (IW)
- Drop shadows (`shadowBlur`, `shadowColor`)
- Thick borders (`borderWidth: 5`)
- Semi-transparent fills (`rgba(...)`)

These elements add visual clutter without conveying additional data.

---

### Redundant Encoding (RE)
- Legend (only one dataset, so redundant)
- Subtitle (repeats information already visible)
- Datalabels plugin (duplicates values already represented by bar heights)

---

### Noise Gridlines (NG)
- X-axis gridlines
- Y-axis gridlines

Gridlines are excessive and distract from the bars.

---

### Tick Density (TD)
- Unnecessary tick configurations (`autoSkip`, extra ticks)

These add noise without improving readability.

---

## Fix Applied

To improve the data-ink ratio:

- Removed all shadows and decorative effects  
- Simplified bar styling (solid fill, minimal border)  
- Disabled legend, subtitle, and datalabels  
- Removed all gridlines  
- Simplified tick configuration  

This ensures that only the **data itself remains the focus**.

---

## Corrected HTML

```html
<!--
Chartjunk Removed:

Ink Waste (IW):
- Removed shadowBlur and shadowColor (drop shadows)
- Removed thick border (borderWidth reduced)
- Removed semi-transparent fill (used solid color)

Redundant Encoding (RE):
- Removed legend (single dataset, unnecessary)
- Removed subtitle (redundant text)
- Removed datalabels (duplicates information already shown by bar height)

Noise Gridlines (NG):
- Removed x-axis gridlines
- Removed y-axis gridlines

Tick Density (TD):
- Removed unnecessary tick configuration

These changes improve the data-ink ratio by removing non-data elements and focusing only on the signal.
-->

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Chart Measurement 4</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
</head>
<body>

<h2>Chart Measurement 4</h2>
<p>A bar chart showing temporal measurements.</p>

<canvas id="chart"></canvas>

<script>
new Chart(document.getElementById('chart'), {
  type: 'bar',
  data: {
    labels: ["January","February","March","April","May","June","July"],
    datasets: [{
      label: 'Dataset 1',
      data: [65,59,80,81,56,55,40],
      backgroundColor: "#f28ea8",
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: false },
      subtitle: { display: false },
      datalabels: { display: false }
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { display: true }
      },
      y: {
        grid: { display: false },
        ticks: { display: true }
      }
    }
  }
});
</script>

</body>
</html>
```

---

## Conclusion
By removing chartjunk across all categories (Ink Waste, Redundant Encoding, Noise Gridlines, Tick Density), the chart now clearly emphasizes the data.  
The improved design maximizes the **data-ink ratio**, making the visualization cleaner, more readable, and more effective.

