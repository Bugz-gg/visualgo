import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


class ZoomableWidget(QWidget):
    MIN_SCALE = 0.1
    MAX_SCALE = 2

    def __init__(self, parent=None):
        super().__init__(parent)
        self.zoom = 1.0

    def wheelEvent(self, event):
        # Zoom in or out based on the direction of the mouse scroll
        if event.angleDelta().y() > 0:
            self.zoom *= 1.1  # Zoom out
        else:
            self.zoom /= 1.1  # Zoom in

        # Limit the scale factor to a reasonable range
        self.zoom = max(self.MIN_SCALE, min(self.zoom, self.MAX_SCALE))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    zoomable_widget = ZoomableWidget()
    zoomable_widget.show()
    sys.exit(app.exec_())
