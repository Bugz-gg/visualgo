from enum import Enum
from abc import ABC

class Data(ABC):
    def __init__(self, is_visualisable = False):
        self.is_visualisable = is_visualisable
        self.status = Status.CREATED
        
class Status(Enum):
    NONE = 0
    CREATED = 1
    AFFECTED = 2
    COMPARED = 3
    READ = 4