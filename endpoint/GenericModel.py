'''
Moduer Upgrade for existing Geenric Model

Working Mechanisms

Main Role : end-point db client for making db operations and fetch request via dedicated handle for abstracting models.

Working and features
    + checking for data flow and informed loging mechanism for easy debug tracing
    + Working data flow and error mechanism for planning work and failior
'''
import sqlite3 as sql
import os
from endpoint.QueryBuilder import *
from config import *
from endpoint.repo import *

# Loading Path for sql operations
path = '/home/madhav/Projects/niyukt/endpoint/db/niyukt.db'

class GenericModel:
    def __init__(self, table_name, columns):
        self.columns = columns
        self.table = table_name
        self.build_query = QueryBuilder(table_name, columns)
        self.repo = Repo(table_name)  # Making all fetch requests

    def execute(self, query, data):
        '''
Checks for validity of data flow for final Executions
        '''
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, data)
                connection.commit()  # :P
                log.info(f"Execute of Generic Model Executed with {query} and data {data}")
            except Exception as e:
                log.error(f"Generic Model failed for query : {query} with data : {data}")
                raise Exception("Invalid Query or DB failed for executoin")

    def insert(self, values):
        '''
        Check Existence with search
            terminate with Existence
        Validate Data entries with columns 
        Try for execution request

        Values : Dictionary with columns as their keys
        '''
        if len(values) != len(self.columns):
            log.warning("Terminating Due to Invalid Data type passed for insertion")
            return False

        insertion_query = self.build_query.insertion()
        # Checking for existence of given information
        name = values["name"]  # hardcoding for simplicity 
        if self.repo.exists(name):  # Embeded for names for now
            log.warning("Terminating insert at Generic Model due to existing data found")
            return False

        try:
            data = tuple(values[col] for col in self.columns) # insertion order flexible
            self.execute(insertion_query, data)
            log.info(f"Insert Executed with {insertion_query} with data : {values}")
            return True
        except Exception as e:
            log.error(f"Failed at insert of Generic Model with {e}")
            return False 

    def update(self, update_information, anchor_information):
        '''
        Making Update to the anchored entry '''
        pass # TODO : TARGET ***

