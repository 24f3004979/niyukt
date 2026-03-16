'''
Admin DashBoard Api-Endpoints

Features
    + user control endpoint
        Requesting activation/deactivation of user
    + Requests panel for admin for approval and rejection -> history of all admin decissions
'''
from flask import Blueprint, request, render_template 
from model.user import *
from flask import jsonify

admin = Blueprint('/admin', __name__, url_prefix="/admin")

@admin.route("/") 
def root():
    return render_template("admin.html")


@admin.route("/users", methods=["GET"])
def fetch_user():

    user = User()
    anchor_info = [("role", "company")] # Due to list based fetch
    data = user.db.repo_fetch(anchor_info, required_columns="name,role,status")
    resp = []
    for elem in data:
        dicto = {}
        dicto["name"] = elem[0]
        dicto["role"] = elem[1]
        dicto["status"] = elem[2]
        resp.append(dicto)
    return resp

@admin.route("/alter-status", methods=["POST"])
def alterstatus():
    data = request.get_json()
    user_name = data.get("name")
    status = data.get("st").strip()

    print(f"Status for update request : {status}")

    user = User()
    # Updating DB
    try:
        anchor_information = ("name",user_name)
        update_information = ("status", status)

        user.db.update(update_information, anchor_information)
        if status == "deactivated":
            return jsonify({"status":"success", "st":"active"})
        else:
            return jsonify({"status":"success", "st":"deactivated"})
    except Exception as e:
        print(f"Updating User inforamation failed with {e}")
        return jsonify("status", "Failed")


@admin.route("/user-panel", methods=["GET", "POST"])
def user_control():
    if request.method == "GET":
        user_list = [
            {"name": "Madhav", "role":"student", "status":"active"}
        ]
        # Rendering user list with given JS constraints
        return user_list
    elif request.method == "POST":
        data = request.get_json()
        name = data["name"]  # Making edit to the user-data
        print(f"name : {name}")
        status = True
        return jsonify({"status": status})
