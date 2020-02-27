from valhalla.default_node import DefaultNode


class IntegerValue(DefaultNode):
    NODE_NAME = 'IntegerValue'
    identifier = "net.annatar"
    category = "Basic :: Variables"
    color = (22, 64, 73)

    # Ports
    port_inputs = [
        {"type": "int", "name": "int in"}
    ]
    port_outputs = [
        {"type": "int", "name": "int out"}
    ]

    _value = 0
    _value_port = None

    def __init__(self):
        super(IntegerValue, self).__init__()
        self._value_port = self.add_text_input(
            "value", "Integer value", str(self._value))
        self.set_color(*self.color)

    @property
    def node_id(self):
        return "d91d3615-c696-41cb-9d60-31f88bbed9a9"

    def _do_evaluate(self):
        inputs = self.inputs()
        for input_name, port in inputs.items():
            connected = port.connected_ports()
            if connected.len() < 1:
                # no ports are connected
                continue
            for connected_port in connected:
                connected_node = connected_port.node()
                connected_node.evaluate()

        return


class ScalarNode(DefaultNode):
    NODE_NAME = 'Scalar Value'
    identifier = "net.annatar"
    category = "Basic :: Variables"
    color = (46, 73, 22)

    # Ports
    port_inputs = [
        {"type": "float", "name": "float in"}
    ]
    port_outputs = [
        {"type": "float", "name": "float out"}
    ]

    _value = 0
    _value_port = None

    def __init__(self):
        super(ScalarNode, self).__init__()
        self._value_port = self.add_text_input(
            "value", "Scalar value", str(self._value))
        self.set_color(*self.color)

    @property
    def node_id(self):
        return "1b5c7be1-fa9d-4cb7-962f-0433b66c2569"
