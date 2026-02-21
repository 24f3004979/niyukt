'''
Unit for Manging Repositoy Fetch requests
'''
import sqlite3 as sql
import os

path = "/home/madhav/Projects/niyukt/endpoint/db/niyukt.db"

class Repo:
    def __init__(self, table_name):
        self.table = table_name

    def search(self, anchor_information, required="*"):
        '''
        anchor_information = (target, value)
        '''
        query = f"select {required} from {self.table} where {anchor_information[0]} = ?"
        with sql.connect(path) as connection:

            data = tuple(anchor_information[1])
            cursor = connection.cursor()
            cursor.execute(query, (anchor_information[1],))

            return cursor.fetchone()

