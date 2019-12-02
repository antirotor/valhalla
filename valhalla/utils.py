"""
This is heavily inspired by Pyblish way of discovering plugins. Currently simplified. I think this needs to be
changed completely, not because Pyblish way is wrong but because I think Valhalla will need more robust way to add
plugins, not just as files ...
"""

import os
import sys
import types
import inspect
from .default_node import DefaultNode

from . import (
    _registered_node_paths,
    _registered_nodes
)


def register_node_path(path):
    normalized = os.path.normpath(path)
    if normalized not in _registered_node_paths:
        _registered_node_paths.append(normalized)
    return path


def _find_nodes_in_module(module):
    nodes = list()

    for name in dir(module):
        obj = getattr(module, name)

        if not inspect.isclass(obj):
            continue

        if not issubclass(obj, DefaultNode):
            continue

        nodes.append(obj)

    return nodes


def discover_nodes():
    nodes = dict()
    node_names = []
    for path in _registered_node_paths:
        if not os.path.isdir(path):
            continue

        for file in os.listdir(path):
            absolute_path = os.path.join(path, file)
            node_name, node_ext = os.path.splitext(file)

            if not node_ext.lower() == ".py":
                continue

            module = types.ModuleType(node_name)
            module.__file__ = absolute_path

            try:
                with open(absolute_path) as n:
                    exec(n.read(), module.__dict__)

                sys.modules[absolute_path] = module
            except Exception as e:
                print("  * skipped [{node}] - {err}".format(node=node_name, err=e))
                continue

            for node in _find_nodes_in_module(module):
                if node.__name__ in node_names:
                    # duplicate node detected
                    continue

                node_names.append(node.__name__)
                node.__module__ = module.__file__
                key = "{0}.{1}".format(node.__module__, node.__name__)
                nodes[key] = node

    nodes = list(nodes.values())
    return nodes



