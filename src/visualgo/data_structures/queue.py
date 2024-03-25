from visualgo.data_structures.data import Data,Status

class Queue(Data):
    def __init__(self, is_visualisable):
        self.data = []
        self.is_visualisable = is_visualisable
    
    def remove(self):
        assert not self.IsEmpty(), "queue is empty"
        return self.data.pop(self.Size())
    
    def add(self, value):
        self.data.insert(0, value) 
        assert not self.IsEmpty(), "operation failed, queue is empty"
        
    def isEmpty(self):
        return self.Size() == 0
    
    def size(self):
        return len(self.data)
    
    def clear(self):
        self.data = []
        assert self.IsEmpty(), "queue not empty"
        
        
    
    
    
    