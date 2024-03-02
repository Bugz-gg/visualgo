

class ProgramState:
    def __init__(self, variables_to_display: dict[str, any] = None):
        # The ProgramState should contain all the variable of the program
        # We could imagine that some variable shouldn't be displayed
        # So we only focus on the variables to display here
        if variables_to_display is None:
            self.variables_to_display: dict[str, any] = {}
        else:
            self.variables_to_display: dict[str, any] = variables_to_display

