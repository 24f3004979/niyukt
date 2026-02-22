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
        self.student_db = GenericModel("student", self.student_data)
        
    def activate(self, information):
        '''
        Initiate user [handle errors]
        setup for student table information
        '''
        user_information = list(information[:3])
        user_information.append("student")
        user_information = tuple(user_information)

        try:
            print(f"USER INFORMATION : {user_information}")
            self.register(user_information) # Raising Core error
            print(f"User information sent form student completed :)")
        except Exception as e:
            log.error(f"Exception at student registration with {e}")
            raise Exception(f"Error Making student {e}")

        # Making Student Table update  requires student ID
        name = information[0]
        id = get_id(name)
        print(f"Fetched student id : {id}")
        student_info = []
        student_info.append(id)
        student_info.extend(information[3:])
        student_info = tuple(student_info)

        print(f"Student Information : {student_info}")
        
        try:
            print(f"Student Information : {student_info}")
            self.student_db.insert(student_info)
        except Exception as e:
            raise Exception(f"Student Information is Not uploaded with {e}")

