from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from visualgo.visu.ZoomableWidget import ZoomableWidget


class CanvasContainer(ZoomableWidget):
    def __init__(self, start_x, start_y, width, height, inside_widget):
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height

        layout = QVBoxLayout()
        layout.addWidget(inside_widget)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges

        # Set the pen color and width
        painter.setPen(Qt.NoPen)

        # Set the brush color and style
        painter.setBrush(QBrush(QColor(100, 100, 255, 150)))

        # Draw the rounded rectangle
        rect = self.rect().adjusted(1, 1, -1, -1)  # Adjust for pen width
        painter.drawRoundedRect(rect, 10, 10)  # Adjust radius for desired roundness

