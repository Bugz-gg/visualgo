import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, \
    QVBoxLayout, QLabel

from visualgo.visu.displayDataStructure import ArrayWidget, DataState, ArrayCellWidget
from visualgo.visu.programState import ProgramState
from visualgo.visu.visualizer import Visualizer


class Controller(QMainWindow):
    def __init__(self, program_name):
        super().__init__()

        # DATA SECTION
        # freezing the values is necessary as we need to instantiate new one each time,
        # to ensure that the originals don't get modified
        self.program_states: list[ProgramState] = [
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([])}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1], [DataState.CREATED])}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2], [DataState.NORMAL, DataState.CREATED])}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.CREATED])}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                                  ), "max_value": lambda: ArrayCellWidget(1, DataState.CREATED)}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                                  ), "max_value": lambda: ArrayCellWidget(1, DataState.NORMAL)}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                                  ), "max_value": lambda: ArrayCellWidget(1, DataState.NORMAL),"my_tree_variable": lambda: TreeWidget(TreeNode(1,state=DataState.CREATED))}),
            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                                  ), "max_value": lambda: ArrayCellWidget(1, DataState.NORMAL),"my_tree_variable": lambda: TreeWidget(TreeNode(1, [
        TreeNode(2, state=DataState.CREATED),
        TreeNode(3, state=DataState.CREATED)    
    ]))}),            ProgramState({"my_list_variable":
                              lambda: ArrayWidget([1, 2, 3],
                                                  [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                                  ), "max_value": lambda: ArrayCellWidget(1, DataState.NORMAL),"my_tree_variable": lambda: TreeWidget(TreeNode(1, [
        TreeNode(2,[TreeNode(4, state=DataState.CREATED),TreeNode(5, state=DataState.CREATED)]),
        TreeNode(3)    
    ]))}),
            
        ]
        # Start at state 0
        self.current_state_index = 0

        # DISPLAY SECTION
        self.setWindowTitle("Visualiser Visualgo")

        # Initialize layouts
        self.main_layout = QVBoxLayout()

        # Main title
        self.set_title(program_name)

        # Content layout : code / data
        self.content_layout = Visualizer()  # set up the visualiser
        self.content_layout.update_data(self.program_states[self.current_state_index])  # update it once at beginning
        self.main_layout.addLayout(self.content_layout)

        # Controller layout : mainly buttons
        self.controller_layout = QHBoxLayout()
        self.setup_controller_layout()

        # Set main_layout as the central layout of the QMainWindow
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Give space to the various element of the main layout => Should be handled elsewhere ?
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 3)

        # Set the minimum size, modify as needed
        self.setMinimumSize(QSize(600, 300))

    # Handle the title of the window
    def set_title(self, title):
        title = QLabel(title)
        title_font = QFont()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title)

    # Handle the controls of the visualizer : Run / step / pause?
    def setup_controller_layout(self):
        self.main_layout.addLayout(self.controller_layout)

        # Buttons control
        step_prev_button = QPushButton("<|")
        step_prev_button.clicked.connect(self.step_previous)
        self.controller_layout.addWidget(step_prev_button)

        step_next_button = QPushButton("|>")
        step_next_button.clicked.connect(self.step_next)
        self.controller_layout.addWidget(step_next_button)

        # Current state index display
        self.state_label = QLabel(self.get_state_label_text())
        self.controller_layout.addWidget(self.state_label)

    def get_state_label_text(self):
        return f"{self.current_state_index} / {len(self.program_states) - 1}"

    def display_current_state(self):
        # Update state index
        self.state_label.setText(self.get_state_label_text())

        # update visualisation
        self.content_layout.update_data(self.program_states[self.current_state_index])

    def step_next(self):
        if self.current_state_index >= len(self.program_states) - 1:
            return
        self.current_state_index += 1
        self.display_current_state()

    def step_previous(self):
        if self.current_state_index <= 0:
            return
        self.current_state_index -= 1
        self.display_current_state()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = Controller("Demo visualisation")
    window.show()
    sys.exit(app.exec())
