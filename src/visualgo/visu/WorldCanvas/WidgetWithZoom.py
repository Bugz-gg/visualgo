from PyQt5.QtWidgets import QWidget


class WidgetWithZoom(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zoom = 1.0

    def update_zoom(self, new_zoom):
        self.zoom = new_zoom

    def zoomed_int(self, value):
        return int(value * self.zoom)

    def zoomed_float(self, value):
        return float(value * self.zoom)
