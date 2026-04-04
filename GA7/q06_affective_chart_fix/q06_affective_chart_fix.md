# GA7 Q6 – Affective Chart Fix

## Explanation

The chart exaggerates small changes by truncating the y-axis, making the growth appear dramatic even though the actual variation is minimal.

## Corrected HTML

```html
<!-- Quantification: 12.4x Distortion: inflates tiny deltas by 12.4x -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>What does this chart claim to show? Quarterly uplift is dramatic</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    body { font-family: system-ui, sans-serif; margin: 16px; }
    canvas { max-height: 340px; }
  </style>
</head>
<body>
  <h3>What does this chart claim to show? Quarterly uplift is dramatic</h3>
  <canvas id="chart"></canvas>
  <script>
    new Chart(document.getElementById('chart'), {
      type: "line",
      data: {
        labels: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
        datasets: [{
          label: "Revenue Index",
          data: [888.55,900.48,902.92,912.39,919.27,919.02,928.39,937.37],
          borderColor: "#2563eb",
          backgroundColor: "rgba(37, 99, 235, 0.15)",
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: "What does this chart claim to show? Quarterly uplift is dramatic"
          }
        },
        scales: {
          y: {
            min: 0,
            beginAtZero: true
          }
        }
      }
    });
  </script>
</body>
</html>
```
