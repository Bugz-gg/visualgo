import sys
import time
import os
from typing import Any
from copy import deepcopy

from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot, pyqtSignal, QWaitCondition, QMutex, QMutexLocker
from PyQt5.QtWidgets import QApplication

from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.stack import Stack
from visualgo.visu.control.controller import Controller
from visualgo.visu.control.programState import ProgramState
import threading
from visualgo.visu.utils import always_try
from visualgo.data_structures.number import Number
from visualgo.data_structures.array import Array
from visualgo.data_structures.queue import Queue
from visualgo.data_structures.tree import Tree, Node


class Program:

    def __init__(self, worker) -> None:
        self.historic: list[ProgramState] = []
        self.__dict__["worker"] = worker

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.log()  # In some case we need to log before adding the value, this is because of previously added things to
        # containers that were not registered
        if isinstance(__value, list) and __name == 'historic':
            self.__dict__[__name] = __value
        elif isinstance(__value, int):
            n = Number(__value)
            if __name in self.__dict__:
                n.status = Status.AFFECTED
            self.__dict__[__name] = n
        elif isinstance(__value, Number):
            if __name in self.__dict__:
                __value.set_status(Status.AFFECTED)
            self.__dict__[__name] = __value
        elif isinstance(__value, Stack):
            self.__dict__[__name] = __value
        elif isinstance(__value, Tree):
            self.__dict__[__name] = __value
        elif isinstance(__value, Node):
            self.__dict__[__name] = __value
        elif isinstance(__value, Array):
            self.__dict__[__name] = __value
        elif isinstance(__value, Queue):
            self.__dict__[__name] = __value
        else:
            raise AttributeError("Unknown attribute")
        if not __name == "historic" or __name == "log" or __name == "__dict__":
            self.log()

    @always_try
    def log(self):
        """
        Not gonna comment this one cuz fuck it
        """
        attr = super().__getattribute__("__dict__")
        state = {}
        for attr_name in attr:
            if attr_name != "historic" and "historic" in attr:
                if isinstance(attr[attr_name], Data):
                    state[attr_name] = deepcopy(attr[attr_name])

        all_data = []
        for data in state.values():
            all_data += data.get_flat_data()
        if len(list(filter(lambda d: d.status != Status.NONE
                                 and d.status != Status.READ
                                 and d.status != Status.LOOKED_INSIDE,
                           all_data))) == 0:
            pass
        elif "historic" in attr:
            for attr_name in attr:
                if isinstance(attr[attr_name], Data):
                    attr[attr_name].reset_status()
            p_state = ProgramState(state)
            super().__getattribute__("historic").append(p_state)
            # Send signal to controller telling historic has grown and wait for signal to continue working
            worker = self.__dict__["worker"]
            worker.wait()

    def __getattribute__(self, __name: str) -> Any:
        if __name == "historic" or __name == "log" or __name == "__dict__":
            return super().__getattribute__(__name)
        result = super().__getattribute__(__name)
        if isinstance(result, Number):
            result.status = Status.READ
        self.log()
        return result

    @staticmethod
    def visualize(historic, program_name="visualization"):
        """
        Static method to visualize specified data structures through the algorithm run.

        :param historic: Array of *program states* to be visualized.
        :param program_name: String of the name of the visualization window ("visualization" by default).
        """
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
        thread.start()
        
    # Call at the end to ensure that everything is logged
    def end(self):
        self.log()

    @staticmethod
    def wrap_code_in_function(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                code = file.read()
                code += "\np.end()\n"

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
        else:
            print("no file")
