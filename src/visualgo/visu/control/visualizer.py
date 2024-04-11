from __future__ import annotations

import math
import random

from PyQt5.QtCore import QSize, QPoint, Qt
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
            widget = ProgramState.resolve_visual_structure(data)
            size = self.get_minimal_size(widget.sizeHint())
            self.data_area.add_container(CanvasContainer(self, pos, size, widget, name))

        self.data_area.update()

    def get_minimal_size(self, hint: QSize):
        width = math.ceil(hint.width() / self.data_area.DOT_SPACING)
        height = math.ceil(hint.height() / self.data_area.DOT_SPACING)
        return QSize(width, height)

    def get_free_pos(self, size):
        return QPoint(random.randint(-3, 3), random.randint(-3, 3))

