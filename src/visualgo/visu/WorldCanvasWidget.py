import logging
import sys

from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor

from visualgo.visu import CanvasContainer
from visualgo.visu.ZoomableWidget import ZoomableWidget


class WorldCanvasWidget(ZoomableWidget):
    DOT_SPACING = 75

    def __init__(self):
        super().__init__()
        self.current_position: QPoint = QPoint(0, 0)
        self.containers: list[CanvasContainer] = []

    # shorter getters
    @property
    def width(self):
        return self.frameGeometry().width()

    @property
    def height(self):
        return self.frameGeometry().height()

    def _paint_grid(self, painter, dot_size):
        dot_size *= self.zoom
        local_spacing = int(self.DOT_SPACING * self.zoom)

        # Painful, I know
        # The idea is to determine the screen position of the center dot
        # And then shift to the top left of the screen
        # And then start drawing them in the for loop.
        center_dot_pos = self._screen_pos_to_canvas_pos(QPoint(self.width // 2, self.height // 2)) + QPoint(self.current_position.x() % local_spacing, self.current_position.y() % local_spacing)
        top_left_dot_pos = self._canvas_pos_to_screen_pos(center_dot_pos + self._screen_pos_to_canvas_pos(QPoint(0, local_spacing)))
        start = top_left_dot_pos

        for i in range(self.width // local_spacing + 1):
            for j in range(self.height // local_spacing + 1):
                rect = QRectF(start.x() + local_spacing * i, start.y() + local_spacing * j, dot_size, dot_size)
                painter.drawEllipse(rect)

    def _screen_pos_to_canvas_pos(self, screen_pos: QPoint):
        return QPoint(screen_pos.x() - self.width // 2, -screen_pos.y() + self.height // 2)

    def _canvas_pos_to_screen_pos(self, canvas_pos: QPoint):
        return QPoint(canvas_pos.x() + self.width // 2, -canvas_pos.y() + self.height // 2)

    def paintEvent(self, e):
        try:
            painter = QPainter(self)
            brush = QBrush()
            brush.setColor(QColor(100, 100, 255, 150))
            brush.setStyle(Qt.SolidPattern)
            painter.setBrush(brush)
            self._paint_grid(painter, 5)

        except Exception as e:
            logging.error("An error occurred:", exc_info=True)

    # Handle mouse drag click
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            try:
                delta: QPoint = event.pos() - self.drag_start_position
                delta.setY(-delta.y())  # Invert Y movement
                self.current_position += delta
                self.drag_start_position = event.pos()
                self.repaint()
            except Exception as e:
                logging.error("An error occurred:", exc_info=True)
