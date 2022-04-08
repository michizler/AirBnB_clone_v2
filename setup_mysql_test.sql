-- Creates a database called hbnb_dev_db in the current MySQL server
-- creates the MySQL server user hbnb_test
-- grant permissions for user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test@localhost' IDENTIFIED BY 'hbnb_test@pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test@localhost' IDENTIFIED BY 'hbnb_test@pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test@localhost' IDENTIFIED BY 'hbnb_test@pwd';
FLUSH PRIVILEGES;
