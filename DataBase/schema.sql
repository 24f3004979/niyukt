PRAGMA foreign_keys = ON; -- Foreign enabled

-- User : student, company, admin by role
create table user (
  -- Information
  id integer primary key autoincrement,
  name text not null,
  password text not null,

  email text not null unique,
  status text not null check( status in ('activated', 'deactivated')), -- Managed by admin
  role text not null check( role in ('student','admin','company'))
);

-- Resume for student
create table resume (
  student_id integer primary key,
  resume_markdown text not null, -- Frontend rende : Skill parsing
  foreign key (student_id) references user(id)
  on delete cascade
);

-- DRIVE : COMPANY 
create table drive (
  id integer primary key autoincrement,

  company_id integer not null,
  role varchar(100) not null,
  detail text,

  -- time for final validations of user response
  created_at timestamp default current_timestamp,
  deadline datetime not null,
  -- Constraints for DRIVE
  constraint deadline_valid check( deadline > created_at),
  foreign key (company_id) references user(id) on delete cascade
);

-- Application : student
create table application (
  student_id integer not null,
  drive_id integer not null,
  status text check( status in ("pending", "shortlisted", "selected")),
  
  -- Format  : YYYY-MM-DD HH:MM:SS
  applied_at datetime not null, -- Frontend timestamp for endtime
  foreign key (drive_id) references drive(id) on delete cascade,
  foreign key (student_id) references user(id) on delete cascade,
  primary key (student_id, drive_id) -- no dupli
);

-- Only created with final validation of student of offer and company decission
create table application_history (
  id integer primary key autoincrement,
  -- id info
  student_id integer not null,
  drive_id integer not null,

  final_result text check(final_result in ("placed", "comp-rejected", "std-rejected")),

  foreign key (student_id) references user(id) on delete cascade,
  foreign key (drive_id) references drive(id) on delete cascade
);
