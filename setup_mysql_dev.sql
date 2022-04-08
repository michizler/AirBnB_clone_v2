-- Creates a database called hbnb_dev_db in the current MySQL server
-- creates the MySQL server user hbnb_test
-- grant permissions for user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev@localhost' IDENTIFIED BY 'hbnb_dev@pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev@localhost' IDENTIFIED BY 'hbnb_dev@pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev@localhost' IDENTIFIED BY 'hbnb_dev@pwd';
FLUSH PRIVILEGES;
