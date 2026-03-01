from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *


# FIX : make Working end to end reliable generic model working model and abstract models to work with
'''
IMprove Log and data flow for user and generic model for making this app usable-
And developable in future extent
Write tests for the given code to validate on the go with test suit about the project working
'''

class User:
    """
    User Functions
    -> Making usefull lockups and loading data from generic for dashboards with filters

    +++  Upgrading features are yet to discover for user model to do 
    Features to implement
    1. sync : For making db sync for the information dictionary
    2. Making lookup loading from the DB
    Making User as Data Model but class would be required for the further expansion for the code logic
    """
    def __init__(self):
        columns = 'name,email,password,role,status'.split(",")
        self.columns = tuple(columns)
        self.db = GenericModel("user", self.columns)

    def initiate_user(self, information):
        '''
        Initiating User with given information
        Checking with exists or not --> Initiate one with given information
        '''
        # TODO Not requried Generic Model can handle creation with given column information
        try:
            if self.db.insert(information):
                k = list(information.keys())[0]
                anchor_information = (k, information[k])
                id = self.db.repo.fetch(anchor_information, "id")
                if id:
                    return id
                else:
                    return False
        except Exception as e:
            log.error(f"User Creation Failed | reason : {e}")
            print(f"user Failed to load with : {e}")
            raise Exception(f"User creation Failed with reason : {e}")

# user authentication Helper function
def authenticate_user(information):
    user = User()
    anchor_information = ("name", information["name"])
    req = "name,password"
    info = user.db.repo.search(anchor_information, req)
    if (type(info) == tuple) and (len(info) == 2):
        password = info[1]
        plain_pass = information["password"]
        result = authentication(password, plain_pass)
        if result:
            return 1
        else:
            return 2
        
    else:
        log.info(f"User not found with : {information}")
        return 0
