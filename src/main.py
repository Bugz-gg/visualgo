from visualgo.flow_control import program
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack
from visualgo.data_structures.tree import Tree, Node
from visualgo.visu.data_structures.tree_widget import TreeWidget
# Initialiser la class program qui permet de faire la sauvergarde.
p = program.Program()
# p2 = program.Program()
# p3 = program.Program()
# # ------------- Test Number ---------------
# p.x = Number(5)
# p.y = Number(6)
# p.z = p.x + p.y
# p.x += Number(10)
# p.y -= Number(2)
# for i in p.historic:
#     # Toujours regarder le status avant la value sinon on modifie son status.
#     print(i)
# print("----------------------------------------------------------------")

# # -------------- Test Stack ---------------
# p2.st = Stack()
# p2.st.isEmpty()
# p2.st.push(4)
# p2.st.pop()
# p2.st.size()
# p2.st.push(4)
# p2.st.push(10)
# p2.st.push(-16)
# p2.st.pop()
# p2.st.pop()
# p2.st.pop()
# p2.st.push(-16)
# hist2 = p2.historic
# print("Stack", hist2)

# for i in hist2:
#     print(i)

# # ----------- Fonction MAX -----------------

# print("----------------------------------------------------------------")


# def max_stack(p):
#     p.max_value = Number(float('-inf'))
#     while not p.st.isEmpty():
#         p.current_value = p.st.pop()
#         print(p.current_value)
#         p.max_value = max(p.max_value, p.current_value)

#     return p.max_value

# p3.st2 = Stack()
# p3.st2.push(0)
# p3.st2.push(1)
# p3.x = Number(0)
# p3.y = Number(1)
# p3.z = p3.x + p3.y
# p3.st = Stack()
# p3.st.push(4)
# p3.st.push(10)
# p3.st.push(-15)
# p3.st.push(100)
# p3.st.push(7)
# p3.st.push(19)

# max_stack(p3)
# hist3 = p3.historic
# print("Stack", hist3)

# for i in hist3:
#     print(i)


# p3.visualize()


# Initialize the Program class for saving the state
# p = program.Program()

# -------------- Test Tree ---------------
# -------------- Test Tree ---------------
p.tree = Tree()

# Create the tree nodes
p.root = Node(1)
p.child1 = Node(2)
p.child2 = Node(3)
p.child3 = Node(4)
p.child4 = Node(5)

# Set the children of the nodes
p.root.append_left_child(p.child1)
p.root.append_right_child(p.child2)
p.child1.append_left_child(p.child3)
p.child1.append_right_child(p.child4)

# Set the root of the tree
p.tree.set_root(p.root)

# Visualize the tree
p.visualize()
