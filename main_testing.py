import threading
import time 
from DataBase.Executor import *
from DataBase.GenericModel import *

CentralExecutor = Executor()

thread = threading.Thread(target=CentralExecutor.run, daemon=False)
thread.start()

columns = tuple('name,email,password_hash,role'.split(","))
user = GenericModel(CentralExecutor.ExecutionQueue, "user", columns)

vals = tuple('Hii,ugjgog.com,1234,student'.split(","))  # Initiating Repo Done
user.insert(vals)

