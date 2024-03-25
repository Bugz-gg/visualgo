from visualgo.data_structures.data import Data,Status

class Queue(Data):
    def __init__(self, is_visualisable):
        self.data = []
        self.is_visualisable = is_visualisable
    
    def remove(self):
        assert not self.isEmpty(), "queue is empty"
        return self.data.pop(self.size())
    
    def add(self, value):
        self.data.insert(0, value) 
        assert not self.isEmpty(), "operation failed, queue is empty"
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.data)
    
    def clear(self):
        self.data = []
        assert self.isEmpty(), "queue not empty"
        
        
    
    
    
    