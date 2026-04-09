'''
Drive handle unit
Simple unit for handleing placement drive
    1. Creation
    2. handle edits
    3. Update DB and sync fetch responses
'''
from endpoint.GenericModel import *
from endpoint.repo import *

class Drive:
    def __init__(self):
        columns = ("company_id", "job_role", "description")
        self.db = GenericModel("placement_drive", columns)
        self.repo = Repo("placement_drive")

    def create(self, information):
        try:
            id = self.db.insert(information)
            if id:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f"Exception Occured during Creation : {e}")
