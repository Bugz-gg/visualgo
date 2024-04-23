import sys
import time
import os
from typing import Any
from copy import deepcopy

from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot
from PyQt5.QtWidgets import QApplication

from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack
from visualgo.visu.control.controller import Controller
from visualgo.visu.control.programState import ProgramState
import threading


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
        else:
            raise AttributeError("Unknown attribute")
        if not __name == "historic" or __name == "log" or __name == "__dict__":
            self.log()

    def log(self):
        attr = super().__getattribute__("__dict__")
        state = {}
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    x = deepcopy(attr[attr_name])
                    x.frozen = True
                    state[attr_name] = x
                    attr[attr_name].reset_status()
        if len(list(filter(lambda x: x[1].status != Status.NONE, state.items()))) == 0:
            pass
        elif "historic" in attr:
            super().__getattribute__("historic").append(ProgramState(state))
            # Send signal to controller telling historic has grown and wait for signal to continue working

    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        super().__getattribute__("log")
        return super().__getattribute__(__name)

    def visualize(self, program_name="visualisation"):
        pass

    @staticmethod
    def wrap_code_in_function(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                code = file.read()

            p = Program()

            app = QApplication(sys.argv)
            # load QSS file
            with open("visualgo/visu/style.qss", "r") as f:
                app.setStyleSheet(f.read())

            controller = Controller(p, file_path)

            class Worker(QRunnable):
                @pyqtSlot()
                def run(self):
                    exec(code, {"p": p})

            controller.threadpool.start(Worker())

            controller.show()
            sys.exit(app.exec())
