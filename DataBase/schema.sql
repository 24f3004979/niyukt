PRAGMA foreign_keys = ON;
-- Foreign Keys config is to be loaded with every connection for cascade and foreign checks
-- Root table : User
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,

    role TEXT NOT NULL CHECK(role in ('student', 'company', 'admin')),
    status TEXT NOT NULL DEFAULT 'active'
        CHECK(status IN ('active', 'deactivated'))
);

-- Company
CREATE TABLE company (
    company_id INTEGER PRIMARY KEY,
    discription TEXT NOT NULL,
    contact_details INTEGER UNIQUE NOT NULL,

    FOREIGN KEY(company_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Student : FIX: We could be having same in company and student validate it
CREATE TABLE student (
    student_id INTEGER PRIMARY KEY,

    resume TEXT,
    branch TEXT,

    FOREIGN KEY(student_id) REFERENCES user(id) ON DELETE CASCADE
);


