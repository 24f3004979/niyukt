'''
Central Query Execution Unit
Input : Query and Data
Executes with implementing the data sheets
fetch data if reqested
'''
from queue import Queue 
from queue import Empty
import sqlite3 as sql 
from config import *
import os

'''
Making Simpler Version of Executor for simplification
+ Potential Theading Issue of sqlite3 due to Multi thread request
'''

path = "/home/madhav/Projects/niyukt/endpoint/db/niyukt.db"


def executor(query, data):

    with sql.connect(path) as connection:
        cursor = connection.cursor()

        # Making Executions
        try:
            print(f"Executing Query : {query} with data : {data}")
            cursor.execute(query, data)
            connection.commit()  # Making Final Commit
        except Exception as e:
            log.error(f"Exception Occured Raising Error : {e}")
            connection.rollback()

class Executor:
    def __init__(self):
        self.ExecutionQueue = Queue()

    def run(self):
        with sql.connect('/home/madhav/Projects/niyukt/DataBase/niyukt.db') as connection:
            cursor = connection.cursor()

            while True:
                try:
                    task = self.ExecutionQueue.get()
                    # Making DB-Execution
                    query = task.query 
                    data = task.data 

                    log.info(f"Loading Task for Execution : {task}")

                    try:
                        cursor.execute(query, data)
                        connection.commit()  # DB-LINK
                        task.status = 'completed'
                        self.ExecutionQueue.task_done() # Marks last fetch completed
                    except Exception as e:
                        connection.rollback()
                        task.status = 'failed'
                        log.error(f" Central Execution Failed with : {e}")
                        raise e  # Testing Multiple layer Error Handle

                except Empty:
                    log.info(f"Queue is Empty")
                    continue
                except Exception as e:
                    print(f"Exception Occured as {e}")
                finally:
                    log.info(f"Task Final status : {task.status}")

