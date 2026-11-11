-- SQLite
SELECT *
    FROM products;

SELECT *
    FROM products
    WHERE price > 50000;

SELECT *
    FROM products_per_invoice
    WHERE product_id = 1;

SELECT
    product_id,
    SUM(quantity) AS total_quantity_per_product,
    SUM(total_amount) AS total_amount_per_product
    FROM products_per_invoice
    GROUP BY product_id;

SELECT *
    FROM invoices
    WHERE buyer_email = 'ana.gomez@gmail.com';

SELECT *
    FROM invoices
    ORDER BY total_amount DESC;

SELECT *
    FROM invoices
    WHERE invoice_number = 'FAC-001';
