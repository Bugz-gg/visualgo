import time
from visualgo.data_structures.tree import Node, Tree
from visualgo.data_structures.queue import Queue
from visualgo.data_structures.array import Array
global p

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
def parcours_en_largeur(p):
    p.result = Array()
    if p.Mytree.get_root() is None:
        return p.result

    p.queue = Queue()
    p.queue.add(p.Mytree.get_root())
    print("Mytree.get_root():", p.Mytree.get_root())
    while not p.queue.isEmpty():
        p.node = p.queue.remove()
        p.result.append(p.node.get_value())
        print("p.node.get_value():", p.node.get_value())

        for p.child in p.node.children:
            p.queue.add(p.child)

    return p.result

p.traversal_result = parcours_en_largeur(p)

print("Level-order traversal:", p.traversal_result)
