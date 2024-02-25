import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QGroupBox, QHBoxLayout, QWidget
from displayDataStructure import ArrayWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualgo")

        # Create a QTextEdit widget
        self.textEdit = QTextEdit()

        # Create an ArrayWidget
        self.ArrayWidget = ArrayWidget([1,2,3,4,5])

        # Create a horizontal layout for the main window with code left and array right
        layout = QHBoxLayout()

        # Add the widgets to the layout
        layout.addWidget(self.textEdit)
        layout.addWidget(self.ArrayWidget)

        # Make the array takes 3/4 of the window and the code takes 1/4
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