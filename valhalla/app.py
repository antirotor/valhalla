import sys
from NodeGraphQt import QtWidgets
from NodeGraphQt import NodeGraph, BackdropNode, setup_context_menu
from .nodes.default_node import DefaultNode


def run():
    print('>>> running')
    app = QtWidgets.QApplication(sys.argv)
    graph = NodeGraph()
    setup_context_menu(graph)
    graph.register_node(DefaultNode)
    # graph.register_node(BackdropNode)

    # backdrop = graph.create_node('nodeGraphQt.nodes.Backdrop', name='Backdrop')
    default = graph.create_node('net.annatar.DefaultNode', name='Default Node')

    viewer = graph.viewer()
    viewer.show()

    sys.exit(app.exec_())
