from endpoint.GenericModel import *
from endpoint.repo import *
from auth.login import *

class User:
    """
    User Functions
    -> Making usefull lockups and loading data from generic for dashboards with filters

    +++  Upgrading features are yet to discover for user model to do 
    Features to implement
    1. sync : For making db sync for the information dictionary
    2. Making lookup loading from the DB
    """
    def __init__(self):
        columns = 'name,email,password_hash,role'.split(",")
        self.columns = tuple(columns)
        self.db = GenericModel("user", self.columns)
