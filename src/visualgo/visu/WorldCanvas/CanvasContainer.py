from __future__ import annotations

import logging

from PyQt5.QtCore import Qt, QRect, QMargins, QPoint, QSize, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.utils import always_try


class CanvasContainer(WidgetWithZoom):
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

    def set_position_and_zoom(self, world: WorldCanvasWidget):
        local_spacing = world.zoom * world.DOT_SPACING
        adapted_size = self.size * local_spacing
        self.setGeometry(QRect(world.canvas_pos_to_screen_pos(self.start * local_spacing), adapted_size))
        self.zoom = world.zoom
        self.inside_widget.zoom = world.zoom

    @always_try
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(100, 100, 255, 150)))

        inside = self.geometry().marginsRemoved(QMargins(5, 5, 5, 5))
        painter.drawRoundedRect(inside, 10, 10)  # Adjust radius for desired roundness

    # Make the container draggable
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.offset))
