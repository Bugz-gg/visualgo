import logging
import sys

from PyQt5.QtCore import Qt, QRect, QRectF, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

from visualgo.visu.CanvasContainer import CanvasContainer
from visualgo.visu.ZoomableWidget import ZoomableWidget


class WorldCanvasWidget(ZoomableWidget):
    DOT_SPACING = 75

    def __init__(self):
        super().__init__()
        self.center_pos: QPoint = QPoint(self.frameGeometry().width() // 2, self.frameGeometry().height() // 2)
        self.containers = []

    # shorter getters
    @property
    def width(self):
        return self.frameGeometry().width()

    @property
    def height(self):
        return self.frameGeometry().height()

    def _paint_grid(self, painter, dot_size):
        dot_size *= self.zoom
        start = self.center_pos - QPoint(self.width // 2, self.height // 2) * self.zoom

        local_spacing = int(self.DOT_SPACING * self.zoom)
        for i in range(self.width // local_spacing):
            for j in range(self.height // local_spacing):
                rect = QRectF(start.x() + local_spacing * i, start.y() + local_spacing * j, dot_size, dot_size)
                painter.drawEllipse(rect)

    def paintEvent(self, e):
        try:
            painter = QPainter(self)
            brush = QBrush()
            brush.setColor(QColor('lightgray'))
            brush.setStyle(Qt.SolidPattern)
            painter.setBrush(brush)
            self._paint_grid(painter, 5)
            for container in self.containers:
                container.repaint()

        except Exception as e:
            logging.error("An error occurred:", exc_info=True)

    # Handle mouse drag click
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            try:
                delta = event.pos() - self.drag_start_position
                self.center_pos += delta
                self.drag_start_position = event.pos()
                self.repaint()
            except Exception as e:
                logging.error("An error occurred:", exc_info=True)


if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = WorldCanvasWidget()
    window.containers.append(CanvasContainer(0, 0, 3, 3, QLabel("Hello world")))
    window.show()
    app.exec()
