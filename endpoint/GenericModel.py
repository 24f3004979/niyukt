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
    '''
    Input Parameter needs type validations for input flow
    '''
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
                return True
            except Exception as e:
                connection.rollback()
                log.error(f"Generic Model failed for query : {query} with data : {data} Reason : {e}")
                information = (query, data)
                raise ExecutionFailed(f"Generic Model Failed with {e}", information=information)

    def repo_fetch(self, anchor_information, required_columns):
        query, data = self.build_query.selection(anchor_information, required_columns)
        print(f"Repo fetch request : {query, data}")
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, data)
                fetched = cursor.fetchall()
                print(f"Fetch request processed for {anchor_information} result : {fetched}")
                return fetched
            except Exception as e:
                raise Exception(f"Core Generic Model fetch failed with : {e}")



    def insert(self, values):
        '''
        Check Existence with search
            terminate with Existence
        Validate Data entries with columns 
        Try for execution request

        Values : Dictionary with columns as their keys
        '''
        # TODO UPgrade Generic Model for searching DB with given information to execute the creation
        if len(values) != len(self.columns):
            log.warning(f"Terminating Due to Invalid Data type passed for insertion Information : {values} for table {self.table} with columns : {self.columns}")
            return False

        insertion_query = self.build_query.insertion()
        # Checking for existence of given information
        try:
            data = tuple(values[col] for col in self.columns) # insertion order flexible
            if self.execute(insertion_query, data):
                log.info(f"Insertion Executed with {insertion_query} with data : {values}")
                return True
            else:
                raise ExecutionFailed("Generic Model- Executor failed")


        except ExecutionFailed as e:
            log.error(f'Execution Failed at Generic Model : Information > Query : {insertion_query} with data : {data}')
            raise Exception("Core Execution Function Failed")


        except Exception as e:
            log.error(f"Failed at insert of Generic Model with {e}")
            raise Exception(f"Insertion Not working with {e}")

    def update(self, update_information, anchor_information):
        '''
        Making Update to the anchored entry
        Check Existence -> Make Edit -> Finalize with True
        '''
        query, data  = self.build_query.edit(update_information, anchor_information)
        print(f"Query : {query, data}")
        try:
            if self.execute(query, data):
                return True  # Success for the Update opreation
            else:
                log.error(f"Execution Failed at Generic Model with : {query, data}")
        except Exception as e:
            log.error(f"Update information failed with {e}")
            raise Exception(f"Update Query Failed with {e}")

class ExecutionFailed(Exception):
    def __init__(self, message, information):
        super().__init__(message)
        self.message = message
        self.information = information
    def __str__(self):
        return f"DB Execution Failed with {self.message} Information : {self.information}"
