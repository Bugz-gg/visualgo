from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QRect 
from PyQt5.QtGui import QPainter, QPen

class ArrayCellWidget(QWidget):
    def __init__(self, value):
        super().__init__()
        # set value
        self._value = value
        self.setObjectName("ArrayCellWidget")  # Set object name for styling

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw the rectangle with the cell value in it
        painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignCenter, str(self._value))
    
class ArrayWidget(QWidget):
    def __init__(self, array):
        super().__init__()
        self.array = array
        self.setObjectName("ArrayCellWidget")  # Set object name for styling

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for  value in array:
            cellWidget = ArrayCellWidget(value)
            layout.addWidget(cellWidget)  

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