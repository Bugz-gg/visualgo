from visualgo.data_structures.data import Data, Status


class Number(Data):

    def __init__(self, value=0):
        super().__init__()
        self.value = value

    def __str__(self):
        return f"{self.__dict__['value']} : {self.status}"

    # TODO: add typeguards
    # TODO: handle operations between Numbers and integers

    def __add__(self, other):
        self.set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value + other.value)

    def __iadd__(self, other):
        super().set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value + other.value)

    def __sub__(self, other):
        super().set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value - other.value)

    def __isub__(self, other):
        super().set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value - other.value)

    def __mul__(self, other):
        super().set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value * other.value)

    def __imul__(self, other):
        self.set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value * other.value)

    def __pow__(self, other):
        self.set_status(Status.READ)
        other.set_status(Status.READ)
        return Number(self.value**other.value)

    def __lt__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.LESS_THAN)
            other.set_status(Status.GREATER_THAN)
            return self.value < other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.LESS_THAN)
            return self.value < other
        raise TypeError

    def __gt__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.GREATER_THAN)
            other.set_status(Status.LESS_THAN)
            return self.value > other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.GREATER_THAN)
            return self.value > other
        raise TypeError

    def __le__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.LESS_THAN)
            other.set_status(Status.GREATER_THAN)
            return self.value <= other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.LESS_THAN)
            return self.value <= other
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.GREATER_THAN)
            other.set_status(Status.LESS_THAN)
            return self.value >= other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.GREATER_THAN)
            return self.value >= other
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.EQUAL)
            other.set_status(Status.EQUAL)
            return self.value == other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.EQUAL)
            return self.value == other
        raise TypeError

    def __ne__(self, other):
        if isinstance(other, Number):
            self.set_status(Status.DIFFERENT)
            other.set_status(Status.DIFFERENT)
            return self.value == other.value
        elif isinstance(other, int) or isinstance(other, float):
            self.set_status(Status.DIFFERENT)
            return self.value == other
        raise TypeError
