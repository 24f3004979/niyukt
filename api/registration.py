from flask import Blueprint, request, render_template, session, redirect
from model.user import *
from model.student import *
from model.company import *
from auth.login import *
from endpoint.repo import *
from config import *

# TODO : Mantain Routes organization, Adjust scope of the functions with modularity of the routes file directions and improve upon defining endpoint
'''
Introduce dynamic routing with secure access routes for the core application modules
    + Yet to improve with moduler way for access of routes and information
    + Login isnt working # BUG : to fix
'''


register = Blueprint('/registration', __name__, url_prefix="/register")

@register.route("/")
def root():
    return "Register root: Navigations and Linking registration routes"

# Registration Routing
@register.route("/login", methods=['GET','POST'])
def login_page():
    '''
    Making User Centric redirections for given information
    Procedure
        Fetch information about user
            anchor : Name -> information match 
        Verify with authentication pipeline

        Login user and redirect for relevent pages
    '''
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
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

            db_fetched = user_repo.fetch(anchor_information, "name,password,role")
            stored_hash = db_fetched[1]
            password = login_information["password"]

            if authentication(stored_hash, password):
                role = db_fetched[2]
                session["user_name"] = db_fetched[0]
                return redirect("http://127.0.0.1:8080/register/dashboard")
            else:
                return "Wrong password"
        else:
            return "User Doesnt Exist | Create Account please :) "

@register.route("/dashboard", methods=["GET"])
def dashboard():
    user_repo = Repo("user")
    user = session.get("user_name")

    anchor_information = ("name", user)
    fetch = user_repo.fetch(anchor_information, "name")
    status = user_repo.fetch(anchor_information, "status")

    if not user:
        return redirect("/register/login")
    log.info(f"User Loged in {user}")
    if status == "active":
        return f"<h1> Wellcome {user} </h1>"
    else:
        return f"<h1> Your account is deactivated by ADMIN : {status} </h1> ACCESS DENIED"

@register.route("/logout", methods=["GET"])
def logout():
    session.clear()
    print(f"Loged out user")
    return redirect("/login")


@register.route("/student" , methods=['POST', 'GET'])
def student_register():  # Working student registration flow tested :)
    if request.method == 'GET':
        return render_template("register_student.html")
    elif request.method == 'POST':
        data = request.form

        info = extract_information(data)
        info["role"] = "student"
        info["status"] = "active"
        # password hash

        selection = data.get("branch-selection")
        resume = data.get("resume")

        # Payload
        information = {
                "user":info,
                "student": {
                    "branch" : selection,
                    "resume" : resume
                    }
                }
        student = Student()
        try:
            if student.activate(information):
                return "Student Registered : Wellcome to niyukt"
            else:
                return "Student Registration Failed"
        except Exception as e:
            return f"Failing With {e}"

@register.route("/company", methods=['POST', 'GET'])
def register_company():
    if request.method == "GET":
        return render_template("register_company.html")
    elif request.method == "POST":

        data = request.form
        info = extract_information(data)
        info["role"] = "company"
        info["status"] = "deactivated"

        description = data.get("description")
        # company information
        information = {
                "user" : info,
                "company": {
                    "description" : description
                    }
                }
        log.info(f'Company information for initiation :::: {information}')
        company = Company()

        try:
            if company.initiate(information):
                return f"Company Registered : Admin Aproval required"
            else:
                return "Company Registration Failed"
        except UserExists as e:
            return f"User Exsists"
        except Exception as e:
            return "Company Registration failed : Error"


        
def extract_information(data):
    requirements = "name,email,password".split(",")
    fetched = {}
    for i in requirements:
        fetched[i] = data.get(i) # fetched information
    fetched["password"] = hash_password(fetched['password'])
    return fetched

