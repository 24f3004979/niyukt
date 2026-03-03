from .user import *
from config import *

'''
Making good Error handle units with grace failiors
'''

class Company():
    def __init__(self):
        company_data = ("company_id", "description")
        self.db = GenericModel("company", company_data)
        self.user = User()

    def initiate(self, information):
        '''
        Initiation flow
        check exists 
        create with gracing for both table update
        '''
        user_information = information["user"]
        # Making Company Initiation deactivated by deafault
        user_information["status"] = "deactivated"
        company_information = information["company"]

        try:
            id = self.user.insert(user_information)
            company_information["company_id"] = id
            if self.db.insert(company_information):
                    return True
            else:
                    raise Exception(f"Company Insertion failed")
        except UserExists as e:
            raise UserExists("User Exsists with given information")
        except Exception as e:
            raise Exception(f"Company initation Failed with {e}")

