from model.company import *

# Payload
name = "RandomCpany"
email = "email@r23ranmshabd"
password = "1234"
selection = "random branch is being selected"
resume = "Resume for the random student"




information = {
                "user":{
                    "name" : name,
                    "password_hash" : password,
                    "email" : email,
                    "role" : "company"
                    },
                "company": {
                    "discription" : selection,
                    "contact_details" : resume
                    }
                }

c = Company()
c.initiate(information)
