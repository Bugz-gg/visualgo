from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

from visualgo.visu.CanvasContainer import CanvasContainer
from visualgo.visu.WorldCanvasWidget import WorldCanvasWidget
from visualgo.visu.displayDataStructure import ArrayWidget, DataState, ArrayCellWidget, TreeNode, TreeWidget
from visualgo.visu.programState import ProgramState
from visualgo.visu.visualizer import Visualizer

if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = WorldCanvasWidget()

    program_state = ProgramState({"my_list_variable":
                      lambda: ArrayWidget([1, 2, 3],
                                          [DataState.NORMAL, DataState.NORMAL, DataState.NORMAL]
                                          ), "max_value": lambda: ArrayCellWidget(1, DataState.NORMAL),
                  "my_tree_variable": lambda: TreeWidget(TreeNode(1, [
                      TreeNode(2, [TreeNode(4, state=DataState.CREATED), TreeNode(5, state=DataState.CREATED)]),
                      TreeNode(3)
                  ]))})

    mainWidget = QWidget()
    visualizer = Visualizer()
    visualizer.update_data(program_state)
    mainWidget.setLayout(visualizer)

    window.containers.append(CanvasContainer(window, QPoint(-5, 5), QSize(20, 10), mainWidget))
    window.setMinimumSize(QSize(720, 480))
    window.show()
    app.exec()
