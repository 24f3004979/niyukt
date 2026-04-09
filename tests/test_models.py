'''
Testing Whole Model Pipeline with Strict Data flow and Checks
'''
from model.user import *
from model.student import *
import random
import pytest
from endpoint.GenericModel import *
from auth.login import *

from model.company import *

def mock_user():
    i = random.randint(-100000,100000)
    user = f"user{i}"
    mail = f"mail{i}"
    return user, mail
'''
def test_generic_model():
    columns = tuple("name,email,password,status,role".split(","))
    g = GenericModel("user", columns)

    user, mail = mock_user()

    values = {
        "name":user,
        "email" : mail,
        "password" : "123",
        "status" : "active",
        "role" : "student"
    }
    insertion_result = g.insert(values)  # Tested insert

    update_info = ("name", "TESLA CO-FOUNDER AND CEO")
    anchor_info = ("name", user)  # Using same user

    update_result = g.update(update_info, anchor_info)

    generic_test = (insertion_result == True) and (update_result == True)
    assert generic_test is True
'''


def test_user_model():
    u = User()
    user, mail = mock_user()
    values = {
        "name": user,
        "email" : mail,
        "password" : "123",
        "status" : "activated",
        "role" : "student"
    }
    
    # USER MODEL RETURNS ID OF INITIATED USER ID
    result = type(u.insert(values)) == int
    assert result is True

def test_student_model():
    s = Student()
    user, mail = mock_user()
    values = {
        "name": user,
        "email" : mail,
        "password" : hash_password("123"),
        "status" : "activated",
        "role" : "student"
    }

    # Student Information
    student_info = {
        "resume" : "Resume",
        "branch" : "Dummy branch"
    }

    information = {
        "user" : values,
        "student" : student_info
    }
    assert s.activate(information) is True

def test_company():
    c = Company()
    user, mail = mock_user()
    values = {
        "name": user,
        "email" : mail,
        "password" : hash_password("123"),
        "role" : "company"
    }

    company_information = {
        "discription" : "Dummy About company"
    }
    info = {
        "user" : values,
        "company": company_information
    }

    assert c.initiate(info) is True
