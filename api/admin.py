'''
Admin DashBoard Essential Endpoints
Admin Landing Page
    /admin
        Dashboard renders images from backend
        Live dash board features - future scaled
    
    /admin/requests
        GET
        Lists all admin requests
        POST
        Accept - given request --> Update given information [ Update required ]

'''
from flask import Blueprint, request, render_template 
from model.user import *

admin = Blueprint('/admin', __name__, url_prefix="/admin")

@admin.route("/")  # BUG : Any one can fetch information about all students :)
def root():
    return "ADMIN DASHBOARD"

@admin.route("/approval", methods=["POST", "GET"])
def approvals():
    if request.method == "GET":
        return "Hi i am here"
    if request.method == "POST":
        data = request.form
        user_model = User()
        # iterating for changing their status via update unit of generic model
        for company in data:
            anchor_information = ("name", company)
            update_information = ("status", "active")
            if not(user_model.db.update(update_information, anchor_information)):
                return "Updating status Failed with unexpected failior in generic Model"
        return f"Status Updated for Company {data}"

@admin.route("/requests", methods=["GET", "POST"])
def requests():
    if request.method == "GET":
        ''' Fetch all requests for company registrations'''
        user = User()
        anchor_information = [("status", "deactivated"), ("role","company")]
        # Making this to fetch just the company names only
        anchor_information = [("role", "company"), ("status", "deactivated")]
        requests_list = user.db.repo_fetch(anchor_information, "name")
        print(f"Fetched Requests : {requests_list}")

        return render_template("request_tab.html", requests_list=requests_list)
    elif request.method == "POST":
        pass


