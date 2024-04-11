from enum import Enum

from PyQt5.QtGui import QColor

from visualgo.data_structures.data import Status


class DataStates(Enum):
    NORMAL = (1, QColor("white"))
    CREATED = (2, QColor("lime green"))
    AFFECTED = (3, QColor("pink"))
    COMPARED = (4, QColor("red"))
    READ = (5, QColor("light blue"))

    def __new__(cls, nb: int, color: QColor):
        entry = object.__new__(cls)
        entry.nb = entry._value_ = nb
        entry.color = color
        return entry

    @staticmethod
    def from_status(status: Status):
        match status:
            case Status.NONE: return DataStates.NORMAL
            case Status.CREATED: return DataStates.CREATED
            case Status.AFFECTED: return DataStates.AFFECTED
            case Status.COMPARED: return DataStates.COMPARED
            case Status.READ: return DataStates.READ
            case _: raise RuntimeError(f"Unrecognized status {status}.")
