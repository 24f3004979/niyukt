from flask import Blueprint, request, render_template, session, redirect, url_for
from model.user import *
from model.student import *
from model.company import *
from auth.login import *
from endpoint.repo import *
from config import *

dashboard_route = Blueprint('/dashboard', __name__, url_prefix="/dashboard")

@dashboard_route.route("/", methods=["GET"])
def dashboard():
    user_repo = Repo("user")
    user = session.get("user_name")
    print(f"Dashboard fetch output : {user}")

    anchor_information = ("name", user)
    fetch = user_repo.fetch(anchor_information, "name")
    status = user_repo.fetch(anchor_information, "status")
    role = user_repo.fetch(anchor_information, "role")

    if not user:
        return redirect("/register/login")

    log.info(f"User Loged in {user}")
    if status == "active": # Based on Role navigate dashboard
        if role == "admin":
            print(f"ADMIN LOGED IN ======+  +++++++++++++++++++++++ +----------------")
            return redirect('/admin')
        elif role == "company":
            return redirect("/company")
        elif role == "student":
            return redirect("/student")
        else:
            return "Crash"
    else:
        return f"<h1> Your account is deactivated by ADMIN : {status} </h1> ACCESS DENIED"


@dashboard_route.route("/user/<username>", methods=['GET'])
def user_dashboard(username):
    # Fetch user information
    return f"User Dashboard Information for student : {username}"

