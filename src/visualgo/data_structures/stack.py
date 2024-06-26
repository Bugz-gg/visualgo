from visualgo.data_structures.data import Data, Status
from visualgo.data_structures.number import Number


class Stack(Data):
    def __init__(self, is_visible=True):
        super().__init__(is_visible)
        self.value = []

    def get_flat_data(self):
        return [self] + self.value

    def __str__(self):
        return ", ".join(str(val) for val in self.__dict__['value']) + f" {self.status}"
    
    def pop(self):
        """
        Removes the top element of the stack. Assert that the stack is not empty.

        :return: The top element of the stack.
        """

        super().set_status(Status.REMOVED_INSIDE)
        assert not self.isEmpty(), "stack is empty"
        return self.value.pop(0)
    
    def push(self, value):
        """
        Pushes a value onto the top of the stack.
        
        :param value: Value to push onto the stack.
        :return:
        """

        super().set_status(Status.LOOKED_INSIDE)

        if isinstance(value, int):
            self.value.insert(0, Number(value))
        else:
            self.value.insert(0, value)
        
    def isEmpty(self):
        """
        Checks if the stack is empty.

        :return: A boolean, True if the stack is empty, False otherwise.
        """
        return self.size() == 0

    def size(self):
        """
        Returns the number of elements in the stack.

        :return: The number of elements in the stack.
        """
        return len(self.value)
    
    def clear(self):
        """
        Reset the stack by removing all elements.

        :return:
        """
        self.value = []
        assert self.isEmpty(), "stack not empty"
    
    def peep(self):
        """
        Returns the top element of the stack without removing it. Assert that the stack is not empty.

        :return: The top element of the stack.
        """
        assert not self.isEmpty(), "stack is empty"
        return self.value[0]
    
    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Stack):
            return self.value == other.value
        return False
