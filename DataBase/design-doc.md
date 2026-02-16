# DB-design

Core Data tables
    + user
        > User is Root table for student, company, admin
        handle all user level information and fetch requests
        > DB - triggers are also using roles for seting up transactions final validation

    + application
        > Student creates application, for drive 
        creation triggers
            student validation + company validation + time stamp validation
            if all conditions validate addition takes place to update the status

        status = shortlisted --> Updates the student's application part
        status = selected [ Finalised via company for final decission ] 
        triggers
            Adds student to application_history and makes entry for placement record
        ** Company can take multiple students as they finalise their choice and close the drive **
        triggers : rejecting all students --> placement record update

    + drive 
        > A port to set for application
        > Validated via Admin panel

-- Constraints --
creating application
    + Student must exist
    + Drive should not be expired

-- Issues and reslution proposal --
+ How timestamp would be evaluated for application ?
    ]- Js request would consist of timestamp of request which would be validated via trigger at DB-level to validate and Add up to the DB or raise Error


