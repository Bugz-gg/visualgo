import sys

from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.data_states import status_to_color
from visualgo.visu.utils import always_try


class CellWidget(WidgetWithZoom):
    DEFAULT_CELL_SIZE = 30

    def __init__(self, value: Number):
        super().__init__()
        self._value = value.value
        self.status: Status = value.status

    def color(self):
        return status_to_color(self.status)

    @always_try
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother edges
        font = painter.font()
        font.setPointSize(self.zoomed_int(20))
        painter.setFont(font)

        zoomed_cell_size = self.zoomed_int(self.DEFAULT_CELL_SIZE)
        self.setFixedSize(zoomed_cell_size, zoomed_cell_size)  # cell size

        brush = painter.brush()
        brush.setColor(self.color())
        painter.setBrush(brush)

        painter.drawRect(self.rect())

        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))

