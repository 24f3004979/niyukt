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

