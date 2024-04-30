from visualgo.data_structures.data import Data,Status
from visualgo.data_structures.number import Number

class Array(Data):
    
    def __init__(self, is_visualisable):
        self.is_visualisable = is_visualisable
        self.data = []
    
    def __setitem__(self, index, value):
        if isinstance(value, Number):
            self.data[index] = Number(value.value)
            self.data[index].status = Status.AFFECTED
        elif isinstance(value, int) or isinstance(value, float):
            self.data[index] = Number(value)
            self.data[index].status = Status.AFFECTED
        else:
            raise ValueError("Cannot assign given type to array cell")
    

