import pyglet
from pprint import pprint


class VisualNode:

    # colors
    _base_color = [128, 128, 128, 255]
    _default_color = [128, 128, 128, 255]

    # geometry
    x = 0.0
    y = 0.0
    width = 100.0
    height = 100.0

    _batch = None
    _vertex_list = None
    _changed = False

    name = "defaultNode"

    def __init__(self, batch):
        self.name = "defaultName"
        self._batch = batch
        self._vertex_list = self._batch.add(6, pyglet.gl.GL_QUAD_STRIP, None,
                                            ('v2f', (self.x, self.y,
                                                     self.x, self.y,
                                                     self.x, self.y + self.height,
                                                     self.x + self.width, self.y,
                                                     self.x + self.width, self.y + self.height,
                                                     self.x + self.width, self.y + self.height)),
                                            ('c4B', self._base_color*6))
        self._label_x = (self.x + self.width) / 2
        self._label_y = self.y + self.height - 10

        self._label = pyglet.text.Label(self.name,
                                        font_name='Times New Roman',
                                        font_size=9,
                                        x=self._label_x, y=self._label_y,
                                        anchor_x='center', anchor_y='center', batch=self._batch)

    def draw(self):

        if self._changed:
            # change node position
            self._vertex_list.vertices[0] = self.x
            self._vertex_list.vertices[1] = self.y

            self._vertex_list.vertices[2] = self.x
            self._vertex_list.vertices[3] = self.y

            self._vertex_list.vertices[4] = self.x
            self._vertex_list.vertices[5] = self.y + self.height

            self._vertex_list.vertices[6] = self.x + self.width
            self._vertex_list.vertices[7] = self.y

            self._vertex_list.vertices[8] = self.x + self.width
            self._vertex_list.vertices[9] = self.y + self.height

            self._vertex_list.vertices[10] = self.x + self.width
            self._vertex_list.vertices[11] = self.y + self.height

            # change color
            self._vertex_list.colors = self._base_color * 6

            # move node label
            self._label.x = self._label_x + self.x
            self._label.y = self._label_y + self.y

            # draw ports
            self._draw_ports()

            self._batch.invalidate()

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

    def _draw_ports(self):
        pass

