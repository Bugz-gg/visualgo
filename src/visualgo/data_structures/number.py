from visualgo.data_structures.data import Status, Data

class Number(Data):

    def __init__(self, value):
        self.value = value
        self.status = Status.CREATED

    def read(self):
        self.status = Status.READ
        return self
    
    def affect(self, value):
        self.value = value
        self.status = Status.AFFECTED
    
    def __lt__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value < other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value < other
        raise TypeError
    
    def __gt__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value > other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value > other
        raise TypeError
    
    def __le__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value <= other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value <= other
        raise TypeError
    
    def __ge__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value >= other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value >= other
        raise TypeError
    
    def __eq__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value == other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value == other
        raise TypeError
    
    def __ne__(self, other):
        if isinstance(other, Number):
            other.status = Status.COMPARED
            self.status = Status.COMPARED
            return self.value == other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.status = Status.COMPARED
            return self.value == other
        raise TypeError