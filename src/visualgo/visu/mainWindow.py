import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QGroupBox, QHBoxLayout, QWidget
from displayDataStructure import ArrayWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualgo")

        # Create a QTextEdit widget
        self.textEdit = QTextEdit()

        # Create a canvas widget and layout in order to adopt the ArrayWidget
        self.canvas =QGroupBox()
        canvasLayout = QHBoxLayout(self.canvas)

        # Add ArrayWidget as a child of the canvas
        self.ArrayWidget = ArrayWidget()
        canvasLayout.addWidget(self.ArrayWidget) # must be added to the layout

        layout = QHBoxLayout()

        layout.addWidget(self.textEdit)
        layout.addWidget(self.canvas)

        layout.setStretch(0, 1)
        layout.setStretch(1, 3)
        # Create a central widget for the QMainWindow and set the layout
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())