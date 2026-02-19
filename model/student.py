from DataBase.GenericModel import *
from DataBase.repo import *



student_repo = Repo('user')


def existence(student_name):
    anchor_information = ('name', student_name)
    result = student_repo.search(anchor_information)

    if len(result) > 0:
        return True
    else:
        return False


r = existence("Madhav")
print(f"Search Result : {r}")

