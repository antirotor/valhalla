from pprint import pprint

from .abstract_node import AbstractNode
from NodeGraphQt import BaseNode


class DefaultNode(AbstractNode):
    """
    Default node is node from every other node should inherit.
    """

    __identifier__ = "net.annatar"
    NODE_NAME = 'DefaultNode'

    def disable_evaluation(self):
        pass

    def enable_evaluation(self):
        pass

    def __init__(self):
        self._inputs = []
        self._outputs = []
        super(DefaultNode, self).__init__()
        self._initialize_ports()

    @property
    def node_id(self):
        return "79b4a290-ea03-436a-9518-c176081aa40e"

    def get_category(self):
        return self._category

    def _initialize_ports(self):
        index = 1
        for ip in self._ports["input"]:
            color = tuple(int(ip['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            node_name = "{}_in{}".format(ip['type'], index)
            print("--- adding: {}".format(node_name))
            self.add_input(node_name, display_name=True, color=color)
            index += 1

        index = 1
        for op in self._ports["output"]:
            color = tuple(int(op['color'].lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
            node_name = "{}_in{}".format(ip['type'], index)
            print("--- adding: {}".format(node_name))
            self.add_output(node_name, multi_output=True, color=color)
            index += 1

    def evaluate(self):
        pass




