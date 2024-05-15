from abc import ABC, abstractmethod, ABCMeta

from visualgo.data_structures.data import Status
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom


class CustomMeta(ABCMeta, type(WidgetWithZoom)):
    pass


class VisualWidget(ABC, WidgetWithZoom, metaclass=CustomMeta):
    """
    The base class for any visual fantasy.
    """
    def __init__(self, status):
        super().__init__()
        self.status = status

    @abstractmethod
    def get_flat_data(self):
        """
        Returns: a list of all the instances of Visual Widget.

        For singular value, it would be something like [self].
        For containers, something like [self] + internal_list_of_visual_widgets

        """
        pass
