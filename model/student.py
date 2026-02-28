'''
Student Model
1. Making student registration hadle with using user Model
2. Requesting user for loging the student entity
3. Updating student table with resume and branch information
'''
from .user import *

class Student(User):
    '''
    Features
    1. Initiating student user with given information
    2. Update student table with given information 
    3. further functions wit students to add ...
    '''
    def __init__(self):
        super().__init__()
        self.student_data = tuple("student_id,resume,branch".split(','))
        self.student = GenericModel("student", self.student_data)
        
    def activate(self, information):
        '''
        information -> user:{user_info_dict}, student:{student_info}
        Student Account activation flow
        create user -> Make student table update

        Student Requries flow for initiation due to user requirements but user wont need it can use generic model rather it would be used for fetching other information and user level interactions
        '''
        log.info(f"Loading information for creation : {information}")
        user_information = information["user"]
        student_information = information["student"]
        try:
            info = self.initiate_user(user_information)
            if info:
                student_information["student_id"] = info[0]
            else:
                raise Exception("Something went wrong with student activation")

            self.student.insert(student_information)
        except Exception as e:
            log.error(f"Exception at Student Creation : {e}")
            raise Exception(f"Student Creation Failed with {e}")

