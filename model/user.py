from endpoint.GenericModel import *
from config import *
from endpoint.repo import *
from auth.login import *
from config import *


class User:
    '''
    Handle User information
    1. initiate
        cheks for existence -> initiates
    2. register
        preprocessing pipeline for user informatioin -> register
    '''
    def __init__(self):
        columns = ("name", "email", "password", "status", "role")
        self.db = GenericModel("user", columns)
        self.repo = Repo("user")

    def insert(self, information):
        '''
        information : {} with columns : values for specifics
        Procedure
        check for existing user -> initiate if failed
        return id for the initiated student
        '''
        key = list(information.keys())[0]
        anchor_information = (key, information[key])

        if self.repo.exists(information[key]): # Exist Works with just name
            raise UserExists(information)

        # Initiating User
        try:
            self.db.insert(information)
            print(f'Anchor Information for id fetch : {anchor_information}')
            id = self.repo.fetch(anchor_information, "id")
            print(f"Fetched Id : {id}")
            if id:
                return id
            else:
                raise CoreExecutionFailed("Core Execution Failed as after insertion is is not fetched")
            

        except ExecutionFailed as e:
            return Exception(f"Failed Execution at User with {e}")


class UserExists(Exception):
    def __init__(self,information):
        super().__init__()
        self.information  = information
    def __str__(self):
        return f"User Exists with name "

class CoreExecutionFailed(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
    def __str__(self):
        return f"Exception with core module failior : {self.message}"
