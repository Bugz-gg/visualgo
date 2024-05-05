from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number


class Node(Data):
    def __init__(self, value, children = []):
        super().__init__()

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
        self.insert_child(child, 0)
        
    def append_right_child(self, child):
        self.insert_child(child, len(self.children))
    
    def get_children(self, index):
        if index < 0 or index >= len(self.children):
            raise IndexError
        self.children[index].status = Status.READ
        return self.children[index]
    
    def get_left_children(self):
        return self.get_children(0)
    
    def get_right_children(self):
        return self.get_children(len(self.children) - 1)
    
    def remove_children(self, index):
        if index < 0 or index >= len(self.children):
            raise IndexError
        del self.children[index]
    
    def remove_left_children(self):
        self.remove_children(0)

    def remove_right_children(self):
        self.remove_children(len(self.children) - 1)
    
    def set_children(self, child, index):
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
        self.set_children(child, 0)
    
    def set_right_children(self, child):
        if not self.children:
            self.children.append(None)
        self.set_children(child, len(self.children) - 1)

    def get_value(self):
        self.status = Status.READ
        return self.value
    
    def set_value(self, value):
        self.status = Status.AFFECTED
        if isinstance(value, int):
            self.value = Number(value)
        elif isinstance(value, Number):
            self.value = value


class Tree(Data):
    def __init__(self, is_visible=True, root=None):
        super().__init__(is_visible)
        if root is None or isinstance(root, Node):
            self.root = root
        else:
            raise TypeError

    def set_root(self, root):
        if isinstance(root, Node):
            self.root = root
        else:
            raise TypeError
        
    def get_root(self):
        return self.root
