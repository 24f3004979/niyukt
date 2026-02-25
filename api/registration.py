from flask import Blueprint, request, render_template
from model.student import *
from model.company import *
from auth.login import *


register = Blueprint('/registration', __name__, url_prefix="/register")

@register.route("/")
def root():
    return "Register root"

# Registration Routing
@register.route("/login", methods=['GET','POST'])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        data = request.form
        user_name = data["name"]
        password = data["password"]
        # Making Authentication logic with login api
        information = {"name":user_name, "password":password}

        result = authenticate_user(information) # 1 - authenticated , 2- password wrong , 0 - user not found
        if result == 1:
            return "User Verified"
        elif result == 2:
            return "Incorrect Password"
        else:
            return "User Not found"

@register.route("/student" , methods=['POST', 'GET'])
def student_register():  # Working student registration flow tested :)
    if request.method == 'GET':
        return render_template("register_student.html")
    elif request.method == 'POST':
        data = request.form

        info = extract_information(data)
        info["role"] = "student"
        # password hash
        info["password"] = hash_password(info["password"])

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
            student.activate(information)
            return "Welcome to niyukt login now :)"
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

        description = data.get("discription")
        contact_details = data.get("contact_details")

        # company information
        information = {
                "user" : info,
                "company": {
                    "discription" : description,
                    "contact_details" : contact_details
                    }
                }
        print(f'Company information : {information}')

        company = Company()
        company.initiate(information) # root for bugs 
        # TODO Final Check sums for the company registration is left for completion
        '''
        With company registration working we can move for making fetch based admin dashboards and other systems :)
        '''

def extract_information(data):
    requirements = "name,email,password".split(",")
    fetched = {}
    for i in requirements:
        fetched[i] = data.get(i) # fetched information
    print(f"Information fetched : {fetched}")
    return fetched

