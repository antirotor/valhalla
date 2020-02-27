from .abstract_node import AbstractNode
import errors

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

    def _do_evaluate(self):
        pass

    def _gather_input_values(self):
        for available_port in self._ports["in"]:
            connected_ports = available_port["port_instance"].connected_ports()
            if connected_ports.len() < 1:
                # no ports are connected
                continue
            if not connected_ports:
                pass
            if len(connected_ports) != 1:
                # TODO: proper error handling
                raise RuntimeError(
                    "Multiple connection to port are not allowed")

            connected_port = connected_ports[0]

            try:
                available_port["value"] = connected_port.node().evaluate()[connected_port]
            except errors.NodeEvaluationError as e:
                print("!!! {}: {}".format(connected_port.node(), e))

    def evaluate(self):
        if self.disabled():
            return

        self._gather_input_values()
        self._do_evaluate()
        results = dict()
        for out_port in self._ports["out"]:
            results[out_port["port_instance"]] = out_port["value"]

        return results
