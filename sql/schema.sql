CREATE TABLE IF NOT EXISTS "products" (
    name TEXT,
    category TEXT,
    quantity INTEGER CHECK(quantity >= 0),
    price REAL CHECK(price >= 0)
);
