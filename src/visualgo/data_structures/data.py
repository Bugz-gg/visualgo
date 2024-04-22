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

    def set_status(self, status):
        self.status = status
        # print("------------ status has changed for",  self.status, "------------")

    def get_status(self):
        return self.status

    def reset_status(self):
        self.status = self.set_status(Status.NONE)

    def __setattr__(self, name, value):
        stack = traceback.extract_stack()[-2].name
        # print("__setattr__ called on", name, value, stack) # Debug logs
        if name == 'value' and stack != '__init__':
            self.set_status(Status.AFFECTED)
        super().__setattr__(name, value)


class Status(Enum):
    NONE = 0
    CREATED = 1
    AFFECTED = 2
    COMPARED = 3
    READ = 4 
