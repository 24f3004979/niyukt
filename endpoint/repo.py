'''
Unit for Manging Repositoy Fetch requests
Handling mass reading and given fetch request for the given function
''' 
import sqlite3 as sql
from config import *
from endpoint.QueryBuilder import *
import os

path = '/home/madhav/Projects/niyukt/endpoint/db/niyukt.db'

class Repo:
    def __init__(self, table_name):
        self.table = table_name

    def count(self):
        q = f"select count(*) from {self.table}"
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute(q)
            fetch = cursor.fetchone()
            return int(fetch[0])
    def exists(self, name):
        '''Making Existence check with search api of repo'''
        anchor_information = ("name", name)
        search = self.fetch(anchor_information, "name")
        if search:
            log.info(f" Fetch-exists : Found Given Informatioin : {anchor_information}")
            return True
        else:
            log.warning(f" Fetch-exists : Existence Check for given information : {anchor_information}, failed")
            return False
            
    def fetch(self, anchor_information, required="*"):
        query = f'select {required} from {self.table} where {anchor_information[0]} = ?'
        print(f"Fetch query : {query}")

        # Fetch from DB 
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (anchor_information[1], ))
            fetch = cursor.fetchone()  # Getin one Entry
            # Comprehensive fetch analysis
            print(f"Fetch requirements filter : {required.split(",")}")
            if (len(required.split(",")) == 1) and (fetch != None):
                result = fetch[0]
                print(f"result : {result}")
                return result
            if fetch:
                return fetch
            else:
                return False
    def fetch_instance(self, required_columns="*"):
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            query = f"select {required_columns} from {self.table}"
            cursor.execute(query)
            fetch = cursor.fetchall()
            if fetch:
                return fetch
            else:
                log.error(f"Repo failed for fetching information instance for giveen table : {self.table}")
                return False
        

