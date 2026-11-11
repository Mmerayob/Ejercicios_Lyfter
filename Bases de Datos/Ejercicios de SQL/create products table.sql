-- SQLite
-- entry_date is stored as TEXT (format 'YYYY-MM-DD') due to SQLite native date type limitation
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    code VARCHAR(25) NOT NULL,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    entry_date TEXT NOT NULL, 
    brand VARCHAR(50) NOT NULL,
    stock_available INTEGER NOT NULL
);