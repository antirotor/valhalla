from abc import ABC

from .nodes.node import VisualNode
from pyglet.gl import *



class ValhallaWindow(pyglet.window.Window):

    _nodes = []
    _selected_node = None

    def __init__(self, width, height, resizable):
        super(ValhallaWindow, self).__init__(width, height, resizable)
        self._batch = pyglet.graphics.Batch()
        self._nodes.append(VisualNode(self._batch))

    def on_mouse_press(self, x, y, button, modifiers):
        for n in self._nodes:
            if n.in_bounds(x, y):
                self._selected_node = n
                n.color([255, 128, 0, 255])

    def on_mouse_release(self, x, y, button, modifiers):
        self._selected_node.restore_color()
        self._selected_node = None

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self._selected_node:
            rx, ry = self._selected_node.get_local_coord(x, y)
            self._selected_node.x = self._selected_node.x + dx
            self._selected_node.y = self._selected_node.y + dy
            self._selected_node.invalidate()

    def render(self):
        self.clear()
        for n in self._nodes:
            n.draw(self._batch)
        self._batch.draw()

    def on_draw(self):
        self.render()


def run():
    print('running')
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    window = ValhallaWindow(1280, 720, resizable=True)
    pyglet.app.run()

    # window.push_handlers(o)
