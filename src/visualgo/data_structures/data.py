from enum import Enum
from abc import ABC
import traceback

class Data(ABC):
    
    def __init__(self, is_visualisable=False):
        self.__is_visualisable = is_visualisable
        self.status = Status.CREATED

    
    def set_status(self, status):
        self.status = status
        # print("------------ status has changed for",  self.status, "------------")

    def get_status(self):
        return self.status

    def reset_status(self):
        self.set_status(Status.NONE)
        self.source = []

    # this method use side effect unlike "=" operator which use reference assignment
    # might cause issues elsewhere
    def assign(self, obj):
        self.set_status(Status.AFFECTED)
        self.value = obj.value
class Status(Enum):
    NONE = 0
    CREATED = 1
    AFFECTED = 2
    READ = 3
    LESS_THAN = 4 # used for both < and <=
    GREATER_THAN = 5 # used for both > and >=
    EQUAL = 6 # used for ==
    DIFFERENT = 7 # used for !=
