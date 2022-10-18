DROP TABLE IF EXISTS posts;

CREATE TABLE records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    phonenumber INTEGER NOT NULL,
    reason TEXT NOT NULL
    evidence 
);

CREATE TABLE report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    phonenumber INTEGER NOT NULL,
    reason TEXT NOT NULL
    evidence 
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    psswrd TEXT NOT NULL,
    
);

CREATE TABLE summary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phoneno INTEGER NOT NULL,
    fullname TEXT NOT NULL,
    faddress TEXT NOT NULL
    idpic 
    sprovider TEXT NOT NULL
);