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

def valueInRange(value, min_val, max_val):
    return min_val <= value <= max_val

def rectOverlap(pos1, size1, pos2, size2):
    x1, y1 = pos1.x(), pos1.y()
    w1, h1 = size1.width(), size1.height()
    x2, y2 = pos2.x(), pos2.y()
    w2, h2 = size2.width(), size2.height()

    xOverlap = valueInRange(x1, x2, x2 + w2-1) or valueInRange(x2, x1, x1 + w1-1)
    yOverlap = valueInRange(y1, y2, y2 + h2 - 1) or valueInRange(y2, y1, y1 + h1 - 1)

    return xOverlap and yOverlap

# Visualizer role is handle data placement inside the WorldCanvasWidget
class Visualizer(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())

        self.data_area: WorldCanvasWidget = WorldCanvasWidget()
        self.data_positions = {}

        self.layout().addWidget(self.data_area)
    def print_data_positions(self):
        print("Data Positions:")
        for name, (pos, size) in self.data_positions.items():
            print(f"  {name}: Position: ({pos.x()}, {pos.y()}), Size: ({size.width()}, {size.height()})")
    @always_try
    def update_data(self, program_state: ProgramState):
        self.data_area.clear()  # Clear previous data
        print("Updating data------------------------------------------")
        for name, data in program_state.variables_to_display.items():
            widget = ProgramState.resolve_visual_structure(data)
            size = self.get_minimal_size(widget.sizeHint())

            try:
                pos = self.data_positions[name][0]
            except KeyError:
                pos = self.get_free_pos(size)
            self.data_positions[name] = (pos, size)  # Update the size in the dictionary

            self.data_area.add_container(CanvasContainer(self, pos, size, widget, name))
            print(f"Element: {name}, Position: ({pos.x()}, {pos.y()}), Size: ({size.width()}, {size.height()})")
        self.print_data_positions()  # Print the data positions dictionary
        print("Data updated------------------------------------------")
        self.data_area.update()

    def get_free_pos(self, size):
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
            if not self.intersects_with_existing(next_pos, size):
                print("returning next_pos that doesnt intersect ",next_pos)
                return next_pos
            col += 1 
            # print("adding width to col",size.width())
            # print("col now is ",col)

    
    def intersects_with_existing(self, pos, size):
        for existing_pos, existing_size in self.data_positions.values():
            if self.rectangles_intersect(pos, size, existing_pos, existing_size):
                print(f"current pos: {pos.x()},{pos.y()},size  {size.width()},{size.height()}")
                print(f"Intersecting with {existing_pos.x()},{existing_pos.y()},that has a size {existing_size.width()},{existing_size.height()}")
                return True
        return False

    # @always_try
    def rectangles_intersect(self, pos1, size1, pos2, size2):
        return rectOverlap(pos1, size1, pos2, size2)

    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(max(width, 1), max(1, height))


