from visualgo.data_structures.data import Data, Status

class Number(Data):

    def __init__(self, value):
        super().__init__()
        self.value = value
        
    # TODO: add typeguards
    # TODO: handle operations between Numbers and integers
        
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __iadd__(self, other):
        return Number(self.value + other.value)
    
    def __sub__(self, other):
        return Number(self.value - other.value)
    
    def __isub__(self, other):
        return Number(self.value - other.value)
    
    def __mul__(self, other):
        return Number(self.value * other.value)
    
    def __imul__(self, other):
        return Number(self.value * other.value)
    
    def __pow__(self, other):
        return Number(self.value ** other.value)
    
    def __eq__(self, other):
        super().set_status(Status.COMPARED)
        if isinstance(other, Number):
            return self.value == other.value
        return False