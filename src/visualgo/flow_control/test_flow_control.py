from re import *
from typing import Any
# from PySide2.QtCore import QObject, Signal
import time


class program:
    pass


class program2:
    def __init__(self, program):
        self.program = program

    def spliting(self):
        self.split_program = self.program.split("\n")

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
        self.program = program

    def spliting_lines(self):
        self.split_program = self.program.split("\n")

    def concat_lines(self):
        self.compiled = ""
        for line in self.compiled_program:
            self.compiled += line + "\n"

    def lock(self):
        print("Type c to continue execution...")
        while input() != 'c':
            time.sleep(1)

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
                # We can do a control_func_list and then do if line in control_func_list.
                if line == 'lock()':
                    self.lock()
                    compiled_line = line
                else:
                    # Other lines, just replace variables
                    for var, repl in variables.items():
                        line = line.replace(var, repl)
                    compiled_line = line
            self.compiled_program.append(compiled_line)
            print(self.compiled_program)

    def execute(self):
        exec(self.compiled)

    def run(self):
        self.spliting_lines()

        self.compile()

        self.concat_lines()
        # print(self.compiled)

        self.execute()


class attribute:
    def __init__(self, value: Any, name: str, count=0, VISUALIZE=False, line=0):
        self.value = value
        self.name = name
        self.VISUALIZE = VISUALIZE
        self.count = count
        self.code_line = line

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
            raise TypeError(
                "Unsupported operand type for *: {}".format(type(other)))

    def debug(self):
        print("\n[DEBUG]", type(self).__name__)
        print("Name of attribute ", self.name)
        print("value\t\t", self.value)
        print("VISUALIZE\t", self.VISUALIZE)
        print("count\t\t", self.count)
        print("line of code\t", self.code_line, "\n")


class program3:
    __listattr = {}

    def __init__(self, clock=0):
        self.clock = clock

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name not in self.__listattr:
            self.__dict__[__name] = attribute(__value, __name, 0)
            self.__listattr[__name] = {self.__dict__[
                __name].count: self.__dict__[__name]}
        else:
            self.__dict__[__name] = attribute(
                __value, __name, len(self.__listattr[__name]))
            self.__listattr[__name][self.__dict__[
                __name].count] = self.__dict__[__name]

    def __getattr__(self, name: str) -> Any:
        if name in self.__dict__:
            return self.__dict__[name].value
        else:
            raise AttributeError(
                f"'program3' object has no attribute '{name}'")

    def historic(self, variable: str) -> dict:
        return self.__listattr[variable]

    def debug(self):
        print("\n[DEBUG]", type(self).__name__)
        for attr in self.__dict__:
            self.__dict__[attr].debug()



import sys

class program5:

    def __init__(self):
            self.historic = []

    def update_value(self, name, new_value):
        self.__dict__[name] = new_value

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.update_value(__name, __value)
    


    def debug(self):
        print("\n[DEBUG]", type(self).__name__)
        for attr in self.__dict__:
            self.__dict__[attr].debug()
    
    def custom_instruction(self, frame, event, arg = None):
        snapshot = []
        for attr_name, attr_value in self.__dict__.items():
            if attr_name != "historic":
                snapshot.append(attr_value)
        self.historic.append(snapshot)

        return self.custom_instruction
    

    def open(self):
        sys.settrace(self.custom_instruction)


    def close(self):
        sys.settrace(None)
    

p = program5()


def f(y):
    y += 100
    print("je passe par là : ", p.x)
    p.x = p.x + 5
    return y

def g(x):
    x[0] += 1



def h(x):
    x += 5


p.open()

p.x = 5

h(p.x)


p.close()

print(p.historic)





class iop:
    
    def __init__(self, value = None):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, int):
            return iop(self.value + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'iop' and '{}'".format(type(other).__name__))

class program6:

    def __init__(self):
            self.historic = []

    # def __setattr__(self, __name: str, __value: Any) -> None:
    #         self.__dict__[__name] = iop(__value)

    @property
    def log(self):
        state = []
        for attr_name, attr_value in self.__dict__.items():
            if attr_name != "historic":
                state.append((attr_name, attr_value))
        self.historic.append(state)
    

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value
        self.log

    def __getattr__(self, name: str) -> Any:
        if name in self.__dict__:
            self.log
            return self.__dict__[name].value
        else:
            raise AttributeError(
                f"'program3' object has no attribute '{name}'")


test = program6()

test.x = 28
test.y = 10
test.z = test.x + test.y
test.l = [1, 2, 3, 4]

print(test.z)

print(test.historic)


def f(x, y):
    x += 5
    return x + y

f(test.x, test.y)

print(test.historic)


def plus_one(l):
    for i in range(len(l)):
        l[i] = l[i] + 1

plus_one(test.l)

print(test.historic)




# =====================================================================================

class mutable_int:
    def __init__(self, value) -> None:
        self.value = value
    
    def __add__(self, value):
        if isinstance(value, int):
            self.value += value
            return mutable_int(self.value)
        elif isinstance(value, mutable_int):
            self.value += value.value
            return mutable_int(self.value)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'iop' and '{}'".format(type(value).__name__))


    def __str__(self) -> str:
        return str(self.value)   

x = mutable_int(5)
y = mutable_int(10)

def add(x, y):
    x += y

add(x, y)

print(x)

z = x + y

print(z)



class program7:

    def __init__(self) -> None:
        self.historic = []

    # @property
    # def log(self):
    #     state = []
    #     for attr_name, attr_value in self.__dict__.items():
    #         if attr_name != "historic":
    #             if isinstance(attr_value, mutable_int):
    #                 state.append((attr_name, attr_value.value))
    #             else :
    #                 state.append((attr_name, attr_value))
    #     self.historic.append(state)


    def __setattr__(self, __name: str, __value: Any) -> None:
        if isinstance(__value, int):
            self.__dict__[__name] = mutable_int(__value)
        elif isinstance(__value, mutable_int):
            self.__dict__[__name] = __value
        elif isinstance(__value, list):
            self.__dict__[__name] = __value
        else:
            raise AttributeError("azzd")
        self.log2

    # def __getattr__(self, name: str) -> Any:
    #     self.log
    #     if name in self.__dict__:
    #         return self.__dict__[name].value
    #     else:
    #         raise AttributeError(
    #             f"'program3' object has no attribute '{name}'")
        
    @property
    def log2(self):
        attr = super().__getattribute__("__dict__")
        state = []
        for attr_name in attr:
            if attr_name != "historic":
                if isinstance(attr[attr_name], mutable_int):
                    state.append((attr_name, attr[attr_name].value))
                else :
                    state.append((attr_name, attr[attr_name]))
        if "historic" in attr:
            super().__getattribute__("historic").append(state)

    def __getattribute__(self, __name: str) -> Any:
        super().__getattribute__("log2")
        return super().__getattribute__(__name)
    




p = program7()



p.x = 8


p.y = 10


p.z = p.x + p.y


add(p.x, p.y)



print(p.x, p.y, p.z)
# print(p.historic)


def print_list(l):
    for i in l:
        print(i)

print_list(p.historic)