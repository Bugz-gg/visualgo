from PyQt5.QtCore import Qt, QMargins, QSize
from PyQt5.QtGui import QPainter

from visualgo.data_structures.data import Status
from visualgo.data_structures.number import Number
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.data_states import status_to_color
from visualgo.visu.utils import always_try


class CellWidget(WidgetWithZoom):
    DEFAULT_CELL_SIZE = 30

    def __init__(self, value: Number):
        super().__init__()
        self.status: Status = value.status
        self._value = value.__dict__["value"]

    def sizeHint(self):
        return QSize(self.DEFAULT_CELL_SIZE, self.DEFAULT_CELL_SIZE)

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
        self.setMinimumSize(zoomed_cell_size, zoomed_cell_size)  # cell size
        painter.setBrush(self.color())
        pen = painter.pen()
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(
            self.rect(),
            self.zoomed_float(20),
            self.zoomed_float(20)
        )

        painter.setPen(pen)
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))
