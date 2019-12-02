from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from functools import lru_cache
import autoprop
import os
import uuid
from pprint import pprint

from NodeGraphQt import BaseNode, Port
from NodeGraphQt.errors import PortRegistrationError
from NodeGraphQt.constants import IN_PORT, OUT_PORT


@autoprop
class AbstractNode(ABC, BaseNode):
    """
    This is abstract class serving as a base for all nodes. It sets all basic node geometry options and
    load port types, etc. Node can then be implemented by whatever UI libs. Creating widget node and rendering
    it is on implementing class.
    """
    category = "System :: Default"

    # Ports
    port_inputs = [
        {"type": "float", "name": "float in"}
    ]
    port_outputs = [
        {"type": "float", "name": "float out"}
    ]

    def __init__(self):

        super(AbstractNode, self).__init__()
        self._ports = {"in": [], "out": []}
        self._process_ports()

    @lru_cache(maxsize=32)
    def _get_type_root(self, type_name):
        """
        This will load xml file defined by `type_name` and return its xml root node.

        :param type_name: name of type
        :return: type node root element
        """
        package_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
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
            self._ports["in"].append({"uuid": str(uuid.uuid4()),
                                      "type": port_type.findall("valhalla:name", ns)[0].text,
                                      "map": port_type.findall("valhalla:map", ns)[0].text,
                                      "color": port_type.findall("valhalla:color", ns)[0].text,
                                      "description": port_type.findall("valhalla:description", ns)[0].text,
                                      "value": None})
            pass
        for o in self.port_outputs:
            port_type = self._get_type_root(o.get("type"))
            self._ports["out"].append({"uuid": str(uuid.uuid4()),
                                       "type": port_type.findall("valhalla:name", ns)[0].text,
                                       "map": port_type.findall("valhalla:map", ns)[0].text,
                                       "color": port_type.findall("valhalla:color", ns)[0].text,
                                       "description": port_type.findall("valhalla:description", ns)[0].text,
                                       "value": None})
            pass
        pprint(self._ports["in"])
        pprint(self._ports["out"])


    def add_input(self, name='input', type=None, multi_input=False, display_name=True,
                  color=None):
        """
        Add input :class:`Port` to node.

        Args:
            name (str): name for the input port.
            multi_input (bool): allow port to have more than one connection.
            display_name (bool): display the port name on the node.
            color (tuple): initial port color (r, g, b) 0-255.

        Returns:
            NodeGraphQt.Port: the created port object.
        """
        if name in self.inputs().keys():
            raise PortRegistrationError(
                'port name "{}" already registered.'.format(name))
        view = self.view.add_input(name, multi_input, display_name)
        if color:
            view.color = color
            view.border_color = [min([255, max([0, i + 80])]) for i in color]
        port = Port(self, view)
        port.model.type_ = IN_PORT
        port.model.name = name
        port.model.display_name = display_name
        port.model.multi_connection = multi_input
        self._inputs.append(port)
        self.model.inputs[port.name()] = port.model
        return port

    def add_output(self, name='output', type=None, multi_output=True, display_name=True,
                   color=None):
        """
        Add output :class:`Port` to node.

        Args:
            name (str): name for the output port.
            multi_output (bool): allow port to have more than one connection.
            display_name (bool): display the port name on the node.
            color (tuple): initial port color (r, g, b) 0-255.

        Returns:
            NodeGraphQt.Port: the created port object.
        """
        if name in self.outputs().keys():
            raise PortRegistrationError(
                'port name "{}" already registered.'.format(name))
        view = self.view.add_output(name, multi_output, display_name)
        if color:
            view.color = color
            view.border_color = [min([255, max([0, i + 80])]) for i in color]
        port = Port(self, view)
        port.model.type_ = OUT_PORT
        port.model.name = name
        port.model.display_name = display_name
        port.model.multi_connection = multi_output
        self._outputs.append(port)
        self.model.outputs[port.name()] = port.model
        return port

    @abstractmethod
    def get_category(self):
        return self._category

    @abstractmethod
    def evaluate(self):
        pass

