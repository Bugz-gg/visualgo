from __future__ import annotations

import random

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from visualgo.visu.WorldCanvas.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.control.programState import ProgramState
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
            self.data_area.add_container(CanvasContainer(self, pos, QSize(1, 1),
                                                         ProgramState.resolve_visual_structure(data), name))

        self.data_area.update()

    def get_free_pos(self, size):       
            if not self.data_positions: # Check if there are any existing objects
                # If no objects, place the new object at (0, 0)
                return QPoint(0, 0)

            # Find the rightmost position of the existing objects
            rightmost_pos = max(pos.x() for pos in self.data_positions.values())

            # Calculate the next available position
            next_pos = QPoint(rightmost_pos + 1, 0)

            return next_pos

