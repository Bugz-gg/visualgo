from visualgo.data_structures.data import Data,Status

class Stack(Data):
    def __init__(self, is_visualisable):
        self.data = []
    
    def Pop(self):
        assert not self.IsEmpty(), "stack is empty"
        return self.data.pop(0)
    
    def Push(self, value):
        self.data.insert(0, value) 
        assert not self.IsEmpty(), "operation failed, stack is empty"
        
    def IsEmpty(self):
        return self.Size() == 0
    
    def Size(self):
        return len(self.data)
    
    def Clear(self):
        self.data = []
        assert self.IsEmpty(), "stack not empty"
        
        
    
    
    
    