from __future__ import annotations

from PyQt5.QtCore import Qt, QRectF, QPoint, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from visualgo.visu.WorldCanvas.ZoomableWidget import ZoomableWidget
from visualgo.visu.utils import always_try


class WorldCanvasWidget(ZoomableWidget):
    DOT_SPACING = 150  # Toy around with this one if you want more or less dot

    def __init__(self):
        super().__init__()
        self.current_position: QPoint = QPoint(0, 0)
        self.containers: list[QWidget] = []
        self.setLayout(QVBoxLayout())

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

    @always_try
    def paintEvent(self, e):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush()
        brush.setColor(QColor(100, 100, 255, 150))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        self._paint_grid(painter, 5)

        for container in self.containers:
            self.layout().addWidget(container)
            container.set_position_and_zoom(self)

    # Handle mouse drag click
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    @always_try
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta: QPoint = event.pos() - self.drag_start_position
            delta.setX(-delta.x())  # invert X for some reason ?
            self.current_position += delta
            self.drag_start_position = event.pos()
            self.repaint()
            for container in self.containers:
                container.move(container.pos() + delta)

    def clear(self):
        self.containers = []
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()  # Hide or delete, deleting breaks going back
                # But I guess hide doesn't clear the memory, so it's a leak until it's fixed
