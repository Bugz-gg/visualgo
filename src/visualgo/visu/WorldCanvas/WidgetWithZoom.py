from PyQt5.QtWidgets import QWidget


class WidgetWithZoom(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zoom = 1.0

    def update_zoom(self, new_zoom):
        """
        Set the zoom level of the widget

        Args:
            new_zoom: the new zoom level
        """
        self.zoom = new_zoom

    def zoomed_int(self, value):
        """
        Useful tool function
        Args:
            value: the origin value to be scaled

        Returns: the value scaled to the current zoom, as an int

        """
        return int(value * self.zoom)

    def zoomed_float(self, value):
        """
                Useful tool function
                Args:
                    value: the origin value to be scaled

                Returns: the value scaled to the current zoom, as a float

                """
        return float(value * self.zoom)

    def get_flat_data(self):
        return []
