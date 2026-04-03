Lists of most critical peices for building

1. Making multiple anchor chaining mechanism for Query Builder
2. Routes are complicating the api endpoints
    Make central api manager for managing routings and registers
        making dynamic routing with the user specific pages
        @app.route("/user", "<int: user_id>")
        that usr_id could be passed into teh function for loading the given information about that user_id
3. Making Flow for edit informaiton via the requests tab


- Make Login and registration endpoints clear with dashboards
- implement admin approval for the company registration with bare minmum working pipeline
    Go scrappy just implement it with idiotic logic very very simple way
    
    - Target hit milestone :)
    + Routes are messed with all cluttered with the registration pipeline
        Routes are just defining function which would call the underlying given processes not maange the whole workflow for given task
        Remove whole workflow based pipeline with the routes defining functions
    + Improve on update pipeline and Update Query builder and repo managers

    + Authentication pipeline failing for initating the login check with the login of the user witht the sessions
    Sessions are persisting for anyone to access the admin data set without login 

------------------------------
10 march 2026

Targets
    [] : Initiate Authentication and token based loging mechanism
    [] : Crafting Admin components render testing  : tested Now scalling is left for other tabs
    [] : Making simple Js componenets for
            - User Control Panel
            - Request Panel for admin
            - Integrating Panel into Admin dashboard

[] Drive alteration status is not working with making ambiguius changes while clicking  verification button : Working with DB changes


------------------------------------------------------------
25/3/2026
[] Improve loging for clarity about execution flow about the system
[] Build basic data insights page for admin pannel  Basic framework is built
[] Student dashboard Working dashboarding stuff

-----------------------------------------------
Making Simple deleting logic is required for admin panel, 
Include auto delete service of deactivated account after some time

------------------------------------------------------------
Admin Dashboard rendering pipeline
    + Streamline admin panel rendering | Generalize simple components
    + making simple loging for the core working components
    + Making simple authentication pipeline for all of the roles

------------------------------------------------------------
30/march/2026

+ Making Simple data rendering pipeline for admin panel loading
+ data rendering pipeline with respect to data flow into the db

--

# Backend Control panel abstration unit
    + View units [Fetch units integration units]
        ~ Active DB integrated unit for fetching information from DB
        ~ Using Active fetching unit -> Main loop rendering unit

    Flow | fetch data form DB -> Format data for request -> Presentation layer showup

    + Post units [ DB Alteration units for requesting edits]
        + Delete unit for making delete into the DB

    ---
# Frontend Unit for data flow
Making simple data loading flow for processing requests
    making simple data flow loading flow | Fetching request via backend and processing it for making final DB changes
