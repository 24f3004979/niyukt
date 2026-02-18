'''
Generic Model
Unit for all DB interations and transactions
'''
from DataBase.QueryBuilder import *
import time

class GenericModel:
    """
    executor_queue, table_name
    """
    def __init__(self, executor_queue, table_name, columns_names):
        self.qb = QueryBuilder(table_name, columns_names)
        self.queue = executor_queue

    def insert(self, values):
        '''
        values : tuple for requuired data elements
        work : Makes insertion request and executes
        '''
        query = self.qb.insertion()

        task = Task(
                query=query,
                data=values
                )
        self.queue.put(task)  # Executor : Creation
