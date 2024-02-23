from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout 
from PyQt5.QtCore import Qt, QRect 
from PyQt5.QtGui import QPainter
class ArrayCellWidget(QWidget):
    def __init__(self, value):
        super().__init__()
        self._value = value
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignCenter, str(self._value))

class ArrayWidget(QWidget):
    def __init__(self, array):
        super().__init__()
        self.array = array

        # Create a grid layout
        layout = QGridLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        self.cellWidgets = []
        for  value in array:
            cellWidget = ArrayCellWidget(value)
            layout.addWidget(cellWidget)  # Change this line to match your desired grid size
            self.cellWidgets.append(cellWidget)

        # Set the layout on the ArrayWidget
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = ArrayWidget([1,2,3,4])
    window.showMaximized()
    app.exec()