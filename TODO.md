# Targets
[1] ## Basic Setup
    1. Working DB triggers and core mechanism for the data flow
    2. Schema, entity , triggers and views
    3.Basic Routing Setup for project

[2] ## Authentication and Role based access
Targets
    1. implement student and company registration flow
        + Working student Pipeline 
            Needs basic refactor for scalling for other entities
            - Implement clear data flow and error fallbacks
            - Generalize with the data flow for all elements
    2. Admin Login and company registration Approval
    3. Redirect Logins into relevent pages for dashboard

Issue
  + Maing pipeline is failing due to issues with data flow

IMPLEMENTATION Targets
1. login page | Making login for all and registration nav for student and company 
2. Making redirectioins for all login credentials 

---- Improvements ------
+ Handle request with ease : Request extraction module required
+ Make defined output / input flow for the meta models and base models
+ Include Unique constrained failed based roll back and loockups with fetch requests
