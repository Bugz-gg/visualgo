from __future__ import annotations

import logging

from PyQt5.QtCore import Qt, QRect, QMargins, QPoint, QSize, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.utils import always_try


class CanvasContainer(QWidget):
    def __init__(self, parent: QWidget, start: QPoint, size: QSizeF, inside_widget: QWidget, container_name: str):
        super().__init__(parent)
        self.start: QPoint = start
        self.size: QSizeF = size

        self.setObjectName("containerWidget")  # Used to set a name for styling

        self.name = QLabel(container_name)
        self.name.setObjectName("containerName")
        self.name.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.layout().addWidget(self.name)
        self.layout().addWidget(inside_widget)
        self.inside_widget = inside_widget
        layout.setStretch(0, 0)
        layout.setStretch(1, 1)  # Give the majority of space to the widget

        self.segment_size = WorldCanvasWidget.DOT_SPACING
        self.zoom = 1.0

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(100, 100, 255, 150)))
        self.painter = painter

    def set_position_and_zoom(self, world: WorldCanvasWidget):
        local_spacing = world.zoom * world.DOT_SPACING
        adapted_size = self.size * local_spacing
        self.setGeometry(QRect(world.canvas_pos_to_screen_pos(self.start * local_spacing), adapted_size))
        self.zoom = world.zoom

    @always_try
    def paintEvent(self, event):
        inside = self.geometry().marginsRemoved(QMargins(5, 5, 5, 5))
        self.painter.drawRoundedRect(inside, 10, 10)  # Adjust radius for desired roundness

    # Make the container draggable
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.offset))


if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("../style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = CanvasContainer(None, QPoint(5, 3), QSize(3, 3), QLabel("Hello world"), "hey")
    window.show()
    app.exec()
