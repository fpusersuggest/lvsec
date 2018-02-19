--
-- File generated with SQLiteStudio v3.0.7 on mar feb 13 23:01:07 2018
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: t_offline
DROP TABLE IF EXISTS t_offline;
CREATE TABLE t_offline (
	id 		INT PRIMARY KEY NOT NULL UNIQUE, 
	nome 		TEXT NOT NULL, 
	stato 	TEXT, 
	sha256 	TEXT (64), 
	md5 		TEXT (32), 
	pkg 		INT REFERENCES t_pkg (id)
);

-- Table: t_pkg
DROP TABLE IF EXISTS t_pkg;
CREATE TABLE t_pkg (
	id 		INT PRIMARY KEY NOT NULL, 
	pkg 		TEXT NOT NULL
);

-- Table: t_online
DROP TABLE IF EXISTS t_online;
CREATE TABLE t_online (
	id 		INT PRIMARY KEY NOT NULL UNIQUE, 
	nome 		TEXT NOT NULL, 
	stato 	TEXT, 
	sha256 	TEXT (64), 
	md5 		TEXT (32), 
	pkg 		INT REFERENCES t_pkg (id)
);



COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

