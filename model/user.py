from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *


class User:
    """
    Handeling User Information
    - Initiate User
    - Admin control tools
    - Information fetch routes
    - verification tools
    """
    def __init__(self):
        columns = 'name,email,password,role,status'.split(",")
        self.columns = tuple(columns)
        self.db = GenericModel("user", self.columns)

    def initiate(self, information):
        try:
            if self.db.insert(information):
                k = list(information.keys())[0]
                anchor_information = (k, information[k])
                id = self.db.repo.fetch(anchor_information, "id")
                print(f"Fetched Id Output : {id}")
                if id:
                    return id
                else:
                    raise UserNotCreated("Used Not initiated as fetch failed :)")

        except UserNotCreated as E:
            raise E
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

class UserNotCreated(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.m = message
    def __str__(self):
        return f"User Creation Pipeline is failing with Unexpected Flow Info : {self.m}"
