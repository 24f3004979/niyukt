from .user import *
from config import *

class Company(User):
    def __init__(self):
        super().__init__()
        self.company_data = tuple("company_id,description".split(","))
        self.company = GenericModel("company", self.company_data)

    def initiate(self, information):
        log.info(f"Loading information : {information}")
        print("*" * 100)
        print(f"Debug information : {self.company_data}")

        user_information = information["user"]
        company_information = information["company"]

        try:
            info = self.initiate_user(user_information)
            company_information["company_id"] = info[0]
            print(f"Company Information for initiation : {company_information}")
            if self.company.insert(company_information):
                print(f"Now we might have company insertion working :)")

            return True
        except Exception as e:
            log.error(f"Failed Company Initiation with : {e}")
            raise Exception("Failed User creation")
