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

def dashbaord_information(user_name):
    pass # Making stuent specific dashbaord information

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
    return render_template('student_dashboard.html', drive_listing=drive_list)

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
        listing_payload.append(info)
    return listing_payload # Final payload for verified drives listing
