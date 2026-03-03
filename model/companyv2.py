from .user import *
from config import *

'''
Making good Error handle units with grace failiors
'''

class Company():
    def __init__(self):
        company_data = ("company_id", "description")
        self.companydb = GenericModel("company", company_data)
        self.user = User()

    def initiate(self, information):
        '''
        Initiation flow
        check exists 
        create with gracing for both table update
        '''
        user_information = information["user"]
        company_information = information["company"]

        # TODO : Existence Check at user level is must required for failing with grace
