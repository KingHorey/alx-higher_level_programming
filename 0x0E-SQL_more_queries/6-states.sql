-- I want to create database
-- and also create a table in it

CREATE SCHEMA IF NOT EXISTS hbtn_0d_usa;

-- switch to database
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
