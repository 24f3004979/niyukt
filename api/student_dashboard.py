'''
Student Dashboard Endpoint
    - Drives listing
    - Applied applications
    - account information
'''
from flask import Blueprint, request, render_template, session, redirect
from model.placement import *
from model.user import *
from flask import jsonify
import matplotlib.pyplot as plt
from endpoint.repo import *
from model.drive import *
from model.application import *

student = Blueprint('/student', __name__, url_prefix="/student")

def dashboard_information(user_name):
    anchor_information = ('name', user_name)
    u = User()
    information = u.repo.fetch(anchor_information, 'name,email')
    print(f"Dashboard information loaded for user :{information}")
    return information

@student.route('/')
def root():
    name = session.get('user_name')
    user_repo = Repo('user')
    anchor = ('name', name)
    role = user_repo.fetch(anchor, 'role')
    if role != 'student':
        return redirect('/login')
    drive_list = drive_listing()
    print(f"Drive list : {drive_list}")
    name = session.get('user_name')
    information = dashboard_information(name)
    return render_template('student_dashboard.html', drive_listing=drive_list,dashboard_information=information)

@student.route('/apply/<int:drive_id>', methods=['POST'])
def apply_into(drive_id):
    print(f"drive Id being applied to {drive_id}")
    
    # Applying for given drive id
    id = session.get('id')  # student ID
    info = {'student_id':id, 'drive_id':drive_id}
    application = Application()
    
    try:
        application.create(info) # INFO : Deadline passed Error
        return jsonify({'st':'applied'})
    except Exception as e:
        return jsonify({'st':'failed'})

# Render all applications applied by student and its status
@student.route('/applications', methods=['GET'])
def applicatiions():
    payload = load_applications()
    return payload

def load_applications():
    a = Application()
    id = session.get('id')
    anchor_information = [('student_id',id)]
    applications = a.db.repo_fetch(anchor_information, 'drive_id,status')
    print(applications)
    d = Drive()
    u = User()
    # Fetch applications information company name, role , status
    final_payload = []
    for ap in applications:
        info = {}

        drive_id = ap[0]  # drive id
        status = ap[1]  # status of application
        anchor_info = ('id', drive_id)
        company_id, job_role,drive_id = d.repo.fetch(anchor_info, 'company_id,job_role,id')
        print(f"drive Information {drive_id} with role : {job_role}")

        # Fetch company name with company id
        anchor_info = ('id', company_id)
        company_name = u.repo.fetch(anchor_info, 'name')

        # Final infomration payload
        info['company_name'] = company_name
        info['job_role'] = job_role
        info['status'] = status
        info['drive_id'] = drive_id
        final_payload.append(info)
    return final_payload


def drive_listing():
    '''
    Directly making server based render for listing and loading with api for application
    '''
    drives = Drive()
    anchor_info=[('status','verified')]
    listing_drives = drives.db.repo_fetch(anchor_info, 'company_id,job_role,description,status,id')
    print(f"All of the drives listed :{listing_drives}")

    # company names fetching and making payload for final api response
    u = User()
    listing_payload = []
    for drive in listing_drives:
        info = {}
        id = drive[0]
        anchor_info = ('id', id)
        name = u.repo.fetch(anchor_info, 'name')
        info['company_id'] = id
        info['company_name'] = name
        info['job_role'] = drive[1]
        info['discription'] = drive[2] # discription
        info['status'] = drive[3]
        info['drive_id'] = drive[4]

        # Iterating all of the applications for makig the listing of current status
        applications_list = load_applications()
        current_id = drive[4]
        status = 'apply'
        for i in applications_list:
            if current_id == i['drive_id']: # BUG: Messed up logic for checking status via applications
                status = i['status']
                break 
        info['student_status'] = status  # current student status

        # fetch student drive status with application if any
        listing_payload.append(info)
    return listing_payload # Final payload for verified drives listing
