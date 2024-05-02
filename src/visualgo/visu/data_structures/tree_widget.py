from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPen, QBrush, QFont, QPainter, QBrush, QPen
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QGraphicsScene, QGraphicsView

from visualgo.data_structures.data import Data
from visualgo.visu.WorldCanvas.WidgetWithZoom import WidgetWithZoom

class TreeNode:
    def __init__(self, value: Data, children=None):
        self.value = value

        # Initialize the list of children nodes
        # If no children are provided, create an empty list
        self.children = children or []

        self.state = value.get_status()



class TreeWidget(QGraphicsView, WidgetWithZoom):
    def __init__(self, tree_root, parent=None):
        super().__init__(parent)

        self.tree_root = tree_root

        # Enable anti-aliasing for smoother rendering
        self.setRenderHint(QPainter.Antialiasing)
        self.setBackgroundBrush(QBrush(QColor("#98C1D9")))
        self.setScene(QGraphicsScene())
        # Set the size of the scene
        self.setSceneRect(0, 0, 800, 600)
        # Disable horizontal scrollbars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Disable vertical scrollbars
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.init_tree(tree_root, self.sceneRect().width() // 2, 50)

    def init_tree(self, node, x, y, level=0):
        if node is None:
            return

        # Create an ellipse item to represent the node
        node_item = QGraphicsEllipseItem(x - 20, y - 20, 40, 40)

        # Set the brush color of the node based on its state
        node_item.setBrush(QBrush(node.value.get_status().color))

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
    def sizeHint(self):
        return QSize(800, 600)

    def update_zoom(self, new_zoom):
        self.resetTransform()
        self.scale(new_zoom, new_zoom)
    