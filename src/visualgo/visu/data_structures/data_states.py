from PyQt5.QtGui import QColor

from visualgo.data_structures.data import Status

default_color = QColor("white")

status_to_color_dict: dict[Status, QColor] = {
    Status.NONE: default_color,
    Status.CREATED: QColor("lime green"),
    Status.AFFECTED: QColor("pink"),
    Status.COMPARED: QColor("red"),
    Status.READ: QColor("light blue")
}


def status_to_color(status: Status):
    try:
        return status_to_color_dict[status]
    except KeyError:
        return default_color

