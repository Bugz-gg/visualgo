import sys
import time
import os
from typing import Any
from copy import deepcopy

from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot, pyqtSignal, QWaitCondition, QMutex, QMutexLocker
from PyQt5.QtWidgets import QApplication

from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack
from visualgo.visu.control.controller import Controller
from visualgo.visu.control.programState import ProgramState
import threading

from visualgo.visu.utils import always_try


class Program:

    def __init__(self, worker) -> None:
        self.historic: list[ProgramState] = []
        self.__dict__["worker"] = worker

    def __setattr__(self, __name: str, __value: Any) -> None:
        print(f"Setting attr {__name} with value {__value}")
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
            print("Logging :D")

    @always_try
    def log(self):
        attr = super().__getattribute__("__dict__")
        state = {}
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    x = deepcopy(attr[attr_name])
                    state[attr_name] = x
                    attr[attr_name].reset_status()
        all_data = []
        for data in state.values():
            all_data += data.get_flat_data()
        if len(list(filter(lambda d: d.status != Status.NONE
                                 and d.status != Status.READ
                                 and d.status != Status.LOOKED_INSIDE,
                           all_data))) == 0:
            pass
        elif "historic" in attr:
            p_state = ProgramState(state)
            super().__getattribute__("historic").append(p_state)
            # Send signal to controller telling historic has grown and wait for signal to continue working
            worker = self.__dict__["worker"]
            worker.wait()

    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        print(f"Getting attr {__name}")
        self.log()
        return super().__getattribute__(__name)

    @staticmethod
    def wrap_code_in_function(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                code = file.read()

            class Worker(QRunnable):
                def __init__(self):
                    super(Worker, self).__init__()
                    self.condition = QWaitCondition()
                    self.mutex = QMutex()

                @pyqtSlot()
                def run(self):
                    exec(code, {"p": p})

                def wait(self):
                    with QMutexLocker(self.mutex):
                        self.condition.wait(self.mutex)

                def resume(self):
                    self.condition.wakeAll()

            worker = Worker()
            p = Program(worker)

            app = QApplication(sys.argv)
            # load QSS file
            with open("visualgo/visu/style.qss", "r") as f:
                app.setStyleSheet(f.read())

            controller = Controller(p, file_path, worker)

            controller.show()
            sys.exit(app.exec())
