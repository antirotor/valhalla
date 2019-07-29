from .default_node_widget import DefaultNodeWidget
from .abstract_node import AbstractNode
from pyflowgraph.port import InputPort, OutputPort, IOPort
from Qt import QtGui, QtCore
from pprint import pprint


class DefaultNode(AbstractNode):
    """
    Default node is node from every other node should inherit.
    """

    def disable_evaluation(self):
        pass

    def enable_evaluation(self):
        pass

    def __init__(self, graph, name):
        super().__init__()
        self._graph = graph
        self._node = DefaultNodeWidget(graph, name, self)
        self._initialize_port_widgets()
        self._graph.addNode(self._node)

    def set_position(self, x, y):
        self._node.setGraphPos(QtCore.QPointF(x, y))

    @property
    def id(self):
        return "79b4a290-ea03-436a-9518-c176081aa40e"

    def get_category(self):
        return self._category

    def _initialize_port_widgets(self):
        for ip in self._ports["input"]:
            color = tuple(int(ip['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            self._node.addPort(InputPort(self._node, self._graph, ip['type'], QtGui.QColor(*color), ip['type']))

        for op in self._ports["output"]:
            color = tuple(int(op['color'].lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
            self._node.addPort(OutputPort(self._node, self._graph, op['type'], QtGui.QColor(*color), op['type']))

    def evaluate(self):
        pass

    def set_color(self, color):
        self._node.setColor(QtGui.QColor(*color))



