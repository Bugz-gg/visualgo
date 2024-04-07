from __future__ import annotations

import logging
import random

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QVBoxLayout

from visualgo.visu.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.programState import ProgramState
from visualgo.visu.utils import always_try


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


# Handle the content of the visualizer : Code | Data
class Visualizer(QWidget):
    def __init__(self):
        super().__init__()
        # Possibility to add a label / textEdit zone with the code
        # Could be difficult to retrieve the code tho

        self.code_area = QLabel(demo_code)
        self.code_area.setMaximumWidth(300)  # Restrain wigdet size
        self.code_area.setObjectName("codeLabel")
        self.setLayout(QVBoxLayout())

        self.data_area: WorldCanvasWidget = WorldCanvasWidget()
        self.data_positions = {}

        self.layout().addWidget(self.data_area)

    @always_try
    def update_data(self, program_state: ProgramState = None):
        self.data_area.containers = []  # Clear previous data
        self.data_area.clear()
        # maybe in the future figure some way to keep position and non deleted data ?
        if program_state is None:
            return

        for name, get_value in program_state.variables_to_display.items():
            try:
                pos = self.data_positions[name]
            except KeyError:
                pos = self.get_free_pos(QSize(1, 1))
                self.data_positions[name] = pos

            print(f"Adding {name} component at {pos}!")
            self.data_area.containers.append(CanvasContainer(self, pos, QSize(3, 1), get_value(), name))

        self.data_area.update()

    def get_free_pos(self, size):
        return QPoint(random.randint(-3, 3), random.randint(-3, 3))

