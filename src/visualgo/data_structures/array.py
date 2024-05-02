from visualgo.data_structures.data import Data,Status
from visualgo.data_structures.number import Number

class Array(Data):
    
    def __init__(self):
        # self.is_visualisable = is_visualisable
        self.value = []
    
    def __setitem__(self, index, value):
        if isinstance(value, Number):
            self.value[index] = Number(value.value)
            self.value[index].status = Status.AFFECTED
        elif isinstance(value, int) or isinstance(value, float):
            self.value[index] = Number(value)
            self.value[index].status = Status.AFFECTED
        else:
            raise ValueError("Cannot assign given type to array cell")
    def append(self, value):
        if isinstance(value, Number):
            self.value.append(Number(value.value))
            self.value[-1].status = Status.AFFECTED
        elif isinstance(value, int) or isinstance(value, float):
            self.value.append(Number(value))
            self.value[-1].status = Status.AFFECTED
        else:
            raise ValueError("Cannot append given type to array")

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.value)    
    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Array):
            return self.value == other.value
        return False    