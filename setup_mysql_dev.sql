-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS edukid_dev_db;
CREATE USER IF NOT EXISTS 'edukid_dev'@'localhost' IDENTIFIED BY 'edukid_dev_pwd';
GRANT ALL PRIVILEGES ON `edukid_dev_db`.* TO 'edukid_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'edukid_dev'@'localhost';
FLUSH PRIVILEGES;