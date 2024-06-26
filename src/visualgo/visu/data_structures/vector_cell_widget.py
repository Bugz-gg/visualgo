from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.VisualWidget import VisualWidget
from visualgo.visu.data_structures.cell_widget import CellWidget
from visualgo.data_structures.tree import Node

class VectorCellWidget(VisualWidget):
    ELEMENT_MARGIN = 10

    def __init__(self, array):
        super().__init__(array.status)
        self.cell_array = [CellWidget(value.get_value()) if isinstance(value, Node) else CellWidget(value) for value in array.value]
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

    def update_zoom(self, new_zoom):
        self.zoom = new_zoom
        for cell in self.cell_array:
            cell.update_zoom(new_zoom)

    def get_flat_data(self):
        return self.cell_array + [self]
