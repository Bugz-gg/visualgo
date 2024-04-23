from __future__ import annotations

import math
import random

from PyQt5.QtCore import QSize, QPoint, Qt, QSizeF
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
    def update_data(self, program_state: ProgramState):
        self.data_area.clear()  # Clear previous data

        for name, data in program_state.variables_to_display.items():
            try:
                pos = self.data_positions[name]
            except KeyError:
                pos = self.get_free_pos(QSize(1, 1))
                self.data_positions[name] = pos

            widget = ProgramState.resolve_visual_structure(data)
            if isinstance(data, Number):
                self.data_area.add_container(CanvasContainer(self, pos, QSizeF(1, 1), widget, name))
            else:
                size = self.get_minimal_size(widget.sizeHint())
                self.data_area.add_container(CanvasContainer(self, pos, size, widget, name))

        self.data_area.update()
        
    def get_free_pos(self, size):
        # Check if there are any existing objects
        if not self.data_positions:
            # If no objects, place the new object at (0, 0)
            return QPoint(0, 0)

        # Find the maximum row and column of existing objects
        max_row = max(pos.y() for pos in self.data_positions.values())
        max_col = max(pos.x() for pos in self.data_positions.values())

        # Initialize the next position to (0, 0)
        next_pos = QPoint(0, 0)

        # Iterate through each row
        for row in range(max_row + 1):
            # Iterate through each column
            for col in range(max_col + 1):
                # Check if the current position is already occupied
                if QPoint(col, row) not in self.data_positions.values():
                    # Check if the new widget fits in the current position
                    if self.does_widget_fit(QPoint(col, row), size):
                        next_pos = QPoint(col, row)
                        return next_pos

        # If no suitable position found, place the widget in the next row
        next_pos = QPoint(0, max_row + 1)
        return next_pos

    def does_widget_fit(self, pos, size):
        # Check if the widget fits within the available space
        for x in range(pos.x(), pos.x() + size.width()):
            for y in range(pos.y(), pos.y() + size.height()):
                if QPoint(x, y) in self.data_positions.values():
                    return False
        return True
    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(max(width, 1), max(1, height))


