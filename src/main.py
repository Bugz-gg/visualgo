from visualgo.flow_control import program
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack

# Initialiser la class program qui permet de faire la sauvergarde.
p = program.Program()
p2 = program.Program()
p3 = program.Program()
# ------------- Test Number ---------------
p.x = Number(5)
p.y = Number(6)
p.z = p.x + p.y
p.x += Number(10)
p.y -= Number(2)
for i in p.historic:
    # Toujours regarder le status avant la value sinon on modifie son status.
    print(i[0], i[1].status, i[1].value)
print("----------------------------------------------------------------")

# -------------- Test Stack ---------------
p2.st = Stack()
p2.st.isEmpty()
p2.st.push(4)
p2.st.pop()
p2.st.size()
p2.st.push(4)
p2.st.push(10)
p2.st.push(-16)
p2.st.pop()
hist2 = p2.historic
print("Stack", hist2)

for i in hist2:
    print(i[0], i[1].status, i[1].value)

# ----------- Fonction MAX -----------------

print("----------------------------------------------------------------")


def max_stack(p):
    p.max_value = Number(float('-inf'))
    while not p.st.isEmpty():
        p.current_value = p.st.pop()
        print(p.current_value)
        p.max_value = max(p.max_value, p.current_value)

    return p.max_value


p3.st = Stack()
p3.st.push(4)
p3.st.push(10)
p3.st.push(-15)
p3.st.push(100)
p3.st.push(7)
p3.st.push(19)

max_stack(p3)
hist3 = p3.historic
print("Stack", hist3)

for i in hist3:
    print(i[0], i[1].status, i[1].value)


p3.visualize()
