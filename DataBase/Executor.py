'''
Central Query Execution Unit
Input : Query and Data
Executes with implementing the data sheets
fetch data if reqested
'''
from queue import Queue 
from queue import Empty
import sqlite3 as sql 
import threading

execution_queue = Queue()


# Executor Needs refinement for Just writing to the DB

def CentralExecutor():
    with sql.connect("niyukt.db") as connection:
        cursor = connection.cursor()

        while True:
            try:
                query, data = execution_queue.get()
                cursor.execute(query, data)
                connection.commit()
                
            except Empty:
                print(f"Waiting For task :) ")
                continue
            execution.task_complte()

