from endpoint.GenericModel import *
from endpoint.repo import *

class User:
    def __init__(self):
        columns = tuple('name,email,password_hash,role'.split(","))
        self.db = GenericModel("user", columns)



user_repo = Repo("user")
def exists(name):
    anchor_information = ("name", name)
    result = user_repo.search(anchor_information)
    if len(result) > 0:
        return True
    else:
        return False

    
