import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QGroupBox, QHBoxLayout, QWidget, QPushButton, \
    QVBoxLayout, QLabel
from displayDataStructure import ArrayWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualgo")

        self.array_widget = ArrayWidget([1, 2, 3, 4, 5])

        layout = QVBoxLayout()
        title = QLabel("Test de visualisation")
        title_font = QFont()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        layout.addWidget(self.array_widget)
        controller_layout = QHBoxLayout()

        run_button = QPushButton("Run")

        controller_layout.addWidget(run_button)
        controller_layout.addWidget(QPushButton("Step"))
        layout.addLayout(controller_layout)

        # Create a central widget for the QMainWindow and set the layout
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        layout.setStretch(0, 1)
        layout.setStretch(1, 3)
        layout.setStretch(2, 1)

        self.setMinimumSize(QSize(600, 300))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
