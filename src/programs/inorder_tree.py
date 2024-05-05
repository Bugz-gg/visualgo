import time
from visualgo.data_structures.tree import Node, Tree
from visualgo.data_structures.array import Array
global p
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
inorder= binary_tree_traversal(p)