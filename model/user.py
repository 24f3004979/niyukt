from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *

class User:
    def __init__(self):
        self.columns = tuple('name,email,password_hash,role'.split(","))
        self.db = GenericModel("user", self.columns)

    def register(self,information):
        '''
        information : tuple with data 
        Registration Procedure
            1. check if user exists > terminate req 
            2. creation request with given info 
            3. send for success and errors
        '''
        if not(len(information) != len(self.columns)):
            return False

        # check if user already exists
        name = information[0]
        print(f"hashed ha ha : {information}")

        if exists(name):
            raise Exception(f"User Already Exists")

        try:
            self.db.insert(information)
        except Exception as e:
            log.error(f"Exception Raised : {e}")
            raise Exception(f"Error Occured at Registration Reason : {e}")
        


# Repo Fetch Requests
user_repo = Repo("user")

def exists(name):
    '''Anchor information for making the search'''
    anchor_information = ("name", name)  # searching with name
    result = user_repo.search(anchor_information)
    if len(result) > 0:
        return True
    else:
        return False

    
