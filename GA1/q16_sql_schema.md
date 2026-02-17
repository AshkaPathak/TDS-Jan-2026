# GA1 — Q16: Infer SQL Schema from CSVs (E-commerce)

## Problem Summary
The task required inferring a relational SQL schema from 4 CSV files (`customers.csv`, `products.csv`, `orders.csv`, `order_items.csv`) and writing `CREATE TABLE` statements with proper constraints: `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, and `CHECK`.

## Data Files and Columns

### customers.csv
- customer_id, email, full_name, signup_date, account_status, loyalty_points

### products.csv
- product_id, product_name, category, price, stock_quantity, supplier_id

### orders.csv
- order_id, customer_id, order_date, total_amount, status, shipping_address

### order_items.csv
- order_item_id, order_id, product_id, quantity, unit_price

## Issues Identified
1. No schema was provided, so data types and keys had to be inferred from CSV content.
2. Referential integrity had to be enforced across tables (`orders` → `customers`, `order_items` → `orders/products`).
3. Fields like dates, prices, quantities, points, and statuses required validation constraints.

## Strategy to Fix
- Use `TEXT` for IDs (since they are alphanumeric like `CUST0001`, `ORD00001`).
- Use `REAL` for monetary values (`price`, `total_amount`, `unit_price`).
- Use `INTEGER` for counts/points (`stock_quantity`, `quantity`, `loyalty_points`).
- Add constraints:
  - `PRIMARY KEY` on each table’s ID column.
  - `FOREIGN KEY` constraints for relationships.
  - `UNIQUE` on `customers.email`.
  - `CHECK` constraints for non-negative numeric fields, date format, and enumerated statuses.
  - `UNIQUE(order_id, product_id)` to prevent duplicate products per order.

## Final SQL Submission
```sql
CREATE TABLE customers (
  customer_id     TEXT PRIMARY KEY,
  email           TEXT NOT NULL UNIQUE,
  full_name       TEXT NOT NULL,
  signup_date     TEXT NOT NULL CHECK (signup_date LIKE '____-__-__'),
  account_status  TEXT NOT NULL CHECK (account_status IN ('active','inactive','suspended')),
  loyalty_points  INTEGER NOT NULL DEFAULT 0 CHECK (loyalty_points >= 0),
  CHECK (customer_id LIKE 'CUST____')
);

CREATE TABLE products (
  product_id      TEXT PRIMARY KEY,
  product_name    TEXT NOT NULL,
  category        TEXT NOT NULL,
  price           REAL NOT NULL CHECK (price >= 0),
  stock_quantity  INTEGER NOT NULL CHECK (stock_quantity >= 0),
  supplier_id     TEXT NOT NULL,
  CHECK (product_id LIKE 'PROD____'),
  CHECK (supplier_id LIKE 'SUPP____')
);

CREATE TABLE orders (
  order_id          TEXT PRIMARY KEY,
  customer_id       TEXT NOT NULL,
  order_date        TEXT NOT NULL CHECK (order_date LIKE '____-__-__'),
  total_amount      REAL NOT NULL CHECK (total_amount >= 0),
  status            TEXT NOT NULL CHECK (status IN ('pending','processing','shipped','delivered','cancelled','refunded')),
  shipping_address  TEXT NOT NULL,
  CHECK (order_id LIKE 'ORD_____'),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id  TEXT PRIMARY KEY,
  order_id       TEXT NOT NULL,
  product_id     TEXT NOT NULL,
  quantity       INTEGER NOT NULL CHECK (quantity > 0),
  unit_price     REAL NOT NULL CHECK (unit_price >= 0),
  CHECK (order_item_id LIKE 'OI_____'),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  UNIQUE (order_id, product_id)
);
```

## Result
PASS
