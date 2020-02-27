from .default_node import DefaultNode


class ScalarNode(DefaultNode):
    _name = "scalar"
    _category = "Basic :: Variables"
    _color = (24, 200, 24)

    # Ports
    _inputs = [
        {"type": "float", "name": "float in"}
    ]
    _outputs = [
        {"type": "float", "name": "float out"}
    ]

    def __init__(self, graph, name):
        super().__init__(graph, name)
        self.set_color(self._color)

    @property
    def id(self):
        return "1b5c7be1-fa9d-4cb7-962f-0433b66c2569"