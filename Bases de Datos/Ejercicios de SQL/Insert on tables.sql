-- SQLite
-- Limitation: Foreign keys are disabled by default in SQLite. 
-- We must explicitly enable them at the beginning of the session to enforce referential integrity.

PRAGMA foreign_keys = ON;


INSERT INTO products (code, name, price, entry_date, brand, stock_available) VALUES
('P001', 'Laptop HP ProBook', 450000.00, '2026-01-10', 'HP', 15),
('P002', 'Mouse Inalámbrico Logitech', 25000.00, '2026-02-15', 'Logitech', 50),
('P003', 'Teclado Mecánico Redragon', 65000.00, '2026-03-01', 'Redragon', 30),
('P004', 'Monitor Samsung 24"', 120000.00, '2026-03-20', 'Samsung', 12),
('P005', 'Silla Gamer Corsair', 150000.00, '2026-04-05', 'Corsair', 8);


INSERT INTO shopping_cart (buyer_email) VALUES
('ana.gomez@gmail.com'),
('carlos.mora@gmail.com'),
('maria.rojas@gmail.com'),
('luis.perez@gmail.com'),
('sofia.castro@gmail.com');


INSERT INTO invoices (invoice_number, purchase_date, buyer_email, total_amount, buyer_phone_number, employee_code) VALUES
('FAC-001', '2026-05-01', 'ana.gomez@gmail.com', 475000.00, '8888-1111', 'EMP01'),
('FAC-002', '2026-05-02', 'carlos.mora@gmail.com', 65000.00, '8888-2222', 'EMP02'),
('FAC-003', '2026-05-03', 'maria.rojas@gmail.com', 120000.00, '8888-3333', 'EMP01'),
('FAC-004', '2026-05-04', 'luis.perez@gmail.com', 150000.00, '8888-4444', 'EMP03'),
('FAC-005', '2026-05-05', 'sofia.castro@gmail.com', 25000.00, '8888-5555', 'EMP02');


INSERT INTO products_per_shopping_cart (product_id, shopping_cart_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4);

-- 5. Insertar registros en PRODUCTS_PER_INVOICE[cite: 4]
INSERT INTO products_per_invoice (quantity, total_amount, product_id, invoice_id) VALUES
(1, 450000.00, 1, 1),
(1, 25000.00, 2, 1),
(1, 65000.00, 3, 2),
(1, 120000.00, 4, 3),
(1, 150000.00, 5, 4);