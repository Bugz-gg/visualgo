import time
from visualgo.data_structures.tree import Node, Tree

global p

# -------------- Test Tree ---------------
p.Mytree = Tree()

# Create the tree nodes
p.root = Node(1)
p.Mytree.set_root(p.root)
p.child1 = Node(2)
p.root.append_left_child(p.child1)
p.child2 = Node(3)
p.root.append_right_child(p.child2)
p.child3 = Node(4)
p.child1.append_left_child(p.child3)
p.child4 = Node(5)
p.child1.append_right_child(p.child4)
p.child5 = Node(6)
p.child1.append_right_child(p.child5)
p.child6 = Node(7)
p.child1.append_right_child(p.child6)