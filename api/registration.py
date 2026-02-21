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
        name = data.get("name")
        password = data.get("password")
        email = data.get("email")
        selection = data.get("branch-selection")
        resume = data.get("resume")
        
        # Data preprocessing

        information = (name, password, email, selection, resume)

        # USER registration
        user = User()
        try:
            user.register(information)
            return "Your Registration is Completed, happy loging in:)"
        except Exception as e:
            log.error(f"Exception Occured with Registration : {e}")
            return f"Registration failed with {e}"

