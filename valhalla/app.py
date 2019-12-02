import sys
import os
from pprint import pprint

from NodeGraphQt import QtWidgets, QtCore
from NodeGraphQt import NodeGraph, setup_context_menu, PropertiesBinWidget, Port
from . import (
    _registered_nodes
)

from .utils import register_node_path, discover_nodes


def _get_package_path():
    lib_py_path = sys.modules[__name__].__file__
    return os.path.dirname(lib_py_path)


@QtCore.Slot(Port, Port)
def _validate_connection(in_port, out_port):
    print("--- connected - {} -> {}".format(out_port.name(), in_port.name()))
    out_node = out_port.node()
    in_node = in_port.node()



def run():
    print('>>> running')
    app = QtWidgets.QApplication(sys.argv)
    graph = NodeGraph()
    setup_context_menu(graph)

    register_node_path(os.path.join(_get_package_path(), "nodes"))
    _registered_nodes = discover_nodes()
    pprint(_registered_nodes)

    for node in _registered_nodes:
        graph.register_node(node)
    # graph.register_node(BackdropNode)

    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)

    def show_prop_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()

    graph.node_double_clicked.connect(show_prop_bin)

    default = graph.create_node('net.annatar.DefaultNode', name='Default Node')

    viewer = graph.viewer()
    viewer.show()
    graph.port_connected.connect(_validate_connection)

    sys.exit(app.exec_())
