from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.cell_widget import CellWidget


class VectorCellWidget(WidgetWithZoom):
    ELEMENT_MARGIN = 10

    def __init__(self, array):
        super().__init__()
        self.cell_array = [CellWidget(value) for value in array.value]
        self.setObjectName("vectorWidget")  # Set object name for styling

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for cell in self.cell_array:
            layout.addWidget(cell)

            # Set the layout on the ArrayWidget
        self.setLayout(layout)

    # redefine sizeHint to give an estimation
    def sizeHint(self):
        width = max(1, len(self.cell_array)) * 2 * (CellWidget.DEFAULT_CELL_SIZE + self.ELEMENT_MARGIN)
        height = CellWidget.DEFAULT_CELL_SIZE + self.ELEMENT_MARGIN
        return QSize(width, height)
