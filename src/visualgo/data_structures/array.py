from visualgo.data_structures.data import Data,Status

class Array(Data):
    data = []
    is_visualisable = True
    
    def __init__(self, is_visualisable):
        self.is_visualisable = is_visualisable
    
    def __del__(self):  
        self.data.clear()

