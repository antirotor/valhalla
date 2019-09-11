import sys
import os

from . import app


if __name__ == "__main__":
    node_path = os.path.join(os.path.dirname(__file__), "..", "vendor", "NodeGraphQt")
    print(node_path)
    sys.path.insert(0, node_path)
    app.run()
