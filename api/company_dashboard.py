'''
Company dashboard
    - Create Drives
    - See all listed drives
        - Get respective applications
          filter students
'''
from flask import Blueprint, request, render_template, session, redirect
from model.placement import *
from model.user import *
from flask import jsonify
import matplotlib.pyplot as plt
from endpoint.repo import *
from model.drive import *

company = Blueprint('/company', __name__, url_prefix="/company")

def dashboard_information(user_name):
    pass


@company.route("/") 
def root():
    name = session.get('user_name')
    user_repo = Repo('user')
    anchor = ('name', name)
    role = user_repo.fetch(anchor, "role")
    if role != 'company':
        return redirect('/login')

    # A base User html template rendering both student and company dashboard with basic informations
    information = {"drives":10, "applications":10, "running_drives":10}
    return render_template("company_dashboard.html", information=information)

@company.route('/drives', methods=['GET'])
def load_drives():
    placement = Placement()
    id = session.get('id')
    print(f"Company id  : {id}")
    anchor = ("company_id", id)
    company_drive = placement.repo.fetch(anchor, 'job_role,description')
    print(f"company drive: {company_drive}")

    return jsonify({"drive":company_drive})  # company drive information

@company.route('/applications/<int:drive_id>', methods=['GET'])
def applications(drive_id):
    '''
    Filter query to DB with company name
    fetching all applications with given drive id
    '''
    pass
    

@company.route('/alter-application', methods=['POST'])
def alter_application():
    pass # Making alteration with given given application id

@company.route('/create-drive', methods=['GET', 'POST'])
def create_drive():
    if request.method == "GET":
        return render_template('placement_drive.html')
    
    if request.method == "POST":
        data = request.form

        job_role = data.get('job_role')
        description = data.get('description')
        id = session.get('id')  # company id

        info = {"company_id":id, 'job_role':job_role, 'description':description}
        d = Drive()
        try:
            made = d.create(info)
        except Exception as e:
            return "Exists Such Role"
        if made:
            return "Drive Created"
            
        else:
            return "Failed to create drive"


