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
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value + other.value)
        elif isinstance(other, int):
            return Number(self.value + other)
        else:
            raise TypeError(f"Unsupported operand type for + : {type(self).__name__} and {type(other).__name__}")
    
    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        self.set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(other.value + self.value)
        elif isinstance(other, int):
            return Number(other + self.value)
        else:
            raise TypeError(f"Unsupported operand type for + : {type(other).__name__} and {type(self).__name__}")

    def __sub__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value - other.value)
        elif isinstance(other, int):
            return Number(self.value - other)
        else:
            raise TypeError(f"Unsupported operand type for - : {type(self).__name__} and {type(other).__name__}")
        
    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(other.value - self.value)
        elif isinstance(other, int):
            return Number(other - self.value)
        else:
            raise TypeError(f"Unsupported operand type for - : {type(other).__name__} and {type(self).__name__}")
    
    def __mul__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value * other.value)
        elif isinstance(other, int):
            return Number(self.value * other)
        else:
            raise TypeError(f"Unsupported operand type for * : {type(self).__name__} and {type(other).__name__}")
    
    def __imul__(self, other):
        return self.__mul__(other)
    
    def __rmul__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(other.value * self.value)
        elif isinstance(other, int):
            return Number(other * self.value)
        else:
            raise TypeError(f"Unsupported operand type for * : {type(other).__name__} and {type(self).__name__}")
    
    def __floordiv__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value // other.value)
        elif isinstance(other, int):
            return Number(self.value // other)
        else:
            raise TypeError(f"Unsupported operand type for // : {type(self).__name__} and {type(other).__name__}")
    
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    
    def __rfloordiv__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(other.value // self.value)
        elif isinstance(other, int):
            return Number(other // self.value)
        else:
            raise TypeError(f"Unsupported operand type for // : {type(other).__name__} and {type(self).__name__}")

    def __mod__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value % other.value)
        elif isinstance(other, int):
            return Number(self.value % other)
        else:
            raise TypeError(f"Unsupported operand type for % : {type(self).__name__} and {type(other).__name__}")

    def __imod__(self, other):
        return self.__mod__(other)
    
    def __rmod__(self, other):
        super().set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(other.value % self.value)
        elif isinstance(other, int):
            return Number(other % self.value)
        else:
            raise TypeError(f"Unsupported operand type for % : {type(other).__name__} and {type(self).__name__}")

    def __pow__(self, other):
        self.set_status(Status.READ)
        if isinstance(other, Number):
            other.set_status(Status.READ)
            return Number(self.value**other.value)
        elif isinstance(other, int):
            return Number(self.value**other)
        else:
            raise TypeError(f"Unsupported operand type for ** : {type(other).__name__} and {type(self).__name__}")
        
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
