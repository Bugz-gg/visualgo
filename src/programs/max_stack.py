import time

from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack

global p


def max_stack(p):
    p.max_value = Number(float('-inf'))
    while not p.st.isEmpty():
        p.current_value = p.st.pop()
        print(p.current_value)
        p.max_value = max(p.max_value, p.current_value)

    return p.max_value


p.st = Stack()
p.st.push(4)
p.st.push(10)
p.st.push(-15)
p.st.push(100)
p.st.push(7)
p.st.push(19)
for i in range(10):
    print("addinf a", i, "to the stack")
    p.st.push(i)

max_stack(p)
