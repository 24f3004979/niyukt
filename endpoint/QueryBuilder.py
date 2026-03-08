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
        self.table = table_name
        self.columns = columns_name # tuple must

    def insertion(self):
        placeholder = ','.join(['?']*len(self.columns))
        print(f"Length for the placeholder : {type(self.columns)}")
        query = f'insert into {self.table}{self.columns} values({placeholder})'
        print(f"Query for Insertion : {query} More debug : placeholder : {placeholder} with col : {self.columns}")
        return query  # insertion Query

    def edit(self,edit_information, anchor_information):
        col = edit_information[0] # colum to edit
        query = f"update {self.table} set {col} = ? where {anchor_information[0]} = ?"
        data = (edit_information[1], anchor_information[1])
        return query, data  # TODO : Extend for mutliple anchor information
    
    def selection(self, anchor_information, required_columns):
        '''
        anchor_ioformation -> [(), ()]
        List for fetching information with multiple [AND] based anchored fetch request
        '''
        base_query = f"select {required_columns} from {self.table} where "
        print(f'Base Query : {base_query}')

        i = 1  # placeholder constraints
        data = []  # Final Execution data list
        condition_strings = []
        for anchor_elem in anchor_information:
            elem = f'({anchor_elem[0]} = ?{i})'
            condition_strings.append(elem)
            data.append(anchor_elem[1])
            i += 1

        condition_string = " and ".join(condition_strings)
        query = base_query + condition_string

        print(f"Query : {query} with data \n : {data}")
        return query, data
