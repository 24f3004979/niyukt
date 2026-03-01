'''
Student Model
1. Making student registration hadle with using user Model
2. Requesting user for loging the student entity
3. Updating student table with resume and branch information
'''
from .user import *

class Student():
    '''
    Features
    1. Initiating student user with given information
    2. Update student table with given information 
    3. further functions wit students to add ...
    '''
    def __init__(self):
        super().__init__()
        self.user = User()
        std_columns = tuple("student_id,resume,branch".split(","))
        self.studentdb = GenericModel("student", std_columns)
        
    def activate(self, information):
        '''
        Activation Flow 
        Check Student Exists
        initiate new user
        fail with ease
        '''
        user_information = information["user"]
        student_information = information["student"]

        if self.user.db.repo.exists(user_information["name"]):
            return False # User Exists

        id = self.user.initiate(user_information)
        if id:
            student_information["student_id"] = id
            try:
                if self.studentdb.insert(student_information):
                    return True # Activation Success full
            except Exception as e:
                log.error(f"Failed with {e}")
                raise Exception(f"Failed with student Activation with {e}")


            

        


