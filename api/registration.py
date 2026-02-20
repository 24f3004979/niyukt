from flask import Blueprint, request, render_template
from model.user import *


register = Blueprint('/registration', __name__, url_prefix="/register")

# Registration Routing
@register.route("/")
def login_page():
    return "Making Login Page"

@register.route("/student" , methods=['POST', 'GET'])
def student_register():
    if request.method == 'GET':
        return render_template("register_student.html")
    elif request.method == 'POST':
        data = request.form
        user_name = data.get("name")
        password = data.get("password")
        email = data.get("email")
        selection = data.get("branch-selection")
        resume = data.get("resume")

        # Check Existence
        if exists(user_name):
            return "User exists"
        else:
            print(f"User not FOund with name : {user_name}")

            user = User()
            values = tuple([user_name, email, password, "student"])
            print(f"Values for the DB insert functions : values")
            user.db.insert(values)

            # Checking Creation
            creation_request = exists(user_name)
            if creation_request:
                return "You are Registered"
            else:
                print(f"creation Request {creation_request}")
                return "Something went wrong"
            
        
