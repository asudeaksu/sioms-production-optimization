-- SIOMS SQL Analysis Queries
-- Inventory analysis for the products table.

-- 1. Display all products
SELECT
    name,
    category,
    quantity,
    price
FROM products;

-- 2. Calculate inventory value for each product
SELECT
    name,
    category,
    quantity,
    price,
    quantity * price AS inventory_value
FROM products
ORDER BY inventory_value DESC;

-- 3. Calculate total inventory value
SELECT
    SUM(quantity * price) AS total_inventory_value
FROM products;

-- 4. Calculate total quantity by category
SELECT
    category,
    SUM(quantity) AS total_quantity
FROM products
GROUP BY category
ORDER BY total_quantity DESC;

-- 5. Identify low-stock products
SELECT
    name,
    category,
    quantity
FROM products
WHERE quantity < 10
ORDER BY quantity ASC;
