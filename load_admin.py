from model.user import *
from auth.login import *

u = User()
info = {
        "name" : "Admin1",
        "email" : "admin@gmail.com",
        "password" : hash_password("1234"),
        "status" : "active",
        "role" : "admin"
        }

u.insert(info)
