'''
Testing Whole Model Pipeline with Strict Data flow and Checks
'''
from model.userv2 import *
import random
import pytest
from endpoint.GenericModel import *

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
    assert r is True

def test_user_model():
    u = User()
    user, mail = mock_user()
    values = {
        "name":user,
        "email" : mail,
        "password" : "123",
        "status" : "active",
        "role" : "student"
    }
    working = type(u.initiate(values)) == int 
    assert working is True
