from abc import ABC, abstractmethod, ABCMeta

from visualgo.data_structures.data import Status
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom


class CustomMeta(ABCMeta, type(WidgetWithZoom)):
    pass


class VisualWidget(ABC, WidgetWithZoom, metaclass=CustomMeta):
    def __init__(self, status):
        super().__init__()
        self.status = status

    @abstractmethod
    def get_flat_data(self):
        pass
