from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QLabel

from visualgo.visu.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget

if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = WorldCanvasWidget()
    window.containers.append(CanvasContainer(window, QPoint(1, 1), 3, 3, QLabel("Hello world")))
    window.setMinimumSize(QSize(720, 480))
    window.show()
    app.exec()
