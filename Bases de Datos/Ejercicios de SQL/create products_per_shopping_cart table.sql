-- SQLite
CREATE TABLE products_per_shopping_cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    product_id INTEGER REFERENCES products(id),
    shopping_cart_id INTEGER REFERENCES shopping_cart(id)
);