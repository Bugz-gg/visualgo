from visualgo.data_structures.data import Data,Status

class Queue(Data):
    def __init__(self):
        super().__init__()
        self.value = []
    
    def remove(self):
        """
        Removes the first element of the queue. Assert that the queue is not empty.

        :return: The first element of the queue.
        """
        super().set_status(Status.READ)
        assert not self.isEmpty(), "queue is empty"
        return self.value.pop(self.size() - 1)
    
    def add(self, value):
        """
        Adds a value at the end of the queue.
        
        :param value: Value to add at the end of the queue.
        :return:
        """
        super().set_status(Status.READ)
        self.value.insert(0, value) 
        assert not self.isEmpty(), "operation failed, queue is empty"
        
    def isEmpty(self):
        """
        Checks if the queue is empty.

        :return: A boolean, True if the queue is empty, False otherwise.
        """
        return self.size() == 0
    
    def size(self):
        """
        Returns the number of elements in the queue.

        :return: The number of elements in the queue.
        """
        return len(self.value)
    
    def clear(self):
        """
        Reset the queue by removing all elements.

        :return:
        """
        self.value = []
        assert self.isEmpty(), "queue not empty"
    
    def __eq__(self, other):
        self.set_status(Status.EQUAL)
        other.set_status(Status.EQUAL)
        if isinstance(other, Queue):
            return self.value == other.value
        return False    
    
    
    
    