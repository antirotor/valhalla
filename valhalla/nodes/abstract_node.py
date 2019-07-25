from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from functools import lru_cache
import autoprop
import os
import uuid
from pprint import pprint


@autoprop
class AbstractNode(ABC):
    """
    This is abstract class serving as a base for all nodes. It sets all basic node geometry options and
    load port types, etc. Node can then be implemented by whatever UI libs. Creating widget node and rendering
    it is on implementing class.
    """
    _name = "default"
    _category = "System :: Default"

    # Ports
    _inputs = [
        {"type": "float", "name": "float in"}
    ]
    _outputs = [
        {"type": "float", "name": "float out"}
    ]
    _ports = {"input": [], "output": []}

    def __init__(self):

        # Metadata
        self._name = "default"
        self._category = "System :: Default"

        # Ports
        self._inputs = [
            {"type": "float", "name": "float in"}
        ]
        self._outputs = [
            {"type": "float", "name": "float out"}
        ]
        self._ports = {"input": [], "output": []}

        self._process_ports()
        super().__init__()

    @property
    @abstractmethod
    def id(self):
        """
        Every node should have its own unique **UUID4**
        :return: uuid of the node
        :rtype: str
        """
        return "55349bfb-b3e1-4786-9b9a-eb7c49be6198"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

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
        # iterate over _inputs and outputs, load type definitions from xml
        ns = {"valhalla": "http://www.valhalla.site/types"}
        for i in self._inputs:
            port_type = self._get_type_root(i.get("type"))
            self._ports["input"].append({"uuid": uuid.uuid4(),
                                         "type": port_type.findall("valhalla:name", ns)[0].text,
                                         "map": port_type.findall("valhalla:map", ns)[0].text,
                                         "color": port_type.findall("valhalla:color", ns)[0].text,
                                         "description": port_type.findall("valhalla:description", ns)[0].text,
                                         "connections": []})
            pass
        for o in self._outputs:
            port_type = self._get_type_root(o.get("type"))
            self._ports["output"].append({"uuid": uuid.uuid4(),
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
