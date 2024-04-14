from __future__ import annotations
import sys

from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, \
    QVBoxLayout, QLabel

from visualgo.data_structures.data import Data
from visualgo.visu.control.programState import ProgramState
from visualgo.visu.control.visualizer import Visualizer


class Controller(QMainWindow):
    def __init__(self, program_name, historic: list[ProgramState]):
        super().__init__()

        # Transform historic into a list of program state ?
        histo_len = len(historic)

        # Convert the historic into a dict ! >:D
        self.program_states = historic

        # Start at state 0
        self.current_state_index = 0

        # DISPLAY SECTION
        self.setWindowTitle("Visualiser Visualgo")
        self.setObjectName("controller")

        # Initialize layouts
        self.main_layout = QVBoxLayout()

        # Main title
        self.set_title(program_name)

        # Content layout : code / data
        self.content_layout = Visualizer()  # set up the visualiser

        self.main_layout.addWidget(self.content_layout)

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
        self.resize(QSize(600, 400))

        # default size at startup
        self.resize(1200, 800)

        # Timer for automatic state advancement
        self.timer = QTimer()
        self.timer.timeout.connect(self.step_next)
        self.timer.setInterval(500)  # 0.5 seconds

    # Handle the title of the window
    def set_title(self, title):
        title = QLabel(title)
        title.setObjectName("title")
        title_font = QFont()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setMaximumHeight(25)  # Restrain wigdet size
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

        # Pause/Resume button
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.toggle_pause)
        self.controller_layout.addWidget(self.pause_button)

        # Current state index display
        self.state_label = QLabel(self.get_state_label_text())
        self.state_label.setObjectName("stateLabel")
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
            self.timer.stop()
            self.pause_button.setText("Restart")
            return
        self.current_state_index += 1
        self.display_current_state()

    def step_previous(self):
        if self.current_state_index <= 0:
            return
        self.current_state_index -= 1
        self.display_current_state()

    def toggle_pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pause_button.setText("Resume")
        else:
            if self.current_state_index >= len(self.program_states) - 1:
                self.current_state_index = 0
                self.display_current_state()
            self.timer.start()
            self.pause_button.setText("Pause")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # load QSS file
    with open("../style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = Controller("Demo visualisation")
    window.show()
    sys.exit(app.exec())