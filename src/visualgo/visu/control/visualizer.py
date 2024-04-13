from __future__ import annotations

import math
import random

from PyQt5.QtCore import QSize, QPoint, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from visualgo.visu.WorldCanvas.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.control.programState import ProgramState
from visualgo.data_structures.number import Number
from visualgo.visu.utils import always_try


# Visualizer role is handle data placement inside the WorldCanvasWidget
class Visualizer(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.data_area: WorldCanvasWidget = WorldCanvasWidget()
        self.data_positions = {}

        self.layout().addWidget(self.data_area)

    @always_try
    def update_data(self, program_state: ProgramState = None):
        self.data_area.clear()  # Clear previous data

        if program_state is None:
            return

        for name, data in program_state.variables_to_display.items():
            try:
                pos = self.data_positions[name]
            except KeyError:
                pos = self.get_free_pos(QSize(1, 1))
                self.data_positions[name] = pos

            print(f"Adding {name} component at {pos}!")
            widget = ProgramState.resolve_visual_structure(data)
            if isinstance(data, Number):
                self.data_area.add_container(CanvasContainer(self, pos, QSize(1, 1),widget, name))
            else:
                size = self.get_minimal_size(widget.sizeHint())
                self.data_area.add_container(CanvasContainer(self, pos, size, widget, name))

        self.data_area.update()
        
    def get_free_pos(self, size):
        # Check if there are any existing objects
        if not self.data_positions:
            # If no objects, place the new object at (0, 0)
            return QPoint(2, 2)

        # Find the total number of objects
        num_objects = len(self.data_positions)

        # Calculate the row and column of the next position
        threshold = 3  # Change the value '3' to the desired threshold
        row = num_objects // threshold
        col = num_objects % threshold

        # Calculate the next position based on the row and column
        next_pos = QPoint(col, row)

        return next_pos
    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(max(width, 1), max(1, height))


