from visualgo.data_structures.data import Data,Status
import traceback


class Stack(Data):
    def __init__(self, ):
        super().__init__()
        self.value = []
    
    def pop(self):
        assert not self.isEmpty(), "stack is empty"
        return self.value.pop(0)
    
    def push(self, value):
        self.value.insert(0, value) 
        assert not self.isEmpty(), "operation failed, stack is empty"
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.value)
    
    def clear(self):
        self.value = []
        assert self.isEmpty(), "stack not empty"
    
    def affect(self, stack):
        assert isinstance(stack, Stack), "r value must but a Stack"
        self.value = stack.data
        self.status = Status.AFFECTED
    
    def peep(self):
        assert not self.isEmpty(), "stack is empty"
        return self.value[0]
    
    def __eq__(self, other):
        super().set_status(Status.COMPARED)
        if isinstance(other, Stack):
            return self.value == other.value
        return False
    