from endpoint.GenericModel import *
from endpoint.repo import *
from config import *

class Application:

    def __init__(self):
        columns = ("student_id", "drive_id")
        self.db = GenericModel("application", columns)
        self.repo = Repo("application")  # repo fetch service

    def create(self, info):
        try:
            self.db.insert(info)  # Insertion information
            return True # Made application
        except Exception as e:
            log.warning(f"Drive creation failed with {e}")
            return False

    def update(self):
        '''
        Update COde ~
            s : shortlisted
            r : rejected
            p : placed
        '''
        pass # TODO : Make this part
        
