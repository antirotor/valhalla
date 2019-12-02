import os
import sys
from .version import version, version_info, __version__

# add NodeGraphQt
node_path = os.path.join(os.path.dirname(__file__), "..", "vendor", "NodeGraphQt")
sys.path.insert(0, node_path)

_registered_node_paths = list()
_registered_nodes = dict()

__all__ = [
    "version",
    "version_info",
    "__version__",
    "_registered_node_paths",
    "_registered_nodes"
]
