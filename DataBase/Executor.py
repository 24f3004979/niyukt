'''
Central Query Execution Unit
Input : Query and Data
Executes with implementing the data sheets
fetch data if reqested
'''
from queue import Queue 
from queue import Empty
from dataclasses import dataclass 
from typing import Optional, Tuple, Any
import sqlite3 as sql 
import threading

execution = Queue()

@dataclass
class Task:
    query: str
    data: Optional[Tuple[Any, ...]] = None
    fetch: bool = False

def CentralExecutor():
    i = 0
    while True:
        print(f"Running CentralExecutor : {i}")
        i += 1
        try:
            task = execution.get(timeout=1)
            print(f"TASK EXECUTION : {task}")
        except Empty as e:
            print(f"Empty Execution : {e}")
            continue
        execution.task_done()
