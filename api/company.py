'''
Making Simple dashboard for company
Requirements
    1. making new drive : Approval required
    2. View Applications -- Applied by students
    3. shortlist candidate or select candidate
    4. view candidate profile -- fetching more information about user
    
Basic Pathway
GET Endpoints
    + applications by students -> Fetched with frontend with frequent update
    + view all drives made by company -> approved and not approved listing

POST Endpoints
    + Editing students status [ shortlisted | rejected ]
'''
from flask import Blueprint, request, render_template, session
from model.drive import *

company = Blueprint('/company', __name__, url_prefix="/company")

@company.route("/")
def root():
    return render_template("Company dashboard root")

@company.route('/drive', methods=["GET","POST"])
def new_drive():
    '''
    Making new drive for the job posting |
        Making new drive for the given students
    '''
    if request.method == "GET":
        return render_template("placement_drive.html")
    elif request.method == "POST":
        company_id = session["id"]
        drive = Drive()
        data = request.form
        print(data)

        job_role = data.get("job_role")
        description = data.get("description")

        info = {}
        info["company_id"] = company_id
        info["job_role"] = job_role
        info["description"] = description

        try:
            if drive.create(info):
                return "<h1> Drive created waiting for response </h1>"
            else:
                return "<h1> Drive Creation failed </h1>"
        except Exception as e:
            return f"Exception Occured with : {e}"
    else:
        return "Wrong Request Made"

@company.route('/drive-listing', methods=['GET'])
def listing_drives():
    '''
    Listing all drives made by company for the students
    Job role  : Description : status
    '''
    pass
