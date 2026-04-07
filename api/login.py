from flask import Blueprint, request, render_template, session, redirect
from model.user import *
from model.student import *
from model.company import *
from auth.login import *
from endpoint.repo import *
from config import *


login_route = Blueprint('/login', __name__, url_prefix='/login')

# Registration Routing
@login_route.route("/", methods=['GET','POST'])
def login_page():
    '''
    Making User Centric redirections for given information
    Procedure
        Fetch information about user
            anchor : Name -> information match 
        Verify with authentication pipeline

        Login user and redirect for relevent pages
    '''
    return render_template("login.html")


@login_route.route('/verification', methods=['POST','GET'])
def login_procedure():

    if request.method == "POST":
        data = request.form
        user_repo = Repo("user")

        # User information
        login_information = {
            "name" : data.get("name"),
            "password" : data.get("password")
        }

        anchor_information = ("name", login_information["name"])
        log.info(f"anchor information : {anchor_information}")

        # Extract Information from Request
        if user_repo.exists(login_information["name"]):

            db_fetched = user_repo.fetch(anchor_information, "id,name,password,role")
            stored_hash = db_fetched[2]
            password = login_information["password"]

            if authentication(stored_hash, password):
                role = db_fetched[2]
                # DB Fetched informatin inspection for passing information about user login
                print(f"DB Fetch result during login : {db_fetched}")

                session["id"] = db_fetched[0]
                session["user_name"] = db_fetched[1]
                return redirect("http://127.0.0.1:8080/dashboard")
            else:
                return "Wrong password"
        else:
            return "User Doesnt Exist | Create Account please :) "
    elif request.method == "GET":
        return 'Mai hu yha'

