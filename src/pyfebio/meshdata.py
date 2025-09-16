from typing import List, Literal, Union

from pydantic_xml import BaseXmlModel, attr, element

from ._types import (
    StringFloatVec3,
)


class NodeDataNode(BaseXmlModel, tag="node", validate_assignment=True):
    lid: int = attr(ge=1)
    text: Union[float, StringFloatVec3]


class NodeData(BaseXmlModel, validate_assignment=True):
    name: str = attr()
    node_set: str = attr()
    data_type: Literal["scalar", "vec3"] = attr()
    all_nodes: List[NodeDataNode] = element(default=[], tag="node")

    def add_node(self, new_node: NodeDataNode):
        self.all_nodes.append(new_node)


class ElementDataElement(BaseXmlModel, tag="elem", validate_assignment=True):
    lid: int = attr(ge=1)
    text: Union[float, StringFloatVec3]


class ElementData(BaseXmlModel, validate_assignment=True):
    name: str = attr()
    elem_set: str = attr()
    data_type: Literal["scalar", "vec3"] = attr()
    all_elements: List[ElementDataElement] = element(default=[], tag="elem")

    def add_element(self, new_element: ElementDataElement):
        self.all_elements.append(new_element)


class SurfaceData(BaseXmlModel, validate_assignment=True):
    pass


class MeshData(BaseXmlModel, validate_assignment=True):
    element_data: List[ElementData] = element(default=[], tag="ElementData")
    node_data: List[NodeData] = element(default=[], tag="NodeData")

    def add_element_data(self, new_element_data: ElementData):
        self.element_data.append(new_element_data)

    def add_node_data(self, new_node_data: NodeData):
        self.node_data.append(new_node_data)
