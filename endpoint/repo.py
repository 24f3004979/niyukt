'''
Unit for Manging Repositoy Fetch requests
Handling mass reading and given fetch request for the given function
'''
import sqlite3 as sql
import os

path = '/home/madhav/Projects/niyukt/endpoint/db/niyukt.db'

class Repo:
    def __init__(self, table_name):
        self.table = table_name

    def exists(self, name):
        '''Making Existence check with search api of repo'''
        anchor_information = ("name", name)
        search = self.fetch(anchor_information, "name")
        if search:
            print(f"Search Results : {search}")
            return True
        else:
            print(f"Search Result {search}")
            return False
        
    def fetch(self, anchor_information, required="*"):
        query = f'select {required} from {self.table} where {anchor_information[0]} = ?'

        # Fetch from DB 
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (anchor_information[1], ))
            fetch = cursor.fetchone()  # Getin one Entry
            # Comprehensive fetch analysis
            print(f"Fetch requirements filter : {required.split(",")}")
            if (len(required.split(",")) == 1) and (fetch != None):
                return fetch[0]
            if fetch:
                return fetch
            else:
                return False
