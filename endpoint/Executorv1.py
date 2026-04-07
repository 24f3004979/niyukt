import sqlite3 as sql
import os
from queue import Queue
from queue import Empty
from config import *
from model.data_models import * # Core Data flow design

DB_PATH = os.getenv("DB_PATH")

# Making Simpler version of executor function

def executor(query, data=None, type=None):
    '''
    Query : String for Execution with Data if given
    type if return is required
    '''
    with sql.connect(DB_PATH) as connection:
        cursor = connection.cursor()

        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            if type=="v":
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"Central Executor Failed with {e}")

# Making Version for Queue based engine for Testing
class Executor:
    '''
    central Executor
    When no task
        Exit loop
    Auto start thus activation thread would decide the running
    '''
    def __init__(self):
        self.execution_queue = Queue()
    
    def execution(self):
        with sql.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            
            while True:
                print("Running Central Executor Function")
                try:
                    task = self.execution_queue.get()
                    query = task.query
                    data = task.data
                    log.info(f"Task Loaded for Execution : {task}")
                    print(f"Loading Task for Execution")
                    try:
                        # Data given then adds data or not
                        if data:
                            cursor.execute(query, data)
                        else:
                            cursor.execute(query) # Just query
                        connection.commit()
                        task.status = "completed"
                        self.execution_queue.task_done()
                        log.info(f"Task Status : {task.status}")
                        print(f"task status : {task.status}")
                    except Exception as e:
                        connection.rollback()
                        task.status = "failed"
                        log.error(f'Central Executor Failed')
                        raise Exception(f"Central Executor Failed with {e}")

                except Empty:
                    log.info(f"No Task Alloted")
                    continue
                        
                except Exception as e:
                    log.warning(f"Executor failed with task : {task} with Exception : {e}")
