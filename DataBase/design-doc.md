# Data Base Implementation

Schema Overview

1. user
    id,name,password,email, status
    > User could be controlled by admin for changing the status for transactions -> implementation : left [ Access Based ]
2. student
    resume, student-id, branch
    > Student Extension to user
    + Make student initiation logic for initiating other process at DB
    + student id is connected to the user table to list out
3. company
    > contact, description,
    + connected for making drives and making edits to applications
4. placementHistory
    > Automated updating unit to store the history of all transactions
5. drives
    > For making placement drives via company required for making applications by students
6. applications
    > Making a applications for the role required via student , unique constraint ensures no duplicate for the request

TODO : 
1. Make Working Queue based Core Executor function for the DB
2. Query builder for executor to accept data from | construct the query via safe way
3. Make easy fetch pipeline for searching and geting information from the DB
4. Finalizing the abstract models for final API-integration and flask wrap up :)
