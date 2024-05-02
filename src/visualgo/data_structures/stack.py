from visualgo.data_structures.data import Data,Status
from visualgo.data_structures.number import Number

class Stack(Data):
    def __init__(self):
        super().__init__()
        self.value = []
    
    def __str__(self):
        return ", ".join(str(val) for val in self.__dict__['value']) + f" {self.status}"
    
    def pop(self):
        super().set_status(Status.READ)
        assert not self.isEmpty(), "stack is empty"
        return self.value.pop(0)
    
    def push(self, value):
        super().set_status(Status.READ)
        if isinstance(value, int):
            self.value.insert(0, Number(value))
        else:
            self.value.insert(0, value)
        
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.value)
    
    def clear(self):
        self.value = []
        assert self.isEmpty(), "stack not empty"
    
    def peep(self):
        assert not self.isEmpty(), "stack is empty"
        return self.value[0]
    
    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Stack):
            return self.value == other.value
        return False
