from visualgo.data_structures.array import Array
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.data_structures.queue import Queue
from visualgo.data_structures.stack import Stack
from visualgo.data_structures.tree import Tree, Node
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom
from visualgo.visu.data_structures.cell_widget import CellWidget
from visualgo.visu.data_structures.stack_cell_widget import StackCellWidget
from visualgo.visu.data_structures.tree_widget import TreeWidget
from visualgo.visu.data_structures.vector_cell_widget import VectorCellWidget


class ProgramState:
    def __init__(self, variables_to_display: dict[str, Data]):
        # The ProgramState should contain all the variable of the program
        # We could imagine that some variable shouldn't be displayed
        # So we only focus on the variables to display here

        self.variables_to_display: dict[str, Data] = variables_to_display

    def __str__(self):
        return ", ".join(f"{name}: {value}" for name, value in self.variables_to_display.items())

    @staticmethod
    def resolve_visual_structure(value: Data) -> WidgetWithZoom:
        """

        This method resolve the visual widget that should be used by an object child of Data.

        Adding a new data structure should imply adding a case below for it to be converted as a VisualWidget.

        Args:
            value: An object inheriting Data.

        Returns: An associated VisualWidget.

        """
        if isinstance(value, Number):
            return CellWidget(value)
        if isinstance(value, Array):
            return VectorCellWidget(value)
        if isinstance(value, Stack):
            return StackCellWidget(value)
        if isinstance(value, Queue):
            return VectorCellWidget(value)
        if isinstance(value, Tree):
            return TreeWidget(value.get_root())  # Pass the root node to TreeWidget
        if isinstance(value, Node):
            return WidgetWithZoom()  # Return an empty WidgetWithZoom for Node instances
        return WidgetWithZoom()


