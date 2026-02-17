# GA1 — Q17: Average Salary per Department (GROUP BY)

## Problem Summary
The task required calculating the average salary for each department from an `employees` table in SQLite. The results had to be:
- Grouped by department
- Rounded to the nearest whole number
- Ordered alphabetically by department name

## Table Structure
Columns:
- employee_id
- name
- department
- salary

## SQL Solution

```sql
SELECT 
  department,
  ROUND(AVG(salary)) AS average_salary
FROM employees
GROUP BY department
ORDER BY department ASC;
```

## Explanation
- `AVG(salary)` computes the average salary per department.
- `GROUP BY department` separates rows by department.
- `ROUND()` ensures the result is a whole number.
- `ORDER BY department ASC` sorts results alphabetically.

## Result
PASS
