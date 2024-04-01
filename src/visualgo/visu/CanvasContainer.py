import logging

from PyQt5.QtCore import Qt, QRect, QMargins, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget

from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget


class CanvasContainer(QWidget):
    def __init__(self, parent: QWidget, start: QPoint, width, height, inside_widget):
        super().__init__(parent)
        self.start: QPoint = start
        self.width = width
        self.height = height

        layout = QVBoxLayout()
        layout.addWidget(inside_widget)
        self.setLayout(layout)
        self.segment_size = WorldCanvasWidget.DOT_SPACING

    def paintEvent(self, event, zoom=1, current_pos=QPoint(0, 0)):
        try:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges

            # Set the pen color and width
            painter.setPen(Qt.NoPen)
            local_segment_size = int(zoom * self.segment_size)
            # Set the brush color and style
            painter.setBrush(QBrush(QColor(100, 100, 255, 150)))
            # Draw the rounded rectangle
            rect = QRect(self.start.x() * local_segment_size, self.start.y() * local_segment_size, self.width * local_segment_size, self.height * local_segment_size)
            self.setGeometry(rect)

            inside = rect.marginsRemoved(QMargins(5, 5, 5, 5))
            painter.drawRoundedRect(inside, 10, 10)  # Adjust radius for desired roundness

        except Exception as e:
            logging.error("An error occurred:", exc_info=True)


if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = CanvasContainer(None, QPoint(5, 3), 3, 3, QLabel("Hello world"))
    window.show()
    app.exec()
