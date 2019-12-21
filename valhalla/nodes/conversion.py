from valhalla.default_node import DefaultNode


class Integer2Float(DefaultNode):
    NODE_NAME = "Integer2Float"
    identifier = "net.annatar"
    category = "Basic :: Conversion"
    color = (86, 131, 115)  # rgb(86, 131, 115)

    # Ports
    port_inputs = [{"type": "int", "name": "int in"}]
    port_outputs = [{"type": "float", "name": "float out"}]

    _value = 0
    _value_port = None

    def __init__(self):
        super(Integer2Float, self).__init__()
        self._value_port = self.add_text_input(
            "value", "Integer value", str(self._value)
        )
        self.set_color(*self.color)

    @property
    def node_id(self):
        return "78fb45ef-7ad2-4510-bcdf-271c577e2228"

    def _do_evaluate(self):
        return


class Float2Integer(DefaultNode):
    NODE_NAME = "Float2Integer"
    identifier = "net.annatar"
    category = "Basic :: Conversion"
    color = (86, 111, 131)  # rgb(86, 111, 131)

    # Ports
    port_inputs = [{"type": "float", "name": "float in"}]
    port_outputs = [{"type": "int", "name": "int out"}]

    _value = 0
    _value_port = None

    def __init__(self):
        super(Float2Integer, self).__init__()
        self._value_port = self.add_text_input(
            "value", "Integer value", str(self._value)
        )
        self.set_color(*self.color)

    @property
    def node_id(self):
        return "f4bf4b0b-d2f9-46aa-bd78-8dfb43653b78"

    def _do_evaluate(self):
        return
