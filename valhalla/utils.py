"""
This is heavily inspired by Pyblish way of discovering plugins. Currently
simplified. I think this needs to be changed completely, not because Pyblish
way is wrong but because I think Valhalla will need more robust way to add
plugins, not just as files ...
"""

import os
import sys
import types
import inspect
from .default_node import DefaultNode
import xml.etree.ElementTree as ET
from functools import lru_cache

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
                print("  * skipped [{node}] - {err}".format(node=node_name,
                                                            err=e))
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


@lru_cache(maxsize=32)
def get_type_info(type_name):
    """
    This will load xml file defined by `type_name` and return
    its xml root node.

    :param type_name: name of type
    :return: type node root element
    """
    ns = {"valhalla": "http://www.valhalla.site/types"}
    package_directory = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__)))
    xml_file = os.path.join(
        package_directory, 'types', '{}.xml'.format(type_name))
    tree = ET.parse(xml_file)
    port_type = tree.getroot()

    type_info = {
        "type": port_type.findall("valhalla:name", ns)[0].text,
        "map": port_type.findall("valhalla:map", ns)[0].text,
        "color": port_type.findall("valhalla:color", ns)[0].text,
        "description": port_type.findall("valhalla:description", ns)[0].text
    }

    return type_info
