import glooey


class TestNode(glooey.Frame):

    def __init__(self):
        super().__init__()
        pass

    class Decoration(glooey.Background):
        pass

    class Box(glooey.Bin):
        custom_right_padding = 10
        custom_top_padding = 10
        custom_left_padding = 10
        custom_bottom_padding = 10
