import threading
import time 
from DataBase.Executor import *

thread = threading.Thread(target=CentralExecutor, daemon=False)
thread.start()


for i in range(10):
    t = f'task{i}'
    task = Task(query=t)
    print(f"Adding to the execution queue : {task}")
    execution.put(task)

