from typing import Any
from ..data_structures.data import *
from ..data_structures.number import Number
from ..data_structures.stack import Stack


class Program:

    def __init__(self) -> None:
        self.historic = []


    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, list) and __name == 'historic':
            self.__dict__[__name] = __value
        elif isinstance(__value, int):
            self.__dict__[__name] = Number(__value)
        elif isinstance(__value, Number):
            self.__dict__[__name] = __value
        elif isinstance(__value, Stack):
            self.__dict__[__name] = __value
        else:
            raise AttributeError("Unknown attribute")
        self.log


    @property
    def log(self):
        attr = super().__getattribute__("__dict__")
        state = []
        for attr_name in attr:
            if attr_name != "historic":
                if isinstance(attr[attr_name], Data):
                    state.append((attr_name, attr[attr_name]))
        if "historic" in attr:
            super().__getattribute__("historic").append(state)


    def __getattribute__(self, __name: str) -> Any:
        super().__getattribute__("log")
        return super().__getattribute__(__name)
    