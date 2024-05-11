import sys
from PyQt5.QtCore import pyqtProperty, QObject, QPropertyAnimation, QPoint, QRect, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._custom_property = 0
        self.label = QLabel("Custom Widget")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def getCustomProperty(self):
        return self._custom_property

    def setCustomProperty(self, value):
        self._custom_property = value
        self.update()  # Ensure widget is updated when property changes

    # Define custom property using pyqtProperty decorator
    customProperty = pyqtProperty(int, fget=getCustomProperty, fset=setCustomProperty)

    def paintEvent(self, event):
        # Custom painting based on the custom property
        painter = QPainter(self)
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._custom_property))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.resize(200, 200)
    widget.show()

    # Animate the custom property
    animation = QPropertyAnimation(widget, b"customProperty")
    animation.setDuration(2000)  # Animation duration in milliseconds
    animation.setStartValue(0)
    animation.setEndValue(100)
    animation.start()

    sys.exit(app.exec_())