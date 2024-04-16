import sys
import time
import os
from typing import Any
from copy import deepcopy

from PyQt5.QtWidgets import QApplication

from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack
from visualgo.visu.control.controller import Controller
from visualgo.visu.control.programState import ProgramState
import threading


class Program:

    def __init__(self, file_path="") -> None:
        self.historic: list[ProgramState] = []
        self.async_print_histo()

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

    @ property
    def log(self):
        attr = super().__getattribute__("__dict__")
        state = []
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    state.append(
                        (attr_name, deepcopy(attr[attr_name])))
        if "historic" in attr:
            super().__getattribute__("historic").append(state)

    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        super().__getattribute__("log")
        return super().__getattribute__(__name)

    def visualize(historic, program_name="visualisation"):
        app = QApplication(sys.argv)
        # load QSS file
        with open("visualgo/visu/style.qss", "r") as f:
            app.setStyleSheet(f.read())

        window = Controller(program_name, historic)
        window.show()
        sys.exit(app.exec())

    def async_print_histo(self):
        def async_print_histo():
            while 1:
                print(self.historic, len(self.historic))
                time.sleep(1)
        thread = threading.Thread(target=async_print_histo)
        thread.daemon = True
        thread.start

    @staticmethod
    def wrap_code_in_function(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                code = file.read()

            def execute_code_in_thread():
                exec(code)

            # Execute the function in a thread
            thread = threading.Thread(target=execute_code_in_thread)
            thread.start()
