from model.studentv2 import *

# Payload
name = "NewUser30"
email = "NewEmail40@email.com"
password = "1234"
selection = "Selectioon Branch"
resume = "Resume for the random student"



information = {
                "user":{
                    "name" : name,
                    "password" : password,
                    "email" : email,
                    "role" : "student",
                    "status" : "active"
                    },
                "student": {
                    "resume" : resume,
                    "branch" : selection
                    }
                }

user_information  = information["user"]

student = Student()

a = student.activate(information)
print(f"Activation output for student : {a}")

