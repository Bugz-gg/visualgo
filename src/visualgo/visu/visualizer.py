from __future__ import annotations

import logging
import random

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget

from visualgo.visu.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.programState import ProgramState


def always_try(f):
    def decorated(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as ignored:
            logging.error("An error occurred:", exc_info=True)
    return decorated


# Handle the content of the visualizer : Code | Data
class Visualizer(QHBoxLayout):
    def __init__(self, controller: QWidget):
        super().__init__()
        self.controller = controller

        # Possibility to add a label / textEdit zone with the code
        # Could be difficult to retrieve the code tho

        demo_code = """
my_list_variable = List()
my_list_variable.append(1)
my_list_variable.append(2)
my_list_variable.append(3)
max_value = 1
my_tree_variable = Tree(1)
my_tree_variable.addNodes(2, 3)
my_tree_variable.addNodes(4, 5)
        """
        self.code_area = QLabel(demo_code)
        self.code_area.setMaximumWidth(300)  # Restrain wigdet size
        self.code_area.setObjectName("codeLabel")
        self.layout().addWidget(self.code_area)

        self.data_area: WorldCanvasWidget = WorldCanvasWidget()

        self.layout().addWidget(self.data_area)

    @always_try
    def update_data(self, program_state: ProgramState = None):
        self.data_area.containers = []  # Clear previous data
        # maybe in the future figure some way to keep position and non deleted data ?

        if program_state is None:
            return

        for name, get_value in program_state.variables_to_display.items():
            self.data_area.containers.append(CanvasContainer(self.controller, QPoint(random.randint(-5, 5), random.randint(-5, 5)), QSize(3, 3), get_value(), name))
