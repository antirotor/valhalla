from .nodes.default_node import DefaultNode
from .nodes.test_node import TestNode

import pyglet
import glooey

from pyglet.gl import *


def run():
    print('>>> running')
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window = pyglet.window.Window()
    pyglet.gl.glClearColor(0.2, 0.2, 0.2, 1)
    gui = glooey.Gui(window)
    f = DefaultNode()
    # f.add(glooey.Placeholder(200, 200))

    f.set_width_hint(200)
    f.set_height_hint(200)

    gui.add(f)
    # f.debug_drawing_problems()
    # f.debug_placement_problems()
    pyglet.app.run()

    # window.push_handlers(o)
