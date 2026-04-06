from endpoint.Executorv1 import *
from threading import Thread
from model.data_models import *


central_executor = Executor()
print(f"Central Executor : {central_executor}")
execution_thread = Thread(
    daemon=False,
    target=central_executor.execution()
)  # Made simple threading setup for central Executor

task = Task(
    query="select * from user",
    data=[]
)

print(f"Adding Task into the task thread")
central_executor.execution_queue.put(task)

