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
from model.student import *
from flask import jsonify
import matplotlib.pyplot as plt
from endpoint.repo import *
from model.drive import *
from model.application import *

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
    drives = load_drives()
    return render_template("company_dashboard.html", drives=drives)

def load_drives():
    placement = Placement()
    id = session.get('id')

    # Loading Drive with drive class inbuilt generic support

    drives = Drive()
    anchor_information = [('company_id', id)]
    # Best way to fetch based on my framework
    company_drive = drives.db.repo_fetch(anchor_information, 'job_role,description,status,id')
    
    print(f"company drive: {company_drive}")
    return company_drive


@company.route('/applications/<int:drive_id>', methods=['GET'])
def applications(drive_id):
    '''
    Filter query to DB with company name
    fetching all applications with given drive id

    Fetch via DB for given drive id applications

    id fetching pipeline : 
        fetch student id form application table for given drive id
            -> For requested student load its basic profile
    '''
    ap = Application()
    anchor_information = [('drive_id', drive_id)]
    students_list = ap.db.repo_fetch(anchor_information, 'student_id')

    # Making List of all students 
    std_l = []
    for s in students_list:
        std_l.append(s[0])

    # Fetching information about the student via fetch of repo
    usr = User()
    student = Student()
    payload = []
    for st in std_l:
        info = {}
        anchor_info = ('id',st)
        name = usr.repo.fetch(anchor_info, 'name')
        info['name'] = name  # Name of student
        anchor_info = ('student_id', st)
        resume = student.repo.fetch(anchor_info, 'resume')
        info['resume'] = resume
        anchor_info = ('student_id',st)
        status = ap.repo.fetch(anchor_info, 'status')
        info['status'] = status
        payload.append(info)

    return payload  # List of all students who applied for given drive
    

@company.route('/alter-application', methods=['POST'])
def alter_application():
    '''
    Taking application id and changing its status via code

    Made specific function in application class for making
        s => shortlisted
        r => rejected
        p => placed
    '''
    data = request.get_json()
    print(f'Initiating alteration sequence ')
    
    application_id = data.get('drive_id')
    current_status = data.get('status')  # current status
    target_status = data.get('target_status')

    application = Application()
    
    # Making basic logic for changing status
    update_info = ('status', target_status) # making simple change
    anchor_information = ('id', application_id)
    try:
        application.db.update(update_info, anchor_information)
        print(f'Student Being Selected')
        return jsonify({'st':target_status})
    except Exception as e:
        print(f"Failing with {e}")
        return jsonify({'st':current_status})


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


