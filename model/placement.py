'''
Placement Drive creation utility
'''
from endpoint.GenericModel import *
from endpoint.repo import *

class Placement:
    def __init__(self):
        columns = ("company_id", "job_role", "description")
        self.db = GenericModel("placement_drive", columns)
        self.repo = Repo("placement_drive")

    def insert(self, information):  # FIX : Simple for now verification with other model is required
        key = list(information.keys())[0]
        anchor_information = (key, information[key])
        
        try:
            print(f"Initiating Insertion into placcement drive ")
            self.db.insert(information)
            id = self.repo.fetch(anchor_information, 'id')
            print(f"Fetched Id for the initaition : {id}")
            if id:
                print(f"Got Id for placement Drive created : {id}")
                return id

            else:
                print(f"Failed Insertion")
                raise Exception("Placement drive not initaited")

        except ExecutionFailed as e:
            print(f"Execution Failed for initiating Placement drive as {e}")
        except Exception as e:
            return Exception(f"Exception with initiating placement drive {e}")

