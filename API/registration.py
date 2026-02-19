from flask import Blueprint, request, render_template
from model.student import *
from DataBase.Executor import *

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

        # Validate If user Exists -- Model call for verification
        exist = existence(user_name)
        if exist:
            return "USER EXISTS :)"
        else:
            pass # Working Endpoints now code base is mess



        
        
