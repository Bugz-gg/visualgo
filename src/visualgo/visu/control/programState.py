from visualgo.data_structures.array import Array
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.visu.data_structures.cell_widget import CellWidget


class ProgramState:
    def __init__(self, variables_to_display: dict[str, Data] = None):
        # The ProgramState should contain all the variable of the program
        # We could imagine that some variable shouldn't be displayed
        # So we only focus on the variables to display here

        self.variables_to_display: dict[str, Data] = variables_to_display

    def __str__(self):
        return ", ".join(f"{name}: {value}" for name, value in self.variables_to_display.items())

    @staticmethod
    def resolve_visual_structure(value: Data) -> any:
        if isinstance(value, Number):
            return CellWidget(value)
        if isinstance(value, Array):
            return


