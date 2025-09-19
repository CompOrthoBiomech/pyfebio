from typing import List, Literal, Optional, Union

import meshio
import numpy as np
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
    StringUIntVec9,
    StringUIntVec10,
    StringUIntVec15,
    StringUIntVec20,
    StringUIntVec27,
)

SolidFEBioElementType = Literal["tet4", "tet10", "tet15", "hex8", "hex20", "hex27", "penta6"]
ShellFEBioElementType = Literal["tri3", "tri6", "quad4", "quad8", "quad9", "q4ans", "q4eas"]
BeamFEBioElementType = Literal["line2", "line3"]


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


class Tet10Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec10 = Field(default="1,2,3,4,5,6,7,8,9,10")
    id: int = attr()


class Tet15Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec15 = Field(default="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15")
    id: int = attr()


class Hex8Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec8 = Field(default="1,2,3,4,5,6,7,8")
    id: int = attr()


class Hex20Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec20 = Field(default="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20")
    id: int = attr()


class Hex27Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec27 = Field(
        default="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27"
    )
    id: int = attr()


class Penta6Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec6 = Field(default="1,2,3,4,5,6")
    id: int = attr()


class Tri3Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec3 = Field(default="1,2,3")
    id: int = attr()


class Tri6Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec6 = Field(default="1,2,3,4,5,6")
    id: int = attr()


class Quad4Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec4 = Field(default="1,2,3,4")
    id: int = attr()


class Quad8Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec8 = Field(default="1,2,3,4,5,6,7,8")
    id: int = attr()


class Quad9Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec9 = Field(default="1,2,3,4,5,6,7,8,9")
    id: int = attr()


class Line2Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec2 = Field(default="1,2")
    id: int = attr()


class Line3Element(BaseXmlModel, tag="elem", validate_assignment=True):
    text: StringUIntVec3 = Field(default="1,2,3")
    id: int = attr()


ElementType = Union[
    Tet4Element,
    Tet10Element,
    Tet15Element,
    Hex8Element,
    Hex20Element,
    Hex27Element,
    Penta6Element,
    Tri3Element,
    Tri6Element,
    Quad4Element,
    Quad8Element,
    Quad9Element,
    Line2Element,
    Line3Element,
]


class Elements(BaseXmlModel, tag="elements", validate_assignment=True):
    name: str = attr(default="Part")
    type: SolidFEBioElementType | ShellFEBioElementType | BeamFEBioElementType = attr(
        default="hex8"
    )
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
    all_tri3: List[Tri3Element] = element(default=[], tag="tri3")
    all_tri6: List[Tri6Element] = element(default=[], tag="tri6")
    all_quad4: List[Quad4Element] = element(default=[], tag="quad4")
    all_quad8: List[Quad8Element] = element(default=[], tag="quad8")
    all_quad9: List[Quad9Element] = element(default=[], tag="quad9")

    def add_tri3(self, new_tri: Tri3Element):
        self.all_tri3.append(new_tri)

    def add_tri6(self, new_tri: Tri6Element):
        self.all_tri6.append(new_tri)

    def add_quad4(self, new_quad: Quad4Element):
        self.all_quad4.append(new_quad)

    def add_quad8(self, new_quad: Quad8Element):
        self.all_quad8.append(new_quad)

    def add_quad9(self, new_quad: Quad9Element):
        self.all_quad9.append(new_quad)


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


ELEMENT_MAP: dict[str, SolidFEBioElementType | ShellFEBioElementType | BeamFEBioElementType] = {
    "tetra": "tet4",
    "tetra10": "tet10",
    "hexahedron": "hex8",
    "hexahedron20": "hex20",
    "hexahedron27": "hex27",
    "triangle": "tri3",
    "triangle6": "tri6",
    "quad": "quad4",
    "quad8": "quad8",
    "quad9": "quad9",
    "line": "line2",
    "line3": "line3",
}
ELEMENT_CLASS_MAP: dict[str, type[ElementType]] = {
    "tet4": Tet4Element,
    "tet10": Tet10Element,
    "hex8": Hex8Element,
    "hex20": Hex20Element,
    "hex27": Hex27Element,
    "tri3": Tri3Element,
    "tri6": Tri6Element,
    "quad4": Quad4Element,
    "quad8": Quad8Element,
    "quad9": Quad9Element,
    "line2": Line2Element,
    "line3": Line3Element,
}

EXCLUDE_SET_STR = ("gmsh:bounding_entities",)


def translate_meshio(
    meshobj: meshio.Mesh,
    nodeoffset: int = 0,
    elementoffset: int = 0,
    surfaceoffset: int = 0,
    shell_sets: Optional[list[str]] = None,
) -> Mesh:
    if shell_sets is None:
        shell_sets = []
    solid_nodes = []
    for key, value in meshobj.cells_dict.items():
        if meshio._mesh.topological_dimension[key] == 3:
            solid_nodes.extend(np.unique(value.ravel()).tolist())
    solid_nodes = set(solid_nodes)

    make_element = {}
    for key, values in meshobj.cells_dict.items():
        make_element[key] = []
        if meshio._mesh.topological_dimension[key] == 2:
            for element in values:
                make_element[key].append(
                    bool(set(np.unique(element.ravel())).difference(solid_nodes))
                )
        else:
            make_element[key].extend([True] * len(values))

    febio_mesh = Mesh()
    nodes_object = Nodes()
    for i, node in enumerate(meshobj.points):
        nodes_object.add_node(Node(id=i + 1 + nodeoffset, text=",".join(map(str, node))))
    num_elements = 0
    num_surface_elements = 0
    for name, members in meshobj.cell_sets_dict.items():
        if any([exclude in name.lower() for exclude in EXCLUDE_SET_STR]):
            continue
        shell_set = name in shell_sets
        for member, offsets in members.items():
            if len(members.keys()) > 1:
                set_name = f"{name}_{ELEMENT_MAP[member]}"
            else:
                set_name = name
            etype = ELEMENT_MAP[member]
            if shell_set or np.array(make_element[member])[offsets].all():
                elements_object = Elements(name=set_name, type=etype)
                for offset in offsets:
                    element = meshobj.cells_dict[member][offset]
                    num_elements += 1
                    elements_object.add_element(
                        ELEMENT_CLASS_MAP[etype](
                            id=num_elements + elementoffset,
                            text=",".join(map(str, element + 1)),
                        )
                    )
                febio_mesh.elements.append(elements_object)
            else:
                surface_object = Surface(name=set_name)
                fn_map = {
                    "tri3": surface_object.add_tri3,
                    "tri6": surface_object.add_tri6,
                    "quad4": surface_object.add_quad4,
                    "quad8": surface_object.add_quad8,
                    "quad9": surface_object.add_quad9,
                }
                node_set = []
                for offset in offsets:
                    num_surface_elements += 1
                    element = meshobj.cells_dict[member][offset]
                    fn_map[ELEMENT_MAP[member]](
                        ELEMENT_CLASS_MAP[etype](
                            id=num_surface_elements + surfaceoffset,
                            text=",".join(map(str, element + 1)),
                        )
                    )
                    node_set.extend((element + 1).tolist())
                node_sets = sorted(set(node_set))
                febio_mesh.node_sets.append(
                    NodeSet(name=set_name, text=",".join(map(str, node_sets)))
                )
                febio_mesh.surfaces.append(surface_object)
    febio_mesh.nodes.append(nodes_object)
    return febio_mesh
