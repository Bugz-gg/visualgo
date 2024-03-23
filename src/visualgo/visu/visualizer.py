import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, \
    QVBoxLayout, QLabel
from visualgo.visu.displayDataStructure import ArrayWidget, DataState, ArrayCellWidget, TreeNode , TreeWidget
from visualgo.visu.programState import ProgramState


class DataWidget(QWidget):
    def __init__(self, name, value, parent=None):
        super().__init__(parent)
        self.name = QLabel(name)
        self.value = value
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.name)
        self.layout().addWidget(self.value)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.offset))


# Handle the content of the visualizer : Code | Data
class Visualizer(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # Possibility to add a label / textEdit zone with the code
        # Could be difficult to retrieve the code tho

        demo_code = """
        my_list_variable = List()
        my_list_variable.append(1)
        my_list_variable.append(2)
        my_list_variable.append(3)
        max_value = 1
        """
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
                self.data_area.addWidget(DataWidget(name, get_value()))
