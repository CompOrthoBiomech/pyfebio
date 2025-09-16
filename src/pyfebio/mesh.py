from enum import Enum
from typing import List, Literal, Union

from pydantic import Field
from pydantic_xml import BaseXmlModel, attr, element

from ._types import (
    StringFloatVec3,
    StringUIntVec,
    StringUIntVec2,
    StringUIntVec3,
    StringUIntVec4,
    StringUIntVec6,
    StringUIntVec8,
)


class FEBioElementType(str, Enum):
    TRI3 = "tri3"
    QUAD4 = "quad4"
    TET4 = "tet4"
    HEX8 = "hex8"
    PENTA6 = "penta6"


class Node(BaseXmlModel, tag="node", validate_assignment=True):
    text: StringFloatVec3 = Field(default="0.0, 0.0, 0.0")
    id: int = attr()


class Nodes(BaseXmlModel, validate_assignment=True):
    name: str = attr(default="")
    all_nodes: List[Node] = element(tag="node", default=[])

    def add_node(self, new_node: Node):
        self.all_nodes.append(new_node)


class Tet4Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec4 = Field(default="1,2,3,4")
    id: int = attr()


class Hex8Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec8 = Field(default="1,2,3,4,5,6,7,8")
    id: int = attr()


class Penta6Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec6 = Field(default="1,2,3,4,5,6")
    id: int = attr()


class Tri3Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec3 = Field(default="1,2,3")
    id: int = attr()


class Quad4Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec4 = Field(default="1,2,3,4")
    id: int = attr()


ElementType = Union[Tet4Element, Hex8Element, Penta6Element, Tri3Element, Quad4Element]


class Elements(BaseXmlModel, tag="elements", validate_assignment=True):
    name: str = attr(default="Part")
    type: Literal[
        FEBioElementType.HEX8,
        FEBioElementType.TET4,
        FEBioElementType.PENTA6,
        FEBioElementType.TRI3,
        FEBioElementType.QUAD4,
    ] = attr(default="hex8")
    all_elements: List[ElementType] = element(default=[], tag="elem")

    def add_element(self, new_element: ElementType):
        self.all_elements.append(new_element)


class ElementSet(BaseXmlModel, tag="ElementSet", validate_assignment=True):
    name: str = attr(default="")
    text: StringUIntVec

    def add_element(self, new_element_id: int):
        ",".join([self.text, str(new_element_id)])


class NodeSet(BaseXmlModel, tag="NodeSet", validate_assignment=True):
    name: str = attr(default="")
    text: StringUIntVec

    def add_node(self, new_node_id: int):
        ",".join([self.text, str(new_node_id)])


class Surface(BaseXmlModel, tag="Surface", validate_assignment=True):
    name: str = attr(default="")
    all_quads: List[Quad4Element] = element(default=[], tag="quad4")
    all_tris: List[Tri3Element] = element(default=[], tag="tri3")

    def add_quad(self, new_quad: Quad4Element):
        self.all_quads.append(new_quad)

    def add_tri(self, new_tri: Tri3Element):
        self.all_tris.append(new_tri)


class SurfacePair(BaseXmlModel, tag="SurfacePair", validate_assignment=True):
    name: str = attr(default="")
    primary: str = element()
    secondary: str = element()


class DiscreteElement(BaseXmlModel, tag="delem", validate_assignment=True):
    text: StringUIntVec2


class DiscreteSet(BaseXmlModel, tag="DiscreteSet", validate_assignment=True):
    name: str = attr(default="")
    elements: List[DiscreteElement] = element(default=[])

    def add_element(self, new_element: DiscreteElement):
        self.elements.append(new_element)


class Mesh(BaseXmlModel, validate_assignment=True):
    nodes: List[Nodes] = element(default=[], tag="Nodes")
    elements: List[Elements] = element(default=[], tag="Elements")
    surfaces: List[Surface] = element(default=[], tag="Surface")
    element_sets: List[ElementSet] = element(default=[], tag="ElementSet")
    node_sets: List[NodeSet] = element(default=[], tag="NodeSet")
    discrete_sets: List[DiscreteSet] = element(default=[], tag="DiscreteSet")
    surface_pairs: List[SurfacePair] = element(default=[], tag="SurfacePair")

    def add_node_domain(self, new_node_domain: Nodes):
        if not new_node_domain.name:
            new_node_domain.name = f"Part{len(self.nodes) + 1}"
        self.nodes.append(new_node_domain)

    def add_element_domain(self, new_element_domain: Elements):
        if new_element_domain.name == "Part":
            new_element_domain.name = f"Part{len(self.elements) + 1}"
        self.elements.append(new_element_domain)

    def add_surface(self, new_surface: Surface):
        if not new_surface.name:
            new_surface.name = f"Surface{len(self.surfaces) + 1}"
        self.surfaces.append(new_surface)

    def add_element_set(self, new_element_set: ElementSet):
        if not new_element_set.name:
            new_element_set.name = f"ElementSet{len(self.element_sets) + 1}"
        self.element_sets.append(new_element_set)

    def add_node_set(self, new_node_set: NodeSet):
        if not new_node_set.name:
            new_node_set.name = f"NodeSet{len(self.node_sets) + 1}"
        self.node_sets.append(new_node_set)

    def add_discrete_set(self, new_discrete_set: DiscreteSet):
        if not new_discrete_set.name:
            new_discrete_set.name = f"DiscreteSet{len(self.discrete_sets) + 1}"
        self.discrete_sets.append(new_discrete_set)

    def add_surface_pair(self, new_surface_pair: SurfacePair):
        if not new_surface_pair.name:
            new_surface_pair.name = f"SurfacePair{len(self.surface_pairs) + 1}"
        self.surface_pairs.append(new_surface_pair)
