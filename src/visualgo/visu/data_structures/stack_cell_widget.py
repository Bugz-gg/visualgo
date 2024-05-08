from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.VisualWidget import VisualWidget
from visualgo.visu.data_structures.cell_widget import CellWidget


class StackCellWidget(VisualWidget):
    ELEMENT_MARGIN = 10

    def __init__(self, stack):
        super().__init__(stack.status)
        self.cell_array = [CellWidget(value) for value in stack.value]
        self.setObjectName("stackWidget")  # Set object name for styling

        # Create a vertical layout for the StackWidget
        layout = QVBoxLayout()

        # Create a CellWidget for each stack value and add it to the layout
        for cell in self.cell_array:
            layout.addWidget(cell)

        # Set the layout on the StackWidget
        self.setLayout(layout)

    def sizeHint(self):
        width = CellWidget.DEFAULT_CELL_SIZE + self.ELEMENT_MARGIN
        height = max(1, len(self.cell_array)) * 2 * (CellWidget.DEFAULT_CELL_SIZE + self.ELEMENT_MARGIN)
        return QSize(width, height)

    def update_zoom(self, new_zoom):
        self.zoom = new_zoom
        for cell in self.cell_array:
            cell.update_zoom(new_zoom)

    def get_flat_data(self):
        return [self] + self.cell_array
