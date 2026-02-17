'''
Query Builder for DB interactions
table-fetch : Listing all columns of the table of search

'''
from dataclasses import dataclass 
from typing import Optional, Tuple, Any


@dataclass
class Task:
    query: str
    data: Optional[Tuple[Any, ...]] = None
    fetch: bool = False

class QueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.columns = []

    def fetch_column_info(self):
        return f"PRAGMA table_info({self.table_name})"

    def set_column_info(self, info):
        print(f"Got information for initiation as : {info} ")
        if len(self.columns) == 0:
            self.columns = info # initiating columns



