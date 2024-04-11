from PyQt5.QtWidgets import QWidget, QHBoxLayout

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.cell_widget import CellWidget


class VectorCellWidget(WidgetWithZoom):
    def __init__(self, array):
        super().__init__()
        self.cell_array = [CellWidget(value) for value in array]
        self.setObjectName("vectorWidget")  # Set object name for styling

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for cell in self.cell_array:
            layout.addWidget(cell)

            # Set the layout on the ArrayWidget
        self.setLayout(layout)
