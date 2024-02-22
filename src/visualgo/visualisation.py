import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy
)
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QFrame

class ArrayVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Array Visualizer")
        self.setWindowIcon(QIcon("icon.png"))  # Optional customization

        self.main_layout = QVBoxLayout(self)

        # Input section
        self.input_label = QLabel("Enter number of cells:")
        self.input_num_cells = QLineEdit()
        self.input_num_cells.setValidator(QtGui.QIntValidator(1, 100))  # Limit input to 1-100

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_array)

        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_label)
        self.input_layout.addWidget(self.input_num_cells)
        self.input_layout.addWidget(self.generate_button)

        # Array display section
        self.array_label = QLabel("Array Visualization:")
        self.array_display = QWidget()  # Placeholder for generated array

        self.array_layout = QHBoxLayout()
        self.array_layout.addWidget(self.array_label)
        self.array_layout.addWidget(self.array_display)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.array_layout)


    def generate_array(self):
        try:
            num_cells = int(self.input_num_cells.text())
        except ValueError:
            return  # Ignore invalid input

        # Clear any existing array display
        if self.array_display.layout() is not None:
            while self.array_display.layout().count():
                child = self.array_display.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Create new array display with number cells
        array_layout = QHBoxLayout()
        for i in range(num_cells):
            cell_widget = QFrame()
            cell_widget.setFrameStyle(QFrame.Box | QFrame.Plain)
            cell_layout = QVBoxLayout(cell_widget)
            cell_label = QLabel(f"{i + 1}")
            cell_layout.addWidget(cell_label)
            cell_widget.setLayout(cell_layout)
            cell_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Set uniform cell size
            array_layout.addWidget(cell_widget)

        self.array_display.setLayout(array_layout)
        self.array_display.layout().update()  # Ensure updates are visible

if __name__ == "__main__":
    app = QApplication(sys.argv)
    visualizer = ArrayVisualizer()
    visualizer.show()
    sys.exit(app.exec_())
