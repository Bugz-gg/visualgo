from visualgo.data_structures.array import Array
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.visu.data_structures.cell_widget import CellWidget


class ProgramState:
    def __init__(self, variables_to_display: list[tuple[str, any]] = None):
        # The ProgramState should contain all the variable of the program
        # We could imagine that some variable shouldn't be displayed
        # So we only focus on the variables to display here
        if variables_to_display is None:
            self.variables_to_display: dict[str, any] = {}
            return

        self.variables_to_display: dict[str, any] = {}

        for name, value in variables_to_display:
            self.variables_to_display[name] = self.resolve_visual_structure(value)

    def __str__(self):
        return ", ".join(f"{name}: {value}" for name, value in self.variables_to_display.items())

    @staticmethod
    def resolve_visual_structure(value: Data):
        if isinstance(value, Number):
            return CellWidget(value)
        if isinstance(value, Array):
            return


