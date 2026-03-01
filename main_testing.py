from model.user import *

# Payload
name = "Iroot"
email = "emil@j23ranmshabd"
password = "1234"
selection = "random branch is being selected"
resume = "Resume for the random student"



information = {
                "user":{
                    "name" : name,
                    "password" : password,
                    "email" : email,
                    "role" : "company",
                    "status" : "active"
                    },
                "company": {
                    "discription" : selection,
                    "contact_details" : resume
                    }
                }

user_information  = information["user"]

u = User()
user_created = u.initiate_user(user_information)
print(f'User initiation output : {user_created}')
