# GA7 — Q5: Broken Aggregation and Sort Order Repair in a Ranking Chart

## Problem Summary
The ranking chart had three independent issues:
1. Incorrect aggregation (sum used instead of average)
2. Incorrect sort order (ascending instead of descending for Top 10)
3. Incorrect highlighted category (not the true top performer)

---

## Fix 1: Correct Aggregation

The chart title specifies:
**"average revenue per transaction"**

So the correct metric is:
- Average = mean of `revenue` grouped by `category`
- NOT sum of revenue

Recomputed category averages (USD):

- Sports: 181.22  
- Toys: 146.46  
- Gaming: 138.50  
- Home: 132.20  
- Pet: 121.17  
- Food: 113.03  
- Garden: 103.88  
- Books: 101.17  
- Travel: 94.04  
- Apparel: 92.41  

---

## Fix 2: Correct Sort Order

Since this is a **Top 10** chart:
- Must be sorted **descending**
- Highest value first

Correct order:
Sports → Toys → Gaming → Home → Pet → Food → Garden → Books → Travel → Apparel

---

## Fix 3: Correct Highlighted Winner

- True top category: **Sports**
- Highlight color moved to Sports

---

## Corrected HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Top 10 categories by average revenue per transaction</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <style>
    body { font-family: sans-serif; margin: 16px; }
    canvas { max-height: 320px; }
  </style>
</head>
<body>
  <!--
  Fixes applied:
  1. Correct aggregation → average revenue per transaction
  2. Correct sorting → descending (Top 10)
  3. Correct highlight → Sports (highest value)
  -->
  <h3>Top 10 categories by average revenue per transaction</h3>
  <canvas id="chart"></canvas>
  <script>
    new Chart(document.getElementById('chart'), {
      type: "bar",
      data: {
        labels: ["Sports","Toys","Gaming","Home","Pet","Food","Garden","Books","Travel","Apparel"],
        datasets: [{
          label: "Top 10 categories by average revenue per transaction",
          data: [181.22,146.46,138.50,132.20,121.17,113.03,103.88,101.17,94.04,92.41],
          backgroundColor: ["#f28e2b","#4e79a7","#4e79a7","#4e79a7","#4e79a7","#4e79a7","#4e79a7","#4e79a7","#4e79a7","#4e79a7"],
          borderColor: "#1f2937",
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          title: {
            display: true,
            text: "Top 10 categories by average revenue per transaction"
          }
        },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  </script>
</body>
</html>
```

---

## Conclusion
By correcting aggregation, ordering, and highlighting, the chart now accurately reflects the intended metric and correctly communicates the top-performing category.

