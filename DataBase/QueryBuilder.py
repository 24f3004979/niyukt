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
    status : str = 'pending' # Failed / completed

class QueryBuilder:
    def __init__(self, table_name, columns_name):
        self.table_name = table_name
        self.columns = columns_name # tuple must

    def insertion(self):
        placeholder = ','.join(['?']*len(self.columns))
        query = f'insert into {self.table_name}{self.columns} values({placeholder})'
        return query  # insertion Query 





