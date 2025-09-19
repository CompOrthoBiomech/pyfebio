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


def test_translate_tet4_mesh(tet4_meshio):
    mesh = feb.mesh.translate_meshio(tet4_meshio)
    assert mesh.nodes
    assert mesh.elements


def test_translate_tet10_mesh(tet10_meshio):
    mesh = feb.mesh.translate_meshio(tet10_meshio)
    assert mesh.nodes
    assert mesh.elements
    my_model = feb.model.Model(mesh=mesh)
    for i, element in enumerate(mesh.elements):
        my_model.material.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.mesh_domains.add_solid_domain(
            feb.meshdomains.SolidDomain(name=element.name, mat=element.name)
        )
    my_model.boundary.add_bc(
        feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1)
    )
    my_model.boundary.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,2.0"),
        )
    )
    my_model.load_data.add_load_curve(
        feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"]))
    )

    my_model.save("tet10.feb")


def test_translate_hex8_mesh(hex8_meshio):
    mesh = feb.mesh.translate_meshio(hex8_meshio)
    assert mesh.nodes
    assert mesh.elements


def test_translate_hex20_mesh(hex20_meshio):
    mesh = feb.mesh.translate_meshio(hex20_meshio)
    assert mesh.nodes
    assert mesh.elements
    my_model = feb.model.Model(mesh=mesh)
    for i, element in enumerate(mesh.elements):
        my_model.material.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.mesh_domains.add_solid_domain(
            feb.meshdomains.SolidDomain(name=element.name, mat=element.name)
        )
    my_model.save("hex20.feb")


def test_translate_hex27_mesh(hex27_meshio):
    mesh = feb.mesh.translate_meshio(hex27_meshio)
    assert mesh.nodes
    assert mesh.elements
