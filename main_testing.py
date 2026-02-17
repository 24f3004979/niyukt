import threading
import time 
from DataBase.Executor import *

thread = threading.Thread(target=CentralExecutor, daemon=True )
thread.start()


for i in range(10):
    t = f'task{i}'
    task = Task(query=t)
    print(f"Task added to the Queue  : {task}")
    execution.put(task)

