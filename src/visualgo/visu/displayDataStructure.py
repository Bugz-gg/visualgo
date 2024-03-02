from enum import Enum


from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QColor


class DataState(Enum):
    NORMAL = (1, QColor("white"))
    CREATED = (2, QColor("lime green"))
    ACCESSED = (3, QColor("light blue"))
    COMPARED = (4, QColor("light red"))

    def __new__(cls, nb, color):
        entry = object.__new__(cls)
        entry.nb = entry._value_ = nb
        entry.color = color
        return entry


class ArrayCellWidget(QWidget):
    def __init__(self, value, default_state=DataState.NORMAL):
        super().__init__()
        self._value = value
        self.state = default_state

    def set_state(self, state: DataState):
        self.state = state

    def paintEvent(self, event):
        painter = QPainter(self)
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)

        # Set correct background color
        painter.fillRect(self.rect(), self.state.color)
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))


class ArrayWidget(QWidget):
    def __init__(self, array, states: list[DataState] = None):
        super().__init__()
        self.cell_array = [ArrayCellWidget(value) for value in array]
        self.setObjectName("ArrayWidget")  # Set object name for styling

        # set proper state if states are given
        if states is not None:
            for i, state in enumerate(states):
                self.cell_array[i].set_state(state)

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for cell in self.cell_array:
            layout.addWidget(cell)

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
