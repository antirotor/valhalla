from NodeGraphQt import Port


class TypedPort(Port):

    def __init__(self, *args, **kwargs):
        port_type = kwargs.pop('port_type', None)
        super(TypedPort, self).__init__(*args, **kwargs)
        self.port_type = port_type
