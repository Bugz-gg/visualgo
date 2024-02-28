import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel
import time 
class ArrayCaseWidget(QWidget):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.setMinimumSize(30, 20)  # Set a minimum size for each case
        self.setStyleSheet("border: 1px solid black")  # Add a border for better visibility
        self.label = QLabel(str(value), self)
        self.label.setAlignment(Qt.AlignCenter)  # Center the text inside the case

        # Add some spacing and set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.setLayout(layout)

    def set_modified_color(self):
        self.setStyleSheet("background-color: yellow; border: 1px solid black")  # Change the background color


class ArrayVisualizationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.array = []
        self.array_widgets = []  # Store references to array case widgets
        self.init_ui()
    def modify_element(self):
            try:
                index = int(self.input_line.text())
                value = 6  # You can modify this based on your requirements
                self.array[index] = value
                self.update_array_widget()
                if 0 <= index < len(self.array_widgets):
                    self.array_widgets[index].set_modified_color()  # Highlight the modified case
            except ValueError:
                self.clear_array_widget()
                self.array_layout.addWidget(QLabel("Invalid input. Please enter a valid integer."))
    def init_ui(self):
        # Create GUI components
        self.input_line = QLineEdit(self)
        self.create_array_button = QPushButton('Create Array', self)
        self.show_array_button = QPushButton('Show Array', self)
        self.modify_element_button = QPushButton('Modify Element', self)
        self.swap_elements_button = QPushButton('Swap Elements', self)
        self.array_layout = QHBoxLayout()

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_line)
        layout.addWidget(self.create_array_button)
        layout.addWidget(self.show_array_button)
        layout.addWidget(self.modify_element_button)
        layout.addWidget(self.swap_elements_button)
        # layout.addWidget(self.text_browser)
        layout.addLayout(self.array_layout)
        self.setLayout(layout)

        # Connect buttons to functions
        self.create_array_button.clicked.connect(self.create_array)
        self.show_array_button.clicked.connect(self.show_array)
        self.modify_element_button.clicked.connect(self.modify_element)
        self.swap_elements_button.clicked.connect(self.swap_elements)

        # Set up the main window
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Array Visualization')
        self.show()

    def create_array(self):
        try:
            size = int(self.input_line.text())
            # size = 10  # Change this to the size of the array you want to create
            self.array = [0] * size
            self.update_array_widget()
        except ValueError:
            self.clear_array_widget()
            self.array_layout.addWidget(QLabel("Invalid input. Please enter a valid integer."))

    def show_array(self):
        self.update_array_widget()

    def update_array_widget(self):
        self.clear_array_widget()
        self.array_widgets = [ArrayCaseWidget(value) for value in self.array]
        for widget in self.array_widgets:
            self.array_layout.addWidget(widget)

    def clear_array_widget(self):
        for i in reversed(range(self.array_layout.count())):
            self.array_layout.itemAt(i).widget().setParent(None)
    def swap_elements(self):
        try:
            index1 = int(self.input_line.text())
            index2 = 0  # Change this to the second index you want to swap with
            self.array[index1], self.array[index2] = self.array[index2], self.array[index1]
            self.update_array_widget()
                    # Set modified color for the swapped elements
            self.array_widgets[index1].setStyleSheet("background-color: purple; border: 1px solid black")
            self.array_widgets[index2].setStyleSheet("background-color: purple; border: 1px solid black")
            self.text_browser.setText(f"Swapped elements at indices {index1} and {index2}: {self.array}")
        except ValueError:
            self.clear_array_widget()
            self.text_browser.setText("Invalid input. Please enter a valid integer.")
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArrayVisualizationApp()
    sys.exit(app.exec_())

