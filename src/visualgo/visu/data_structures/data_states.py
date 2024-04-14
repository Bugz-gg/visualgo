from PyQt5.QtGui import QColor

from visualgo.data_structures.data import Status

default_color = QColor(168, 213, 226)

status_to_color_dict: dict[Status, QColor] = {
    Status.NONE: default_color,
    Status.CREATED: QColor(108, 174, 117),
    Status.AFFECTED: QColor(237, 240, 218),
    Status.COMPARED: QColor(211, 135, 171),
    Status.READ: QColor("light blue")
}


def status_to_color(status: Status):
    try:
        return status_to_color_dict[status]
    except KeyError:
        return default_color

