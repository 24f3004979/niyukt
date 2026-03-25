'''
Admin DashBoard Api-Endpoints

Features
    + user control endpoint
        Requesting activation/deactivation of user
    + Requests panel for admin for approval and rejection -> history of all admin decissions
'''
from flask import Blueprint, request, render_template 
from model.placement import *
from model.user import *
from flask import jsonify

admin = Blueprint('/admin', __name__, url_prefix="/admin")

@admin.route("/") 
def root():
    return render_template("admin.html")

# User Panel Control units

@admin.route("/users", methods=["GET"])
def fetch_user():

    user = User()
    anchor_info = [("role", "company")] # Due to list based fetch
    data = user.db.repo_fetch(anchor_info, required_columns="name,role,status")
    
    # Fetch students also
    anchor_info = [("role", "student")]
    data += user.db.repo_fetch(anchor_info, required_columns="name,role,status")

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

    print(f"Initial status of given element : {status}")

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

@admin.route("/requests", methods=["GET"])
def requests():
    '''
    Placement Drive Listing
    
    Fetching information about all of the placement drves from the DB
    '''
    print("Running requests fetching endpoint")
    placement = Placement()
    user = User()
    # Make a handle for fetch endpoint for geting all of the given data entity with given column requests
    listing_information = placement.repo.fetch_instance("*") # TODO : Formating is also requied into json way
    # Simple formating with fetching company name with given id of company
    print(f"listing information : {listing_information}")
    log.info(f"Listing information : {listing_information}")
    final_list = []
    for row in listing_information:
        company_id = row[1] # Company id get name
        anchor_information = ("id", company_id)
        name = user.db.repo.fetch(anchor_information, "name")
        print(f"Fetch results : {anchor_information}, {name}")

        payload = {
            "company_name" : name,
            "drive_id" : row[0],
            "company_id" : company_id,
            "job_role" : row[2],
            "discription" : row[3],
            "status" : row[5]
        }
        log.info(f"Payload : {payload}")
        final_list.append(payload)

    return final_list

# verification and not verified status togle control endpoint
@admin.route("/alter-drive-status", methods=["POST"])
def placement_drive():
    '''
    Simple Alteration for the placement drive status
    '''
    drives = Placement()
    data = request.get_json()
    current_status = data.get("st").strip()
    id = data.get("drive_id")
    # Chaning status and returning updated version
    anchor_information = ("id", id)
    print(f"Initiating alteration sequence for drive status update : {anchor_information}")
    if current_status == "not_verified":
        update_information = ("status", "verified")
        print(f"Update sequence initiation under process INFO : {update_information} with anchor information  : {anchor_information}")
        if drives.db.update(update_information, anchor_information):
            print(f"Success with update of the information for the placement drive")
            return jsonify({"status":"success", "st":"verified"})
        print(f'Update sequence for placement drive alteration failed with update check logs')

    else:
        update_information = ("status", "not_verified")
        if drives.db.update(update_information, anchor_information):
            return jsonify({"status":"success", "st": "not_verified"})
        print(f"Failed with update at Placement alteration sqqence")
        


