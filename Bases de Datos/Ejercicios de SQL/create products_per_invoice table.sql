-- SQLite
CREATE TABLE products_per_invoice(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity INTEGER NOT NULL,
    total_amount DECIMAL(8, 2) NOT NULL,
    product_id INTEGER REFERENCES products(id),
    invoice_id INTEGER REFERENCES invoices(id)
);