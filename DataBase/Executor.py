'''
Central Query Execution Unit
Input : Query and Data
Executes with implementing the data sheets
fetch data if reqested
'''
from queue import Queue 
from queue import Empty
import sqlite3 as sql 


class Executor:
    def __init__(self):
        self.ExecutionQueue = Queue()

    def run(self):
        with sql.connect('/home/madhav/Projects/niyukt/DataBase/niyukt.db') as connection:
            cursor = connection.cursor()

            while True:
                try:
                    task = self.ExecutionQueue.get()
                    print(f"Task Fetched {task}")
                    # Making DB-Execution
                    query = task.query 
                    data = task.data 

                    try:
                        cursor.execute(query, data)
                        connection.commit()  # DB-LINK
                        task.status = 'completed'
                        self.ExecutionQueue.task_done() # Marks last fetch completed
                    except Exception as e:
                        connection.rollback()
                        task.status = 'failed'
                        print(f"Error Occured with the core Execution : {e}")
                        raise e  # Testing Multiple layer Error Handle

                except Empty:
                    print(f"No task found")
                    continue
                except Exception as e:
                    print(f"Exception Occured : {e} ")
                finally:
                    print(f"Task Status : {task.status}")


