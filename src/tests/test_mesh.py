import pytest
from pydantic import ValidationError

import pyfebio as feb

NODE_STRINGS = (
    "-1.0,-1.0,-1.0",
    "1.0,-1.0,-1.0",
    "1.0,1.0,-1.0",
    "-1.0,1.0,-1.0",
    "-1.0,-1.0,1.0",
    "1.0,-1.0,1.0",
    "1.0,1.0,1.0",
    "-1.0,1.0,1.0",
    "0.0,0.0,2.0",
)

TET4_ELEMENT_STRINGS = ("1,2,3,5",)
PENTA6_ELEMENT_STRINGS = ("1,2,3,4,5,8",)
HEX8_ELEMENT_STRINGS = ("1,2,3,4,5,6,7,8",)

TRI3_ELEMENT_STRINGS = ("1,2,3",)
QUAD4_ELEMENT_STRINGS = ("1,2,3,4",)


def test_node_definition():
    feb.mesh.Node(id=1, text=NODE_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Node(id=1, text=("1.,2.,3.,4."))


def test_nodes_definition():
    nodes = feb.mesh.Nodes(name="Nodes1")
    for i, n in enumerate(NODE_STRINGS):
        nodes.add_node(feb.mesh.Node(id=i, text=n))


def test_tet4_element_definition():
    feb.mesh.Tet4Element(id=1, text=TET4_ELEMENT_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Tet4Element(id=1, text=HEX8_ELEMENT_STRINGS[0])


def test_penta6_element_definition():
    feb.mesh.Penta6Element(id=1, text=PENTA6_ELEMENT_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Penta6Element(id=1, text=HEX8_ELEMENT_STRINGS[0])


def test_hex8_element_definition():
    feb.mesh.Hex8Element(id=1, text=HEX8_ELEMENT_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Hex8Element(id=1, text=TET4_ELEMENT_STRINGS[0])


def test_tri3_element_definition():
    feb.mesh.Tri3Element(id=1, text=TRI3_ELEMENT_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Tri3Element(id=1, text=HEX8_ELEMENT_STRINGS[0])


def test_quad4_element_definition():
    feb.mesh.Quad4Element(id=1, text=QUAD4_ELEMENT_STRINGS[0])
    with pytest.raises(ValidationError):
        feb.mesh.Quad4Element(id=1, text=HEX8_ELEMENT_STRINGS[0])
