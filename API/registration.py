from flask import Blueprint, request, render_template

register = Blueprint('/registration', __name__)

# Making student Registration Endpoint

@register.route("/registration")
def registration_home_page():
    return '<h1> Registeration Page </h1>'


@register.route("/register_student" , methods=['POST', 'GET'])
def register_student():
    if request.method == 'GET':
        return render_template('Student_Registration.html')

    if request.method == 'POST':
        return f"Got information as {request}" # TODO: Add logic for Making main core registration for the user after verification if user exists or not
