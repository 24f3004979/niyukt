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

* Implement Student and Company registration and login.
* Create Admin login (Admin is predefined, no registration allowed).
* Admin will approve the Company's Registration, Companies will wait for approval to access the dashboard.
 * Redirect users to role-specific dashboards after login (Admin, Company, Student).
Git Commit Message: Milestone-PPA Auth_RBAC



-----------------------------------------------------------------------------


