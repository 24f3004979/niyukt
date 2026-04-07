from endpoint.Executorv1 import *
from threading import Thread
from model.data_models import *

query = "insert into user(name, password, email, role) values(?,?,?,?)"
data = ("IndiaPak", "1234", "student@gmail.com", "student")

e = executor(query,data)
print(f"output : {e}")
