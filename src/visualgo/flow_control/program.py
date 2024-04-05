from typing import Any
from copy import deepcopy
from ..data_structures.data import *
from ..data_structures.number import Number
from ..data_structures.stack import Stack
count = 0


class Program:

    def __init__(self) -> None:
        self.historic: list[tuple[str, Data]] = []

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
        if not __name == "historic" or __name == "log" or __name == "__dict__":
            self.log

    @property
    def log(self):
        attr = super().__getattribute__("__dict__")
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    super().__getattribute__("historic").append(
                        (attr_name, deepcopy(attr[attr_name])))

    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        super().__getattribute__("log")
        return super().__getattribute__(__name)
