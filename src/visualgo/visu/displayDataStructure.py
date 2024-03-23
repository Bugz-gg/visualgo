from enum import Enum


from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QGraphicsView, QGraphicsScene, 
                             QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem, 
                             QGraphicsTextItem)
from PyQt5.QtCore import Qt, QRect, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont


class DataState(Enum):
    NORMAL = (1, QColor("white"))
    CREATED = (2, QColor("lime green"))
    ACCESSED = (3, QColor("light blue"))
    COMPARED = (4, QColor("red"))

    def __new__(cls, nb, color):
        entry = object.__new__(cls)
        entry.nb = entry._value_ = nb
        entry.color = color
        return entry


class ArrayCellWidget(QWidget):
    def __init__(self, value, default_state=DataState.NORMAL):
        super().__init__()
        self._value = value
        self.state = default_state
        self.setFixedSize(30, 30)  # cell size

    def set_state(self, state: DataState):
        self.state = state

    def paintEvent(self, event):
        painter = QPainter(self)
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)

        # Set correct background color
        painter.fillRect(self.rect(), self.state.color)
        painter.drawText(self.rect(), Qt.AlignCenter, str(self._value))


class ArrayWidget(QWidget):
    def __init__(self, array, states: list[DataState] = None):
        super().__init__()
        self.cell_array = [ArrayCellWidget(value) for value in array]
        self.setObjectName("ArrayWidget")  # Set object name for styling

        # set proper state if states are given
        if states is not None:
            for i, state in enumerate(states):
                self.cell_array[i].set_state(state)

        # Create a horizontal layout for the ArrayWidget
        layout = QHBoxLayout()

        # Create an ArrayCellWidget for each array value and add it to the layout
        for cell in self.cell_array:
            layout.addWidget(cell)

            # Set the layout on the ArrayWidget
        self.setLayout(layout)


class TreeNode:
    def __init__(self, value, children=None, state=DataState.NORMAL):
        self.value = value
        
        # Initialize the list of children nodes
        # If no children are provided, create an empty list
        self.children = children or []
        
        self.state = state

class TreeWidget(QGraphicsView):
    def __init__(self, tree_root, parent=None):
        super().__init__(parent)
        
        self.tree_root = tree_root
        
        # Enable anti-aliasing for smoother rendering
        self.setRenderHint(QPainter.Antialiasing)
        self.setBackgroundBrush(QBrush(QColor("white")))
        self.setScene(QGraphicsScene())
        # Set the size of the scene
        self.setSceneRect(0, 0, 800, 600)
        # Disable horizontal scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Disable vertical scrollbars
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.init_tree(tree_root, self.sceneRect().width() // 2, 50)

    def init_tree(self, node, x, y, level=0):
        # Create an ellipse item to represent the node
        node_item = QGraphicsEllipseItem(x - 20, y - 20, 40, 40)
        
        # Set the brush color of the node based on its state
        node_item.setBrush(QBrush(node.state.color))
        
        # Set a black pen for the outline of the node
        node_item.setPen(QPen(QColor("black"), 2))
        
        # Add the node item to the scene
        self.scene().addItem(node_item)

        # Create a text item to display the node value
        text_item = QGraphicsTextItem(str(node.value))
        text_item.setFont(QFont("Arial", 12))
        
        # Set the text item as a child of the node item
        text_item.setParentItem(node_item)
        
        # Position the text item inside the node
        text_item.setPos(x - 8, y - 10)

        # If the node has children
        if node.children:
            child_width = (len(node.children) - 1) * 100 
            # this ensures that the child nodes are evenly spaced horizontally, with a distance of 100 units between each child.
            
            # Calculate the starting x-coordinate for the child nodes
            child_x = x - child_width // 2

            for child in node.children:
                # Calculate the y-coordinate for the child node
                child_y = y + 100
                
                # Create a line item to connect the parent and child nodes
                line_item = QGraphicsLineItem(x, y + 20, child_x, child_y - 20)
                line_item.setPen(QPen(QColor("black"), 2))
                
                # Add the line item to the scene
                self.scene().addItem(line_item)
                
                # Recursively initialize the child node
                self.init_tree(child, child_x, child_y, level + 1)
                
                # Update the x-coordinate for the next child node
                child_x += 100
if __name__ == "__main__":
    app = QApplication([])
    # load QSS file
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    # window = ArrayWidget([1, 2, 3, 4])
    # testing the tree widget visualization
    tree_root = TreeNode(1, [
        TreeNode(2, [TreeNode(4, state=DataState.CREATED), TreeNode(5, state=DataState.CREATED), TreeNode(6, state=DataState.CREATED)]),
        TreeNode(3, state=DataState.ACCESSED)
    ])
    window = TreeWidget(tree_root)
    window.showMaximized()
    app.exec()

