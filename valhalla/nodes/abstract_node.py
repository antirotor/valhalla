from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from functools import lru_cache
import autoprop
import os
import uuid
from pprint import pprint

from NodeGraphQt import BaseNode


@autoprop
class AbstractNode(ABC, BaseNode):
    """
    This is abstract class serving as a base for all nodes. It sets all basic node geometry options and
    load port types, etc. Node can then be implemented by whatever UI libs. Creating widget node and rendering
    it is on implementing class.
    """
    _name = "default"
    _category = "System :: Default"

    # Ports
    port_inputs = [
        {"type": "float", "name": "float in"}
    ]
    port_outputs = [
        {"type": "float", "name": "float out"}
    ]
    _ports = {"input": [], "output": []}

    def __init__(self):

        super(AbstractNode, self).__init__()
        # Metadata
        self._name = "default"
        self._category = "System :: Default"

        # Ports
        self.port_inputs = [
            {"type": "float", "name": "float in"}
        ]
        self.port_outputs = [
            {"type": "float", "name": "float out"}
        ]
        self._ports = {"input": [], "output": []}

        self._process_ports()

    @lru_cache(maxsize=32)
    def _get_type_root(self, type_name):
        """
        This will load xml file defined by `type_name` and return its xml root node.

        :param type_name: name of type
        :return: type node root element
        """
        package_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..')
        xml_file = os.path.join(package_directory, 'types', '{}.xml'.format(type_name))
        tree = ET.parse(xml_file)
        port_type = tree.getroot()
        return port_type

    def _process_ports(self):
        """
        Load all ports defined for node in `self.inputs` and `self._outputs`, create their uuids and
        fill in data found in their respective xml definitions.
        """
        # iterate over port_inputs and port_outputs, load type definitions from xml
        ns = {"valhalla": "http://www.valhalla.site/types"}
        for i in self.port_inputs:
            port_type = self._get_type_root(i.get("type"))
            self._ports["input"].append({"uuid": str(uuid.uuid4()),
                                         "type": port_type.findall("valhalla:name", ns)[0].text,
                                         "map": port_type.findall("valhalla:map", ns)[0].text,
                                         "color": port_type.findall("valhalla:color", ns)[0].text,
                                         "description": port_type.findall("valhalla:description", ns)[0].text,
                                         "connections": []})
            pass
        for o in self.port_outputs:
            port_type = self._get_type_root(o.get("type"))
            self._ports["output"].append({"uuid": str(uuid.uuid4()),
                                          "type": port_type.findall("valhalla:name", ns)[0].text,
                                          "map": port_type.findall("valhalla:map", ns)[0].text,
                                          "color": port_type.findall("valhalla:color", ns)[0].text,
                                          "description": port_type.findall("valhalla:description", ns)[0].text,
                                          "connections": []})
        pass
        pprint(self._ports["input"])

    @abstractmethod
    def get_category(self):
        return self._category

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def disable_evaluation(self):
        pass

    @abstractmethod
    def enable_evaluation(self):
        pass
