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

@admin.route("/requests", methods=["GET", "POST"])
def requests():
    if request.method == "GET":
        ''' Fetch all requests for company registrations'''
        user = User()
        anchor_information = ("status", "deactivated")
        requests_list = user.db.repo.mass_fetch(anchor_information, "id, name, role")

        print(f"Fetched Requests : {requests_list}")

        return render_template("request_tab.html", requests_list=requests_list)
    elif request.method == "POST":
        pass


