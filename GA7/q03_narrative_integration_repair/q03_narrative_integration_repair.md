# GA7 — Q3: Narrative Integration Repair

## Problem Summary
The chart correctly shows queue length over time but lacks a clear narrative.  
It presents the topic (“Queue Length by Hour”) instead of the **key finding**, forcing the viewer to interpret the conclusion themselves.

---

## Key Finding
A sharp spike occurs at **11:00**, where queue length jumps significantly compared to earlier hours.

---

## Repaired Narrative

### Finding Headline
**queues break at 11:00**

This directly states the conclusion instead of describing the chart.

---

### Annotation Added
- **xValue:** "11:00"  
- **yValue:** 21  

A point annotation is added at the peak to highlight the most important data point.

---

### Caption (with implication keyword)
**The 11:00 spike indicates a bottleneck that should be investigated with staffing or process changes.**

- Includes required keyword: **bottleneck**
- Clearly states the operational implication

---

## Corrected HTML

```html
<!--
Finding:
queues break at 11:00

Annotation:
Marked the peak at 11:00 with value 21.

Caption:
The 11:00 spike indicates a bottleneck that should be investigated with staffing or process changes.
-->

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Queue Length</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.0.1/dist/chartjs-plugin-annotation.min.js"></script>
<style>
  body { font-family: Georgia, serif; margin: 20px; }
  .wrap { max-width: 760px; margin: 0 auto; }
  canvas { width: 100%; max-height: 340px; }
  .caption { margin-top: 12px; font-size: 0.95rem; color: #6b7280; }
</style>
</head>
<body>

<div class="wrap">
  <canvas id="chart"></canvas>
  <p class="caption">The 11:00 spike indicates a bottleneck that should be investigated with staffing or process changes.</p>
</div>

<script>
const annotationPlugin = window['chartjs-plugin-annotation'] || window.ChartAnnotation;
if (annotationPlugin) Chart.register(annotationPlugin);

new Chart(document.getElementById('chart'), {
  type: 'line',
  data: {
    labels: ["08:00","09:00","10:00","11:00","12:00","13:00"],
    datasets: [{
      label: "Queue Length",
      data: [7,8,9,21,20,18],
      borderColor: '#2563eb',
      backgroundColor: 'rgba(37, 99, 235, 0.15)',
      borderWidth: 2,
      tension: 0.25,
      fill: false
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      title: {
        display: true,
        text: "queues break at 11:00"
      },
      annotation: {
        annotations: {
          peak: {
            type: 'point',
            xValue: "11:00",
            yValue: 21,
            backgroundColor: 'red',
            borderColor: 'red',
            radius: 5
          }
        }
      }
    },
    scales: {
      y: {
        title: {
          display: true,
          text: "People Waiting"
        }
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
By converting the descriptive title into a **finding-driven headline**, adding a **targeted annotation**, and including an **actionable caption**, the chart now communicates insight directly and improves decision-making clarity.

