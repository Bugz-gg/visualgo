import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, \
    QVBoxLayout, QLabel

from visualgo.visu.displayDataStructure import ArrayWidget
from visualgo.visu.programState import ProgramState


# Handle the content of the visualizer : Code | Data
class Visualizer(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # Possibility to add a label / textEdit zone with the code
        # Could be difficult to retrieve the code tho

        demo_code = "This is a demo code\nImagine it is real"
        self.code_area = QLabel(demo_code)
        self.layout().addWidget(self.code_area)

        self.data_area = QVBoxLayout()

        self.layout().addLayout(self.data_area)

    def update_data(self, program_state: ProgramState = None):
        # Remove all widgets from the layout
        while self.data_area.count():
            item = self.data_area.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        if program_state is None:
            self.data_area.addWidget(QLabel("Empty environment"))
        else:
            for name, get_value in program_state.variables_to_display.items():
                self.data_area.addWidget(QLabel(name))
                self.data_area.addWidget(get_value())
