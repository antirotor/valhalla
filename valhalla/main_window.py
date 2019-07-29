import sys
from PyQt5 import QtCore, QtWidgets
from .nodes.default_node import DefaultNode
from .nodes.scalar import ScalarNode

from pyflowgraph.graph_view import GraphView
from pyflowgraph.graph_view_widget import GraphViewWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._nodes = {}
        self.view_widget = GraphViewWidget()
        self.graph = GraphView(parent=self.view_widget)

        # this is just for testing
        node1 = DefaultNode(self.graph, 'test1')
        node1.set_position(-150, 0)
        self._nodes['test1'] = node1

        node2 = ScalarNode(self.graph, 'scalar1')
        node2.set_position(0, 0)
        self._nodes['test2'] = node2

        self.view_widget.setGraphView(self.graph)

    def show(self):
        self.view_widget.show()
