from .abstract_node import AbstractNode


class DefaultNode(AbstractNode):
    """
    Default node is node from every other node should inherit.
    """

    __identifier__ = "net.annatar"
    NODE_NAME = 'DefaultNode'

    def __init__(self):

        super(DefaultNode, self).__init__()
        self._initialize_ports()
        self._evaluate = False

    @property
    def node_id(self):
        return "79b4a290-ea03-436a-9518-c176081aa40e"

    def get_category(self):
        return self._category

    def _initialize_ports(self):
        """
        Load port definitions from xml and add it to node

        :return: number of input and output ports created
        :rtype: tuple
        """
        index = 1
        for ip in self._ports["in"]:
            color = tuple(int(ip['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
            node_name = "{}_in{}".format(ip['type'], index)
            # print("--- adding: {}".format(node_name))
            ip["port_instance"] = self.add_input(node_name, display_name=True, color=color)
            index += 1
        input_ports = index

        index = 1
        for op in self._ports["out"]:
            color = tuple(int(op['color'].lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
            node_name = "{}_out{}".format(op['type'], index)
            # print("--- adding: {}".format(node_name))
            op["port_instance"] = self.add_output(node_name, multi_output=True, color=color)
            index += 1
        output_ports = index

        return input_ports, output_ports

    def _do_evaluate(self):
        pass

    def evaluate(self):
        if not self._evaluate:
            return

        for available_port in self._ports["in"]:
            connected_ports = available_port["port_instance"].connected_ports()
            if not connected_ports:
                pass
            if len(connected_ports) != 1:
                # TODO: proper error handling
                raise RuntimeError("Multiple connection to in port are not allowed")

            connected_port = connected_ports[0]

            result = connected_ports.node().evaluate()
