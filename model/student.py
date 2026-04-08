
'''
Student Model
1. Making student registration hadle with using user Model
2. Requesting user for loging the student entity
3. Updating student table with resume and branch information
'''
from .user import *
from config import *
from endpoint.repo import *

class Student:
    '''
    Features
    1. Initiating student user with given information
    2. Update student table with given information 
    3. further functions wit students to add ...
    '''
    def __init__(self):
        self.user = User()
        std_columns = tuple("student_id,resume,branch".split(","))
        self.db = GenericModel("student", std_columns)
        self.repo = Repo("student")
        
    def activate(self, information):
        '''
        Activation Flow 
        Check Student Exists
        initiate new user
        fail with ease
        '''
        user_information = information["user"]
        student_information = information["student"]
        # Initiate user 

        
        try:
            id = self.user.insert(user_information)
            student_information["student_id"] = id
            if self.db.insert(student_information):
                return True
            else:
                raise Exception(f"Activation Failed at student table update")

        except UserExists as e:
            log.info("Terminating student creation with user exists")
            raise UserExists("User Exists with given information")
        except Exception as e:
            raise ActivationFailed(f"Student Activation failed with {e}")


class ActivationFailed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
    def __str__(self):
        return f"Student Activation Failed with : {self.message}"
