import pyglet


class VisualNode:

    # colors
    _base_color = [128, 128, 128, 255]
    _default_color = [128, 128, 128, 255]

    # geometry
    x = 0.0
    y = 0.0
    z = 0.0
    # --------
    _ox = 0.0
    _oy = 0.0

    width = 100.0
    height = 100.0

    _batch = None
    _node_vl = None
    _ports_vl = []
    _port_labels = []

    _changed = False

    name = "defaultNode"
    ports = {
        "inputs": {
            "Model": "In",
            "float": "Scale",
            "int": "Id"
        },
        "outputs": {
            "Model": "Out"
        }
    }
    port_size = 5.0
    port_colors = {
        "Model": [128, 128, 240, 255],
        "float": [128, 240, 128, 255],
        "int": [128, 240, 240, 255]
    }

    def __init__(self, batch):
        self.name = "defaultName"
        self._batch = batch
        self._node_vl = self._batch.add(
            6, pyglet.gl.GL_QUAD_STRIP, None,
            ('v3f', (self.x, self.y, self.z,
                     self.x, self.y, self.z,
                     self.x, self.y + self.height, self.z,
                     self.x + self.width, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z,
                     self.x + self.width, self.y + self.height, self.z)),
            ('c4B', self._base_color*6))

        self._label_x = (self.x + self.width) / 2
        self._label_y = self.y + self.height - 10

        self._label = pyglet.text.Label(self.name,
                                        font_name='Times New Roman',
                                        font_size=9,
                                        x=self._label_x, y=self._label_y,
                                        anchor_x='center', anchor_y='center',
                                        batch=self._batch)
        self._init_ports()

    def draw(self):

        if self._changed:
            # change node position
            self._node_vl.vertices[0] = self.x
            self._node_vl.vertices[1] = self.y

            self._node_vl.vertices[2] = self.x
            self._node_vl.vertices[3] = self.y

            self._node_vl.vertices[4] = self.x
            self._node_vl.vertices[5] = self.y + self.height

            self._node_vl.vertices[6] = self.x + self.width
            self._node_vl.vertices[7] = self.y

            self._node_vl.vertices[8] = self.x + self.width
            self._node_vl.vertices[9] = self.y + self.height

            self._node_vl.vertices[10] = self.x + self.width
            self._node_vl.vertices[11] = self.y + self.height

            # change color
            self._node_vl.colors = self._base_color * 6

            # move node label
            self._label.x = self._label_x + self.x
            self._label.y = self._label_y + self.y

            # draw ports
            self._draw_ports()

            self._batch.invalidate()

            # update original position
            self._ox = self.x
            self._oy = self.y

    def in_bounds(self, x, y):
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                return True

        return False

    def invalidate(self):
        self._changed = True

    def get_local_coord(self, x, y):
        return x - self.x, y - self.y

    def color(self, color):
        self._base_color = color
        self.invalidate()

    def restore_color(self):
        self.color(self._default_color)

    def _init_ports(self):
        inputs = self.ports.get("inputs")
        outputs = self.ports.get("outputs")
        in_offset = self.y + self.height - 20.0
        for type, name in inputs.items():
            pvl = self._batch.add(4, pyglet.gl.GL_QUADS, None,
                                  ('v2f', (self.x - self.port_size / 2.0, in_offset - self.port_size,
                                           self.x - self.port_size / 2.0, in_offset,
                                           self.x + self.port_size / 2.0, in_offset - self.port_size,
                                           self.x + self.port_size / 2.0, in_offset)),
                                  ('c4B', self.port_colors.get(type)*4))
            self._ports_vl.append(pvl)
            pl = pyglet.text.Label(
                self.name,
                font_name='Times New Roman',
                font_size=9,
                x=self.x + self.port_size + 5, y=in_offset - self.port_size,
                anchor_x='left', anchor_y='center',
                batch=self._batch)
            self._port_labels.append(pl)
            in_offset += 8.0



    def _draw_ports(self):
        inputs = self.ports.get("inputs")
        outputs = self.ports.get("outputs")
        pass
