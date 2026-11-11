-- SQLite
-- Limitation: SQLite does not support adding multiple columns in a single ALTER TABLE statement. 
-- For this reason, each column must be added using separate independent statements.
-- Adding a NOT NULL constraint requires a DEFAULT value to prevent errors on existing rows.

ALTER TABLE invoices
	ADD buyer_phone_number BIGINTEGER NOT NULL DEFAULT 0;

ALTER TABLE invoices
	ADD employee_code TEXT NOT NULL DEFAULT 0;