from __future__ import annotations

import math
from math import atan2, sin, cos, pi

from PyQt5.QtCore import QPoint, Qt, QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtCore import QSize, QSizeF
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from visualgo.data_structures.data import Status
from visualgo.data_structures.number import Number
from visualgo.data_structures.tree import Node
from visualgo.visu.WorldCanvas.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.control.programState import ProgramState
from visualgo.visu.data_structures import VisualWidget
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
            if not isinstance(data, Node):
                widget = ProgramState.resolve_visual_structure(data)
                size = self.get_minimal_size(widget.sizeHint())

                try:
                    pos = self.data_positions[name][0]
                    if self.intersects_with_existing(pos, size, exclude=name):
                        # If the updated size causes an overlap, find a new position
                        pos = self.get_free_pos(size, exclude=name)
                except KeyError:
                    pos = self.get_free_pos(size)
                self.data_positions[name] = (pos, size)  # Update the size in the dictionary

                self.data_area.add_container(CanvasContainer(self, pos, size, widget, name))

        self.data_area.update()

    def intersects_with_existing(self, pos, size, exclude=None):
        for name, (existing_pos, existing_size) in self.data_positions.items():
            if name == exclude:
                continue
            if self.rectangles_intersect(pos, size, existing_pos, existing_size):
                return True
        return False

    def get_free_pos(self, size, exclude=None):
        # Check if there are any existing objects
        if not self.data_positions:
            # If no objects, place the new object at (0, 0)
            return QPoint(0, 0)

        # Find a free position that doesn't overlap with existing objects
        threshold = 3  # Change the value '3' to the desired threshold
        row = 0
        col = 0
        while True:
            if col >= threshold:
                col = 0
                row += 1
            next_pos = QPoint(col, row)
            if not self.intersects_with_existing(next_pos, size, exclude):
                return next_pos
            col += 1

    def rectangles_intersect(self, pos1, size1, pos2, size2):
        # Extract coordinates and sizes
        x1, y1 = pos1.x(), pos1.y()
        w1, h1 = size1.width(), size1.height()
        x2, y2 = pos2.x(), pos2.y()
        w2, h2 = size2.width(), size2.height()

        # Calculate the coordinates of the bottom-right points
        r1 = (x1 + w1, y1 - h1)
        r2 = (x2 + w2, y2 - h2)

        # Check if rectangles have area 0
        if x1 == r1[0] or y1 == r1[1] or x2 == r2[0] or y2 == r2[1]:
            return False

        # Check if one rectangle is on the left side of the other
        if x1 >= r2[0] or x2 >= r1[0]:
            return False

        # Check if one rectangle is above the other
        if r1[1] >= y2 or r2[1] >= y1:
            return False

        return True

    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(max(width, 1), max(1, height))
