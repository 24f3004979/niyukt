from flask import Blueprint, request, render_template
from model.student import *
from auth.login import *


register = Blueprint('/registration', __name__, url_prefix="/register")

# Registration Routing
@register.route("/")
def login_page():
    return "Making Login Page"

@register.route("/student" , methods=['POST', 'GET'])
def student_register():  # Working student registration flow tested :)
    if request.method == 'GET':
        return render_template("register_student.html")

# Helper function
def extract_information(data):
    requirements = "name,email,password".split(",")
    fetched = {}
    for i in requirements:
        fetched[i] = data.get(i) # fetched information
    print(f"Information fetched : {fetched}")
    return fetched

    elif request.method == 'POST':
        data = request.form

        info = extract_information(data)
        info["role"] = "student"

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
        # Making Company object


