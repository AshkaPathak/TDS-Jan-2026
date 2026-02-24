# GA3 — Q1: FIFA World Cup Data Cross-Table Analysis (1 mark)

## Problem Summary
You are given two tables from the FIFA World Cup Wikipedia page:
1. **Teams reaching the top four**
2. **Top goalscorers**

You must load both into Google Sheets, analyze them using formulas, and compute:

1. How many times England finished in fourth place  
2. How many World Cup goals Helmut Rahn scored  

Submit answers comma-separated.

---

## Final Answer

2, 10

---

## Step 1 — Import “Teams reaching the top four” table

In Google Sheets (Tab name: `top4_teams`), cell A1:

```gs
=IMPORTHTML("https://en.wikipedia.org/wiki/FIFA_World_Cup","table",6)
```

This imports the summary table containing:
- Team
- Titles
- Runners-up
- Third place
- Fourth place
- Top 4 total

---

## Step 2 — Find England’s fourth-place finishes

Locate the row for **England**.

In the "Fourth place" column it shows:

2 (1990, 2018)

Therefore:

England finished fourth **2 times**.

---

## Step 3 — Import “Top goalscorers” table

Create a new tab (e.g., `top_scorers`), cell A1:

```gs
=IMPORTHTML("https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_top_scorers","table",1)
```

If table 1 does not load correctly, try table index 2 or 3.

---

## Step 4 — Extract Helmut Rahn’s goal count

Assuming:
- Player name column = B
- Goals column = C

Use:

```gs
=QUERY(A:Z, "select B, C where B = 'Helmut Rahn'", 0)
```

This returns:

Helmut Rahn — 10

Therefore:

Helmut Rahn scored **10 World Cup goals**.

---

## Submission Format

Enter the values comma-separated:

2, 10

---

## GitHub Setup

Ensure this file exists at:

GA3/q01_fifa_world_cup_cross_table_analysis/q01_fifa_world_cup_cross_table_analysis.md

Then run:

```bash
cd ~/TDS-Jan-2026
git add GA3/q01_fifa_world_cup_cross_table_analysis/q01_fifa_world_cup_cross_table_analysis.md
git commit -m "GA3 Q1: FIFA World Cup cross-table analysis"
git push
```

---

## Conclusion

England fourth-place finishes = 2  
Helmut Rahn World Cup goals = 10  

Final submitted answer:

2, 10
