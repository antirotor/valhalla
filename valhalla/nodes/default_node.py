from .abstract_node import AbstractNode
import pyglet
import glooey
import autoprop
import uuid


@autoprop
class DefaultNode(AbstractNode, glooey.Frame):

    def disable_evaluation(self):
        pass

    def enable_evaluation(self):
        pass

    def __init_(self):
        super().__init__()
        self._create()

    def _create(self):
        content_grid = glooey.Grid(num_rows=3, num_cols=3)
        content_grid.set_row_height(0, 16)
        content_grid.set_row_height(2, 16)
        content_grid.set_col_width(0, 16)
        content_grid.set_col_width(2, 16)

        content_grid.pack()

        content_grid.add(0, 0, glooey.Placeholder())
        content_grid.add(0, 1, self.NodeTitle('foo'))
        content_grid.add(0, 2, glooey.Placeholder())

        content_grid.add(1, 0, glooey.Placeholder())
        content_grid.add(1, 1, glooey.Placeholder())
        content_grid.add(1, 2, glooey.Placeholder())

        content_grid.add(2, 0, glooey.Placeholder())
        content_grid.add(2, 1, glooey.Placeholder())
        content_grid.add(2, 2, glooey.Placeholder())

        self.add(content_grid)

    @property
    def id(self):
        return "79b4a290-ea03-436a-9518-c176081aa40e"

    def get_category(self):
        pass

    def initialize_port_widgets(self):
        pass

    def evaluate(self):
        pass

    def _get_layers(self, key):
        layers = {
            'node': 0,
            'labels': 1,
            'ports': 2,
            'tags': 3
        }
        return pyglet.graphics.OrderedGroup(layers[key], self.group)

    class Decoration(glooey.Background):
        custom_center = pyglet.resource.texture('resources/center.png')
        custom_top = pyglet.resource.texture('resources/top.png')
        custom_bottom = pyglet.resource.texture('resources/bottom.png')
        custom_left = pyglet.resource.texture('resources/left.png')
        custom_right = pyglet.resource.texture('resources/right.png')
        custom_top_left = pyglet.resource.image('resources/top_left.png')
        custom_top_right = pyglet.resource.image('resources/top_right.png')
        custom_bottom_left = pyglet.resource.image('resources/bottom_left.png')
        custom_bottom_right = pyglet.resource.image('resources/bottom_right.png')

    class Box(glooey.Bin):
        custom_right_padding = 8
        custom_top_padding = 0
        custom_left_padding = 0
        custom_bottom_padding = 8

    class NodeTitle(glooey.Label):
        custom_font_name = "Open Sans SemiBold"
        custom_font_size = 10
        custom_alignment = 'center'
