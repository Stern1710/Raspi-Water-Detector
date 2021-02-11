
/* Creating databse */
CREATE DATABASE IF NOT EXISTS plantdb;
USE plantdb;

/* Creating tables in database */
CREATE TABLE IF NOT EXISTS datasets (
    data_id INT AUTO_INCREMENT,
    temp INT NOT NULL,
    readTime DATETIME NOT NULL DEFAULT NOW(),
    isWatered BIT NOT NULL DEFAULT 1,
    PRIMARY KEY(data_id)
);

/* Creating user for access to database */
CREATE USER IF NOT EXISTS 'user'@'server' IDENTIFIED BY 'Password';
GRANT ALL PRIVILEGES ON plantdb.* TO 'user'@'server';
FLUSH PRIVILEGES;