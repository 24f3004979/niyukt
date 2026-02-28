from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *

class User:
    """
    User Functions
    -> Making usefull lockups and loading data from generic for dashboards with filters

    +++  Upgrading features are yet to discover for user model to do 
    Features to implement
    1. sync : For making db sync for the information dictionary
    2. Making lookup loading from the DB
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
            insert_working = self.db.insert(information)
            print(f"Insert part working : {insert_working}")
            anchor_information = ("name", information["name"])
            fetched_info = self.db.repo.search(anchor_information, "*")
            log.info(f"Creation Request Initation Output : {fetched_info}")
            if fetched_info:
                return fetched_info 
            else:
                return False

        except Exception as e:
            log.error(f"User Creation Failed | reason : {e}")
            raise Exception("User creation Failed")

# Authenticate user
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
