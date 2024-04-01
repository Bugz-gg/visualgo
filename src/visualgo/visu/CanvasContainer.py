import logging
import sys

from PyQt5.QtCore import Qt, QRect, QMargins, QPoint, QSize, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget


class CanvasContainer(QWidget):
    def __init__(self, parent: QWidget, start: QPoint, size: QSizeF, inside_widget: QWidget):
        super().__init__(parent)
        self.start: QPoint = start
        self.size: QSizeF = size

        layout = QVBoxLayout()
        layout.addWidget(inside_widget)
        self.setLayout(layout)
        self.segment_size = WorldCanvasWidget.DOT_SPACING
        self.zoom = 1.0

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(100, 100, 255, 150)))
        self.painter = painter

    def set_position_and_zoom(self, world: WorldCanvasWidget):
        adapted_size = self.size * world.zoom * world.DOT_SPACING
        self.setGeometry(QRect(world.canvas_pos_to_screen_pos(self.start), adapted_size))
        self.zoom = world.zoom

    def paintEvent(self, event):
        try:

            inside = self.geometry().marginsRemoved(QMargins(5, 5, 5, 5))
            self.painter.drawRoundedRect(inside, 10, 10)  # Adjust radius for desired roundness

        except Exception as e:
            logging.error("An error occurred:", exc_info=True)


if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = CanvasContainer(None, QPoint(5, 3), QSize(3, 3), QLabel("Hello world"))
    window.show()
    app.exec()
