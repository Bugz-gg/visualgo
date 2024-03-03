from re import *
from typing import Any

class program:
    pass

class program2:
    def __init__(self, program):
        self.program=program
    
    def spliting(self):
        self.split_program=self.program.split("\n")

    def execute(self):
        exec(self.program)

    def execute_line_by_line(self):
        self.spliting()
        for line in self.split_program:
            exec(line)

    def run(self):
        self.execute()

class program4:
    def __init__(self, program):
        self.program=program

    def spliting_lines(self):
        self.split_program=self.program.split("\n")
    
    def concat_lines(self):
        self.compiled = ""
        for line in self.compiled_program:
            self.compiled += line + "\n"

    def compile(self):
        # Dictionary to store variable assignments
        variables = {}
        # List to store functions
        functions = []
        # Translating each line
        self.compiled_program = []
        for line in self.split_program:
            tokens = line.split()
            if len(tokens) >= 3 and tokens[1] == '<-':
                # Variable assignment
                lhs = tokens[0]
                rhs = tokens[2]
                if rhs in variables:
                    rhs = variables[rhs]
                compiled_line = f"self.{lhs} = {rhs}"
                variables[lhs] = f"self.{lhs}"
            else:
                # Other lines, just replace variables
                for var, repl in variables.items():
                    line = line.replace(var, repl)
                compiled_line = line
            self.compiled_program.append(compiled_line)
            #print(self.compiled_program)
    
    def execute(self):
        exec(self.compiled)
    
    def run(self):
        self.spliting_lines()

        self.compile()

        self.concat_lines()
        #print(self.compiled)

        self.execute()



class attribute:
    def __init__(self, value: Any, VISUALIZE=False):
        self.value=value
        self.VISUALIZE=VISUALIZE
        self.count=0
    
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return attribute(self.value + other.value, self.VISUALIZE)
    
    def __mul__(self, other):
        if isinstance(other, attribute):
            return attribute(self.value * other.value, self.VISUALIZE)
        elif isinstance(other, int) or isinstance(other, float):
            return attribute(self.value * other, self.VISUALIZE)
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(other)))
    
    def debug(self):
        print("\n[DEBUG]", type(self).__name__)
        print("value\t\t", self.value)
        print("VISUALIZE\t", self.VISUALIZE)
        print("count\t\t", self.count, "\n")


class program3:
    def __init__(self, clock=0):
        self.clock = clock

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = attribute(__value)
    
    def __getattr__(self, name: str) -> Any:
        if name in self.__dict__:
            return self.__dict__[name].value
        else:
            raise AttributeError(f"'program3' object has no attribute '{name}'")
    
    def debug(self):
        print("\n[DEBUG]", type(self).__name__)
        for attr in self.__dict__:
            self.__dict__[attr].debug()
