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
    while True:
        print(f"Running Central Executor")
        try:
            task = execution.get(timeout=1)
            print(f"Fetched Task : {task}")
        except Empty:
            print(f"No Task Found :) ")
            continue
        print(f'Executing Dummy task : {task.query}')
        execution.task_done()
