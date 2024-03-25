from visualgo.data_structures.data import Data,Status

class Stack(Data):
    def __init__(self, is_visualisable):
        self.data = []
        self.is_visualisable = is_visualisable
    
    def pop(self):
        assert not self.IsEmpty(), "stack is empty"
        return self.data.pop(0)
    
    def push(self, value):
        self.data.insert(0, value) 
        assert not self.IsEmpty(), "operation failed, stack is empty"
        
    def isEmpty(self):
        return self.Size() == 0
    
    def size(self):
        return len(self.data)
    
    def clear(self):
        self.data = []
        assert self.IsEmpty(), "stack not empty"
    
    def affect(self, stack):
        assert isinstance(stack, Stack), "r value must but a Stack"
        self.data = stack.data
        self.status = Status.AFFECTED
        
        
    
    
    
    