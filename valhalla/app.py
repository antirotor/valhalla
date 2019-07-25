import sys
from Qt import QtGui, QtWidgets, QtCore
from .nodes.default_node import DefaultNode


from pyflowgraph.graph_view import GraphView
from pyflowgraph.graph_view_widget import GraphViewWidget


def run():
    print('>>> running')
    app = QtWidgets.QApplication(sys.argv)

    widget = GraphViewWidget()
    graph = GraphView(parent=widget)

    node1 = DefaultNode(graph, 'test1')
    node1.set_position(-100, 0)
    node2 = DefaultNode(graph, 'test2')
    node2.set_position(0, 0)

    widget.setGraphView(graph)
    widget.show()

    sys.exit(app.exec_())