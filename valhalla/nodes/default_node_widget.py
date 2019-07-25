from pyflowgraph.node import Node
import autoprop
import uuid


@autoprop
class DefaultNodeWidget(Node):

    def __init_(self, graph, title):
        super().__init__(graph, title)

