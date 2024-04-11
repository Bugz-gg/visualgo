from PyQt5.QtWidgets import QWidget


class WidgetWithZoom(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zoom = 1.0

    def zoomed_int(self, value):
        return int(value * self.zoom)
