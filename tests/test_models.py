'''
Testing Whole Model Pipeline with Strict Data flow and Checks
'''
from model.user import *
from model.student import *
import random
import pytest
from endpoint.GenericModel import *
from auth.login import *

def mock_user():
    i = random.randint(-1000,1000)
    user = f"user{i}"
    mail = f"mail{i}"
    return user, mail

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
    r = g.insert(values)
    print(f"Testing Generic Model with {values}")
    assert r is True

def test_user_model():
    u = User()
    user, mail = mock_user()
    values = {
        "name": user,
        "email" : mail,
        "password" : "123",
        "status" : "active",
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
        "status" : "active",
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

