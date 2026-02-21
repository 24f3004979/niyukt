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
            executor(query, values)
            return True
        except Exception as e:
            log.error(f"Error : {e}")
            raise Exception(f'Error Occured with : {e}') from e
        

    def edit(self, edit_information, anchor_information):
        '''
        Anchor information : [(id,1222)] / Having multiple anchors
        edit_information ; which_colum = what value ?
        '''
        pass # To build next


