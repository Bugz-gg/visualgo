from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number


class Node(Data):
    """
    Represents a node in a tree structure.

    :param value: The value of the node.
    :param children: A list of child nodes (optional).
    """
    def __init__(self, value, children = []):
        super().__init__()
        """
        Initializes a new instance of the Node class.

        :param value: The value of the node.
        :param children: A list of child nodes (optional).
        :raises TypeError: If the value is not an instance of int or Number.
        """
        if isinstance(value, int):
            self.value = Number(value)
        elif isinstance(value, Number):
            self.value = value
        else:
            raise TypeError
        
        self.children = []
        for child in children:
            self.append_right_child(child)

    def insert_child(self, child, index):
        """
        Inserts a child node at the specified index.

        :param child: The child node to insert.
        :param index: The index at which to insert the child node.
        :raises IndexError: If the index is out of range.
        :raises TypeError: If the child is not an instance of int, Number, or Node.
        """
        if index < 0 or index > len(self.children):
            raise IndexError
        if isinstance(child, int):
            self.children.insert(index, Node(Number(child)))
        elif isinstance(child, Number):
            self.children.insert(index, Node(child))
        elif isinstance(child, Node):
            self.children.insert(index, child)
        else:
            raise TypeError
        
        self.children[index].status = Status.AFFECTED
              
    def append_left_child(self, child):
        """
        Appends a child node to the left side of the node.

        :param child: The child node to append.
        """
        self.insert_child(child, 0)
        
    def append_right_child(self, child):
        """
        Appends a child node to the right side of the node.

        :param child: The child node to append.
        """
        self.insert_child(child, len(self.children))
    
    def get_children(self, index):
        """
        Retrieves the child node at the specified index.

        :param index: The index of the child node.
        :return: The child node at the specified index.
        :raises IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.children):
            raise IndexError
        self.children[index].status = Status.READ
        return self.children[index]
    
    def get_left_children(self):
        """
        Retrieves the leftmost child node.

        :return: The leftmost child node.
        """
        return self.get_children(0)
    
    def get_right_children(self):
        """
        Retrieves the rightmost child node.

        :return: The rightmost child node.
        """
        return self.get_children(len(self.children) - 1)
    
    def remove_children(self, index):
        """
        Removes the child node at the specified index.

        :param index: The index of the child node to remove.
        :raises IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.children):
            raise IndexError
        del self.children[index]
    
    def remove_left_children(self):
        """
        Removes the leftmost child node.
        """
        self.remove_children(0)

    def remove_right_children(self):
        """
        Removes the rightmost child node.
        """
        self.remove_children(len(self.children) - 1)
    
    def set_children(self, child, index):
        """
        Sets the child node at the specified index.

        :param child: The child node to set.
        :param index: The index at which to set the child node.
        :raises IndexError: If the index is negative.
        :raises TypeError: If the child is not an instance of int, Number, or Node.
        """
        if index < 0:
            raise IndexError

        if index >= len(self.children):
            # Extend the children list if the index is out of range
            self.children.extend([None] * (index - len(self.children) + 1))

        if isinstance(child, int):
            self.children[index] = Node(Number(child))
        elif isinstance(child, Number):
            self.children[index] = Node(child)
        elif isinstance(child, Node):
            self.children[index] = child
        else:
            raise TypeError
    
    def set_left_children(self, child):
        """
        Sets the leftmost child node.

        :param child: The child node to set as the leftmost child.
        """
        self.set_children(child, 0)
    
    def set_right_children(self, child):
        """
        Sets the rightmost child node.

        :param child: The child node to set as the rightmost child.
        """
        if not self.children:
            self.children.append(None)
        self.set_children(child, len(self.children) - 1)

    def get_value(self):
        """
        Retrieves the value of the node.

        :return: The value of the node.
        """
        self.status = Status.READ
        return self.value
    
    def set_value(self, value):
        """
        Sets the value of the node.

        :param value: The new value for the node.
        :raises TypeError: If the value is not an instance of int or Number.
        """
        self.status = Status.AFFECTED
        if isinstance(value, int):
            self.value = Number(value)
        elif isinstance(value, Number):
            self.value = value


class Tree(Data):
    """
    Represents a tree data structure.

    """
    def __init__(self, is_visible=True, root=None):
        """
        Initializes a new instance of the Tree class.

        :param is_visible: Indicates whether the tree is visible (optional, default: True).
        :param root: The root node of the tree (optional, default: None).
        :raises TypeError: If the root is not an instance of Node.
        """
        super().__init__(is_visible)
        if root is None or isinstance(root, Node):
            self.root = root
        else:
            raise TypeError

    def set_root(self, root):
        """
        Sets the root node of the tree.

        :param root: The new root node of the tree.
        :raises TypeError: If the root is not an instance of Node.
        """
        if isinstance(root, Node):
            self.root = root
        else:
            raise TypeError
        
    def get_root(self):
        """
        Retrieves the root node of the tree.

        :return: The root node of the tree.
        """
        return self.root
    def get_flat_data(self):
        """
        Retrieves a flattened representation of the tree.

        :return: A list containing the flattened tree data.
        """
        flat_data = [self]
        self._traverse_tree(self.root, flat_data)
        return flat_data

    def _traverse_tree(self, node, flat_data):
        """
        Recursively traverses the tree and appends the nodes to the flat_data list.
    
        :param node: The current node being traversed.
        :param flat_data: The list to store the flattened tree data.
        """
        if node is None:
            return

        flat_data.append(node)

        for child in node.children:
            self._traverse_tree(child, flat_data)