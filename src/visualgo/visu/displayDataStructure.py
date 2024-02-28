import random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QColor


class ArrayCellWidget(QWidget):
    def __init__(self, value):
        super().__init__()
        self._value = value
        self.is_selected = False

    def toggle_selection(self):
        self.is_selected = not self.is_selected
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)

        if self.is_selected:
            painter.fillRect(self.rect(), QColor("lightblue"))
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))


class ArrayWidget(QWidget):
    def __init__(self, array):
        super().__init__()
        self.cell_array = [ArrayCellWidget(value) for value in array]
        self.setObjectName("ArrayWidget")  # Set object name for styling

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for cell in self.cell_array:
            cellLayout = QVBoxLayout()
            cellLayout.addWidget(cell)
            selection_button = QPushButton("Select me!")
            selection_button.clicked.connect(cell.toggle_selection)
            cellLayout.addWidget(selection_button)
            layout.addLayout(cellLayout)

            # Set the layout on the ArrayWidget
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = ArrayWidget([1, 2, 3, 4])
    window.showMaximized()
    app.exec()
