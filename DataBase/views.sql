
-- Verified Drives for students
CREATE VIEW verified_drives AS
SELECT
        pd.id,
        pd.job_role,
        pd.description,
        pd.deadline,
        u.name AS company_name
FROM placement_drive pd
JOIN company c ON pd.company_id = c.company_id
JOIN user u ON c.company_id = u.id
WHERE pd.status = 'verified'
        OR pd.status = 'open'; -- Listing all open or verified

-- View All company List | Admin
CREATE VIEW company_list AS
SELECT
        u.id,
        u.name,
        u.email,
        c.discription,
        c.contact_details
FROM user u
JOIN company c ON u.id = c.company_id;

-- View for all students
CREATE VIEW student_list AS
SELECT
        u.id,
        u.name,
        u.email,
        s.branch
FROM user u
JOIN student on u.id = s.student_id;

-- : Students applied to a company drive
CREATE VIEW drive_applicants AS
SELECT
        pd.id AS drive_id,
        pd.job_role,
        a.student_id,
        u.name AS student_name,
        s.branch,
        a.status
    FROM application a
    JOIN placement_drive pd ON a.drive_id = pd.id
    JOIN student s ON a.student_id = s.student_id
    JOIN user u ON s.student_id = u.id;
-- Fetch for specific drives
