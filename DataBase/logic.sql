-- Lgical Tables for the application

CREATE TABLE placement_drive (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  company_id INTEGER NOT NULL,
  job_role TEXT NOT NULL,
  description TEXT NOT NULL,

  deadline DATETIME NOT NULL DEFAULT (DATETIME('now', '+10 days')),
  status NOT NULL DEFAULT 'not_verified'
    CHECK(status in ('verified', 'not_verified', 'open', 'closed')),

  -- constraints
  UNIQUE(company_id, job_role),
  FOREIGN KEY(company_id) REFERENCES company(company_id) ON DELETE CASCADE
);


-- TODO : testing required
CREATE TABLE application (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 

  student_id INTEGER NOT NULL, 
  drive_id INTEGER NOT NULL,

  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  status TEXT NOT NULL DEFAULT 'pending'
    CHECK(status in ('pending', 'selected', 'shortlisted', 'rejected')),
  UNIQUE(student_id, drive_id),

  FOREIGN KEY(student_id) REFERENCES student(student_id) ON DELETE CASCADE,
  FOREIGN KEY(drive_id) REFERENCES placement_drive(id) ON DELETE CASCADE
);

CREATE TABLE placement_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  student_id INTEGER NOT NULL,
  drive_id INTEGER NOT NULL,

  final_result TEXT NOT NULL
    CHECK( final_result in ('selected', 'rejected')),
  
  UNIQUE(student_id, drive_id)
  FOREIGN KEY(student_id) REFERENCES student(student_id),
  FOREIGN KEY(drive_id) REFERENCES placement_drive(id)
);

