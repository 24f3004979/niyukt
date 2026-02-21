# Targets

Priority : CORE REQUIREMENTS
[-] - Validate Schema design and document design decisions and plans
[-] - Triggers for final DB-validations and Error handeling for logic layer
[] - Build Models and DB-linking module { Query builder, threaded Queue, fetch handle }
    [] Make Simple core execution pipeline
        Task => QueryBuilder() -> Executor Queue -> Execute to DB
    [] Craft Generic Data handeling Base Models for other models to work on
    [] test out generic models and Core execution and validation pipeline with loging mechanism for easy debug
    -- Worthy to go with making the real abstract models


--------------- Core Requirements for official Milestones ----------
1. Milestone: Authentication and Role-Based Access
✅ Expected Time: 5 days
📊 Completion Progress: 10%

* Implement Student and Company registration and login. [ Working]
    Required Development of 
        * Working Generic Model for edit and creation with defined behaviour
        * working abstract Models for Making creations and requests automated
        * Final Wraping API for the all functions to handle requests
        * Basic Authentication Pipeline for Making hashed Password and login System via authentication routing system 
* Create Admin login (Admin is predefined, no registration allowed).
    * Automated with Previous developement
* Admin will approve the Company's Registration, Companies will wait for approval to access the dashboard.

    Simple Approval requests tab to list out all company waiting for registration
 * Redirect users to role-specific dashboards after login (Admin, Company, Student).
    * Making redirects via verification of credentials and routing via DB fetch for specified pages and embeding access token based security for pages to fetch information from the DB part via central JS requesting tool after registration process
Git Commit Message: Milestone-PPA Auth_RBAC
-----------------------------------------------------------------------------


ONGOING WORK : Making working registration pipeline , first make it working then we would scale and optimize it for other entities and scale  the design and improve bro you got this ...

