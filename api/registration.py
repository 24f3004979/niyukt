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

    elif request.method == 'POST':
        data = request.form
        name = data.get("name")
        password = hash_password(data.get("password"))
        email = data.get("email")
        selection = data.get("branch-selection")
        resume = data.get("resume")

        # Payload
        information = {
                "user":{
                    "name" : name,
                    "password_hash" : password,
                    "email" : email,
                    "role" : "student"
                    },
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
