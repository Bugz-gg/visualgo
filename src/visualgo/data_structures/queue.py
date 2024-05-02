from visualgo.data_structures.data import Data,Status

class Queue(Data):
    def __init__(self):
        super().__init__()
        self.value = []
    
    def remove(self):
        super().set_status(Status.READ)
        assert not self.isEmpty(), "queue is empty"
        return self.value.pop(self.size() - 1)
    
    def add(self, value):
        super().set_status(Status.READ)
        self.value.insert(0, value) 
        assert not self.isEmpty(), "operation failed, queue is empty"
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.value)
    
    def clear(self):
        self.value = []
        assert self.isEmpty(), "queue not empty"
    
    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Queue):
            return self.value == other.value
        return False    
    
    
    
    