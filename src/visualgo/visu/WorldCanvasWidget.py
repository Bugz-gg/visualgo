import logging
import sys

from PyQt5.QtCore import Qt, QRectF, QPoint, QPointF, QRect, QSize, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor, QPaintEvent

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

        # Top left position :D

        start = QPoint(- self.current_position.x() % local_spacing, self.current_position.y() % local_spacing)

        for i in range(self.width // local_spacing + 1):
            for j in range(self.height // local_spacing + 1):
                offset = QPoint(local_spacing * i, local_spacing * j)
                screen_pos = start + offset

                rect = QRectF(screen_pos, QSizeF(dot_size, dot_size))
                painter.drawEllipse(rect)

                # Debug texts
                # world_pos = self._screen_pos_to_canvas_pos(screen_pos)
                # painter.drawText(screen_pos, f"{world_pos.x() // local_spacing}, {world_pos.y() // local_spacing}")

    def screen_pos_to_canvas_pos(self, screen_pos: QPoint):
        return QPoint(screen_pos.x() - self.width // 2, -screen_pos.y() + self.height // 2) + self.current_position

    def canvas_pos_to_screen_pos(self, canvas_pos: QPoint):
        return QPoint(canvas_pos.x() - self.current_position.x() + self.width // 2, -(canvas_pos.y() - self.current_position.y()) + self.height // 2)

    def paintEvent(self, e):
        try:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            brush = QBrush()
            brush.setColor(QColor(100, 100, 255, 150))
            brush.setStyle(Qt.SolidPattern)
            painter.setBrush(brush)
            self._paint_grid(painter, 5)

            for container in self.containers:
                container.set_position_and_zoom(self)
                container.paintEvent(QPaintEvent(container.rect()))
                # painter.drawRect(container.geometry())


            # dummy = QRect(self.canvas_pos_to_screen_pos(self.screen_pos_to_canvas_pos(QPoint(361, 256))), QSize(50, 50))
            # print(self.current_position, file=sys.stderr)
            # painter.drawRect(dummy)

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
                delta.setX(-delta.x())  # invert X for some reason ?
                self.current_position += delta
                self.drag_start_position = event.pos()
                self.repaint()
            except Exception as e:
                logging.error("An error occurred:", exc_info=True)
