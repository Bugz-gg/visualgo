from visualgo.data_structures.data import Data, Status


class Number(Data):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return f"{self.__dict__['value']} : {self.status}"

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
