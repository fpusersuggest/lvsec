--
-- File generated with SQLiteStudio v3.0.7 on mar feb 13 23:01:07 2018
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;


-- Table: t_pkg_on
DROP TABLE IF EXISTS t_pkg_on;
CREATE TABLE t_pkg_on (
	id 		INT PRIMARY KEY NOT NULL, 
	pkg 		TEXT NOT NULL
);

-- Table: t_pkg_off
DROP TABLE IF EXISTS t_pkg_off;
CREATE TABLE t_pkg_off (
	id 		INT PRIMARY KEY NOT NULL, 
	pkg 		TEXT NOT NULL
);

-- Table: t_pkg_files_on
DROP TABLE IF EXISTS t_pkg_files_on;
CREATE TABLE t_pkg_files_on (
	id 		INT PRIMARY KEY NOT NULL, 
	file 		TEXT NOT NULL,
	pkg		INT REFERENCES t_pkg (id)
);

-- Table: t_pkg_files_off
DROP TABLE IF EXISTS t_pkg_files_off;
CREATE TABLE t_pkg_files_off (
	id 		INT PRIMARY KEY NOT NULL, 
	file 		TEXT NOT NULL,
	pkg		INT REFERENCES t_pkg (id)
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


-- Table: t_db
DROP TABLE IF EXISTS t_db;
CREATE TABLE t_db (
	id 		INT PRIMARY KEY NOT NULL UNIQUE, 
	desc		TEXT, 
	data		date,
	uuid		TEXT NOT NULL,
	tipo		BOOL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

