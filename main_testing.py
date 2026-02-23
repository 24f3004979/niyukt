from model.student import *

# Payload
name = "Randomrandom123"
email = "email@random123randomshabd"
password = "1234"
selection = "random branch is being selected"
resume = "Resume for the random student"




information = {
                "user":{
                    "name" : name,
                    "password_hash" : password,
                    "email" : email,
                    "role" : "student"
                    },
                "student": {
                    "branch" : selection,
                    "resume" : resume
                    }
                }

student = Student()
student.activate(information)
