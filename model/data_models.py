'''
Basic Data flow Models
    Task : Executor Data flow model
        Making Track of core executor data flow
        Structured for passing query and data with status
'''
from dataclasses import dataclass
from typing import Any


# Basic Fundamental Task class defined for all of the tasks
@dataclass
class Task:
    query : str
    data : Any
    status : str = "pending"


