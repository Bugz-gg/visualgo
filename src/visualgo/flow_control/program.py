import sys
from typing import Any
from copy import deepcopy

from PyQt5.QtWidgets import QApplication

from ..data_structures.data import *
from ..data_structures.number import Number
from ..data_structures.stack import Stack
from ..data_structures.array import Array
from ..data_structures.queue import Queue
from ..data_structures.tree import Tree, Node
from ..visu.control.controller import Controller
from ..visu.control.programState import ProgramState


class Program:

    def __init__(self) -> None:
        self.historic: list[ProgramState] = []

    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, list) and __name == 'historic':
            self.__dict__[__name] = __value
        elif isinstance(__value, int):
            self.__dict__[__name] = Number(__value)
        elif isinstance(__value, Number):
            self.__dict__[__name] = __value
        elif isinstance(__value, Stack):
            self.__dict__[__name] = __value
        elif isinstance(__value, Tree):
            self.__dict__[__name] = __value
        elif isinstance(__value, Node):
            self.__dict__[__name] = __value
        else:
            raise AttributeError("Unknown attribute")
        if not __name == "historic" or __name == "log" or __name == "__dict__":
            self.log

    @property
    def log(self):
        attr = super().__getattribute__("__dict__")
        state = {}
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    state[attr_name] = deepcopy(attr[attr_name])
                    if hasattr(attr[attr_name], 'reset_status'):
                        attr[attr_name].reset_status()
        if len(list(filter(lambda x: hasattr(x[1], 'status') and x[1].status != Status.NONE, state.items()))) == 0:
            pass
        elif "historic" in attr:
            super().__getattribute__("historic").append(ProgramState(state))


    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        super().__getattribute__("log")
        return super().__getattribute__(__name)

    def visualize(self, program_name="visualisation"):
        app = QApplication(sys.argv)
        # load QSS file
        with open("visualgo/visu/style.qss", "r") as f:
            app.setStyleSheet(f.read())

        window = Controller(program_name, self.historic)
        window.show()
        sys.exit(app.exec())