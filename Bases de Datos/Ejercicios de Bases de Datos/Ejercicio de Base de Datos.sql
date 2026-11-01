CREATE TABLE `Products`(
    `Id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Code` TEXT NOT NULL,
    `Name` TEXT NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry Date` DATE NOT NULL,
    `Brand` TEXT NOT NULL,
    `Stock available` INT NOT NULL
);
CREATE TABLE `Invoices`(
    `Id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Invoice Number` TEXT NOT NULL,
    `Purchase Date` DATE NOT NULL,
    `Buyer Email` TEXT NOT NULL,
    `Total Amount` DOUBLE NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `Id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Quantity` INT NOT NULL,
    `Total Amount` DOUBLE NOT NULL,
    `Product Id` BIGINT NOT NULL,
    `Invoice Id` BIGINT NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer Email` TEXT NOT NULL
);
CREATE TABLE `Products Per Shopping Cart`(
    `Id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Product Id` BIGINT NOT NULL,
    `Shopping Cart Id` BIGINT NOT NULL
);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`Id`) REFERENCES `Products Per Shopping Cart`(`Product Id`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`Id`) REFERENCES `Products Per Invoice`(`Product Id`);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`Id`) REFERENCES `Products Per Invoice`(`Invoice Id`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_id_foreign` FOREIGN KEY(`id`) REFERENCES `Products Per Shopping Cart`(`Shopping Cart Id`);