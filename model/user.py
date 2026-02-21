from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *

class User:
    def __init__(self):
        columns = 'name,email,password_hash,role'.split(",")
        self.columns = tuple(columns)
        self.db = GenericModel("user", self.columns)

    def register(self, information):
        '''
        information : tuple with data 
        Registration Procedure
            1. check if user exists > terminate req 
            2. creation request with given info 
            3. send for success and errors
        '''
        print(f"Length of columns {self.columns} information : {information}")
        if len(information) != len(self.columns):
            print(f"Lengths Issue failed :()")
            raise Exception(f"Insertion Request is not permitible")

        # check if user already exists
        name = information[0]
        if exists(name):
            raise Exception(f"User Already Exists")

        try:
            self.db.insert(information)
            print(f" Information inserted : {information}")
        except Exception as e:
            log.error(f"Exception Raised : {e}")
            raise Exception(f"Error Occured at Registration Reason : {e}")
        


# Repo Fetch Requests
user_repo = Repo("user")

def exists(name):
    '''Anchor information for making the search'''
    anchor_information = ("name", name)  # searching with name
    result = user_repo.search(anchor_information, "name")
    print(f"Result is {result}")
    if result:
        return True
    else:
        return False

def get_id(name):
    anchor_information = ("name", name)
    result = user_repo.search(anchor_information, "id")
    print(f"Result for id search :{result}")
    return result[0]

    
