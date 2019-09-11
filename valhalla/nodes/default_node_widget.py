from NodeGraphQt import NodeGraph, BaseNode, BackdropNode, setup_context_menu
import autoprop
from Qt import QtGui, QtWidgets
from ..node_properties import PropertiesWindow
import uuid


@autoprop
class DefaultNodeWidget(BaseNode):

    _properties = None

    def __init__(self, graph, title, node):
        self._parent = node
        super().__init__(graph, title)
        self._app = QtWidgets.QApplication.instance()


    def open_properties(self):
        """
        Open properties window
        """
        print("opening properties...")
        if not self._properties:
            self._properties = PropertiesWindow(self)
        else:
            self._properties.show()

    def mouseDoubleClickEvent(self, event):
        print('dblclick:', self.getName())
        self.open_properties()