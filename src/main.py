from visualgo.flow_control import program
from visualgo.data_structures.data import Data
from visualgo.data_structures.number import Number
from visualgo.data_structures.stack import Stack
from visualgo.data_structures.array import Array
from visualgo.data_structures.tree import Tree, Node
from visualgo.visu.data_structures.tree_widget import TreeWidget
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
    print(i)
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
p2.st.pop()
p2.st.pop()
p2.st.push(-16)
hist2 = p2.historic
print("Stack", hist2)

for i in hist2:
    print(i)

# ----------- Fonction MAX -----------------

print("----------------------------------------------------------------")


def max_stack(p):
    p.max_value = Number(float('-inf'))
    while not p.st.isEmpty():
        p.current_value = p.st.pop()
        print(p.current_value)
        p.max_value = max(p.max_value, p.current_value)

    return p.max_value

p3.st2 = Stack()
p3.st2.push(0)
p3.st2.push(1)
p3.x = Number(0)
p3.y = Number(1)
p3.z = p3.x + p3.y
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
    print(i)


# p3.visualize()



# -------------- Test Tree ---------------
p4 = program.Program()
p4.Mytree = Tree()

# Create the tree nodes
p4.root = Node(1)
p4.Mytree.set_root(p4.root)
p4.child1 = Node(2)
p4.root.append_left_child(p4.child1)
child2 = Node(3)
p4.root.append_right_child(child2)
child3 = Node(4)
p4.child1.append_left_child(child3)
child4 = Node(5)
p4.child1.append_right_child(child4)
child5 = Node(6)
p4.child1.append_right_child(child5)
child6 = Node(7)
p4.child1.append_right_child(child6)


# p4.visualize()
# -------------- Test Tree ---------------
def binary_tree_traversal(program):
    def inorder_traversal(node, traversal_order):
        if node is None:
            return
        inorder_traversal(node.get_left_children() if node.children else None, traversal_order)
        # here the adding of values to the array dont get captured until the end of all the recursive calls are finished 
        traversal_order.append(node.get_value())
        inorder_traversal(node.get_right_children() if node.children else None, traversal_order)

    # Create a binary tree
    program.tree = Tree()
    root = Node(1)
    root.append_left_child(Node(2))
    root.append_right_child(Node(3))
    root.get_left_children().append_left_child(Node(4))
    root.get_left_children().append_right_child(Node(5))
    program.tree.set_root(root)

    # Perform inorder traversal
    program.inorder = Array()
    inorder_traversal(program.tree.get_root(), program.inorder)

    return program.inorder
p5 = program.Program()
inorder= binary_tree_traversal(p5)
p5.visualize()
