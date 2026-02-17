'''
Generic Model
Unit for all DB interations and transactions
'''
from DataBase.QueryBuilder import *

class GenericModel:
    """
    executor_queue, table_name
    """
    def __init__(self, executor_queue, table_name):

        self.qb = QueryBuilder(table_name)
        columns_fetch = self.qb.fetch_column_info()
        task = Task(query=columns_fetch, fetch=True)
        info = executor_queue.put(task) # Returned results

        self.qb.set_column_info(info) # Making columns initiation




