import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom


class ZoomableWidget(WidgetWithZoom):
    MIN_SCALE = 0.4
    MAX_SCALE = 2

    ZOOM_DIFF_EPSILON = 0.00001

    def __init__(self, parent=None):
        super().__init__(parent)

    def wheelEvent(self, event):
        # Zoom in or out based on the direction of the mouse scroll
        if event.angleDelta().y() > 0:
            new_zoom = self.zoom * 1.1  # Zoom out
        else:
            new_zoom = self.zoom / 1.1  # Zoom in

        # Limit the scale factor to a reasonable range
        new_zoom = max(self.MIN_SCALE, min(new_zoom, self.MAX_SCALE))
        if new_zoom == self.zoom:
            return

        print(f"Changed zoom {self.zoom} -> {new_zoom}")

        self.zoom = new_zoom

        self.repaint()
