from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number


class Array(Data):
    def __init__(self, is_visible=True):
        super().__init__(is_visible)
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

    def reset_status(self):
        for value in self.value:
            value.reset_status()

    def append(self, value):
        """
        Adds a value at the end of the array.

        :param value: The value to add at the end of the array.
        """
        if isinstance(value, Number):
            self.value.append(Number(value.value))
            self.value[-1].status = Status.AFFECTED
        elif isinstance(value, int) or isinstance(value, float):
            self.value.append(Number(value))
            self.value[-1].status = Status.AFFECTED
        else:
            raise ValueError("Cannot append given type to array")

    def get_flat_data(self):
        return [self] + self.data

    def isEmpty(self):
        """
        Checks if the array is empty.

        :return: A boolean, True if the array is empty, False otherwise.
        """
        return self.size() == 0

    def size(self):
        """
        Returns the number of elements in the array.

        :return: The number of elements in the array.
        """
        return len(self.value)

    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Array):
            return self.value == other.value
        return False
