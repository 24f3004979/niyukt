'''
Generic Model
Unit for all DB interations and transactions
'''
from endpoint.QueryBuilder import *
import time
from endpoint.Executor import *
from config import *

class GenericModel:
    """
    executor_queue, table_name
    """
    def __init__(self, table_name, columns_names):
        self.qb = QueryBuilder(table_name, columns_names)

    def insert(self, values):
        '''
        values : tuple for requuired data elements
        work : Makes insertion request and executes
        '''
        query = self.qb.insertion()
        try:
            print(f"Geneic model for executor : {query} and {values}")
            executor(query, values)
            return 1
        except Exception as e:
            log.info(f"Exception Occured with {e}")
            return 0 
