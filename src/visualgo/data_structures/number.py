from data import Status, Data

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
    