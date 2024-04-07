from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.visu.data_structures.data_states import DataStates
from visualgo.visu.utils import always_try


class CellWidget(QWidget):
    def __init__(self, value: Number):
        super().__init__()
        self._value = value.value
        self.state = DataStates.from_status(value.get_status())
        self.setFixedSize(30, 30)  # cell size

    def set_state(self, state: DataStates):
        self.state = state

    @always_try
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother edges
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)

        # Calculate the bounding rectangle for the circle
        radius = min(self.width(), self.height()) / 2   # Radius of the circle
        center = self.rect().center()  # Center of the window
        circle_rect = QRectF(center.x() - radius, center.y() - radius, 2 * radius, 2 * radius)

        painter.setBrush(self.state.color)

        # Draw the circle
        painter.drawEllipse(circle_rect)

        # Set correct background color
        # painter.fillRect(self.rect(), self.state.color)
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))

