from __future__ import annotations

import math
import random

from PyQt5.QtCore import QSize, QPoint, Qt, QSizeF , QRect
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
    @always_try
    def get_free_pos(self, size):
        # Check if there are any existing objects
        if not self.data_positions:
            # If no objects, place the new object at (0, 0)
            return QPoint(0, 0)

        # Find a position that doesn't overlap with existing widgets
        for y in range(self.data_area.height // self.data_area.DOT_SPACING):
            for x in range(self.data_area.width // self.data_area.DOT_SPACING):
                pos = QPoint(x, y)
                rect = QRect(pos, size)

                if not any(QRect(self.data_positions[name], self.data_sizes[name]).intersects(rect)
                        for name in self.data_positions
                        if self.data_positions[name] is not None):
                    return pos

        # If no free position found, place the widget at the bottom-right corner
        return QPoint(self.data_area.width // self.data_area.DOT_SPACING - size.width(),
                    self.data_area.height // self.data_area.DOT_SPACING - size.height())

        return next_pos
    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(max(width, 1), max(1, height))


