-- SQLite
CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    invoice_number TEXT NOT NULL,
    purchase_date TEXT NOT NULL,
    buyer_email VARCHAR(50) NOT NULL,
    total_amount DECIMAL(8, 2) NOT NULL
);