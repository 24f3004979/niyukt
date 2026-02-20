# Development - Information
```
moduler build -> write tests [ integration & unit ] -> commit for changes
```

## Way to follow

1. DB-Schema
    Made Schema with working constraints and logic flow across the tables
2. Triggers and views | test DB-structure
    basic working triggers and views are working to make application update trigges and auto history storage
3. API endpoints for Backend
    next target to work on for implementing basic db-execution flow with generic model and models to work with making core logic flow for final api-calls
4. Testing API-Endpoints
5. Making minimal Frontend with API


--------------- Critical Learning -----------------------
Sql query buildup with making ? is only for values not for the columns since it would parse the data as 'column' = 'value' , thus we have to make sure we validate in our side about the column and provide values via ? way
