from __future__ import annotations

import logging

from PyQt5.QtCore import Qt, QRect, QMargins, QPoint, QSize, QSizeF
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.WorldCanvas.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.utils import always_try


class CanvasContainer(WidgetWithZoom):
    BASE_FONT_SIZE = 30

    def __init__(self, parent: QWidget, start: QPoint, size: QSizeF, inside_widget: WidgetWithZoom, container_name: str):
        super().__init__(parent)
        self.start: QPoint = start
        self.canvas_size: QSizeF = size

        self.setObjectName("containerWidget")  # Used to set a name for styling

        self.font_size = self.get_font_size(len(container_name))

        self.name = QLabel(container_name)
        self.name.setObjectName("containerName")
        self.name.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.layout().addWidget(self.name)
        self.layout().addWidget(inside_widget)
        self.inside_widget: WidgetWithZoom = inside_widget
        layout.setStretch(0, 0)
        layout.setStretch(1, 1)  # Give the majority of space to the widget

        self.segment_size = WorldCanvasWidget.DOT_SPACING

    def get_font_size(self, name_length):

        # with a base font size of 30, about 7 chars fit in 30 px
        # smallest object are cell_widget with 30 px width
        # some can be larger, maybe take advantage of that ?
        font_scaling = 7 / name_length

        # clamp max scaling
        font_scaling = min(1, font_scaling)

        return int(font_scaling * self.BASE_FONT_SIZE)

    def update_zoom(self, new_zoom):
        self.zoom = new_zoom
        self.inside_widget.update_zoom(new_zoom)

    def set_position_and_zoom(self, world: WorldCanvasWidget):
        local_spacing = world.zoom * world.DOT_SPACING
        adapted_size = self.canvas_size * local_spacing
        self.setGeometry(QRect(world.canvas_pos_to_screen_pos(self.start * local_spacing),
                               QSize(int(adapted_size.width()), int(adapted_size.height()))))
        self.update_zoom(world.zoom)
        self.update_name_size()

    def update_name_size(self):
        font = self.name.font()
        font.setPixelSize(self.zoomed_int(self.font_size))
        self.name.setFont(font)
        self.name.setMinimumHeight(self.zoomed_int(30))

    # Make the container draggable
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.offset))
