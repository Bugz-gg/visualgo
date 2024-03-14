from visualgo.data_structures.data import Data,Status

class Array(Data):
    
    def __init__(self, is_visualisable):
        self.is_visualisable = is_visualisable
        self.data = []
        

    def __getitem__(self, index):
        self.data[index].status = Status.READ
        return self.data[index]

