'''
Student Model
1. Making student registration hadle with using user Model
2. Requesting user for loging the student entity
3. Updating student table with resume and branch information
'''
from .user import *

class Student(User):
    def __init__(self):
        super().__init__()
        self.student_data = tuple("student_id,resume,branch".split(','))
        self.student = GenericModel("student", self.student_data)
        
    def activate(self, information):
        '''
        information -> user:{user_info_dict}, student:{student_info}
        Student Account activation flow
        create user -> Make student table update
        '''
        log.info(f"Loading information for creation : {information}")
        user_information = information["user"]
        student_information = information["student"]
        try:
            self.db.insert(user_information)

            print(f"user creation success full")
            # Creating entries for student 
            name = user_information["name"]  # Dict Way is must
            print(f"Name : {name}")
            anchor_information = ("name", name)
            id = self.db.repo.search(anchor_information, "id")

            # Student information with id being at last but faith
            student_information["student_id"] = id
            print(f"student information : {student_information}")
            self.student.insert(student_information) # Making student update
            print(f"Student creation successfull")
        except Exception as e:
            log.error(f"Exception at Student Creation : {e}")
            raise Exception(f"Student Creation Failed with {e}")

