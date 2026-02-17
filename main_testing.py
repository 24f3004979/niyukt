import threading
import time 
from DataBase.Executor import *
from DataBase.GenericModel import *

thread = threading.Thread(target=CentralExecutor, daemon=False)
thread.start()

# Generic Model

g = GenericModel(execution, "user")

