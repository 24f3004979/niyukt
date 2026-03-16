from model.user import *
from model.placement import *
from auth.login import *

u = User()
info = {
        "name" : "Admin1",
        "email" : "admin@gmail.com",
        "password" : hash_password("1234"),
        "status" : "active",
        "role" : "admin"
        }

'''
Loading Placement drives for admin approval mechaism and admin 
'''

p = Placement()

job = "Data Scientist"

placement_information = {
        "company_id" : 1,
        "job_role" : "Jobing",
        "description" : "We are finding goat with thousand years of experience"
}

jobs = "jhadu,pocha,safai,bartan,padhai,dhulai,kamai".split(",")
for job in jobs:
        placement_information['job_role'] = job
        p.insert(placement_information)
        
