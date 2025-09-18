from pathlib import Path

import meshio
import pytest

from pyfebio import mesh

GMSH_DIR = Path(__file__).parent.joinpath("../../assets/gmsh")

SOLID_SETS = ["bottom-layer", "top-layer"]
SURFACE_ELEMENTS = ["bottom", "top", "left", "right", "front", "back"]


@pytest.fixture(scope="session")
def tet4_meshio():
    return meshio.gmsh.read(GMSH_DIR.joinpath("tet4.msh"))


@pytest.fixture(scope="session")
def tet10_meshio():
    return meshio.gmsh.read(GMSH_DIR.joinpath("tet10.msh"))


@pytest.fixture(scope="session")
def hex8_meshio():
    return meshio.gmsh.read(GMSH_DIR.joinpath("hex8.msh"))


@pytest.fixture(scope="session")
def hex20_meshio():
    return meshio.gmsh.read(GMSH_DIR.joinpath("hex20.msh"))


@pytest.fixture(scope="session")
def hex27_meshio():
    return meshio.gmsh.read(GMSH_DIR.joinpath("hex27.msh"))


@pytest.fixture(scope="session")
def tet4_febmesh(tet4_meshio):
    febmesh = mesh.Mesh()
    nodes_object = mesh.Nodes(name="tet4_nodes")
    for i, node in enumerate(tet4_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    febmesh.nodes.append(nodes_object)

    for name, entries in tet4_meshio.cell_sets.items():
        if name in SOLID_SETS:
            elements_object = mesh.Elements(name=name, type="tet4")
            for i, indices in enumerate(entries):
                cell_block = tet4_meshio.cells[i]
                for j in indices:
                    elements_object.add_element(
                        mesh.Tet4Element(
                            id=j + 1, text=",".join(map(str, cell_block.data[j, :] + 1))
                        )
                    )
            febmesh.elements.append(elements_object)
    return febmesh


@pytest.fixture(scope="session")
def tet10_febmesh(tet10_meshio):
    febmesh = mesh.Mesh()
    nodes_object = mesh.Nodes(name="tet10_nodes")
    for i, node in enumerate(tet10_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    febmesh.nodes.append(nodes_object)

    for name, entries in tet10_meshio.cell_sets.items():
        if name in SOLID_SETS:
            elements_object = mesh.Elements(name=name, type="tet10")
            for i, indices in enumerate(entries):
                cell_block = tet10_meshio.cells[i]
                for j in indices:
                    elements_object.add_element(
                        mesh.Tet10Element(
                            id=j + 1, text=",".join(map(str, cell_block.data[j, :] + 1))
                        )
                    )
            febmesh.elements.append(elements_object)
    return febmesh


@pytest.fixture(scope="session")
def hex8_febmesh(hex8_meshio):
    febmesh = mesh.Mesh()
    nodes_object = mesh.Nodes(name="hex8_nodes")
    for i, node in enumerate(hex8_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    febmesh.nodes.append(nodes_object)

    for name, entries in hex8_meshio.cell_sets.items():
        if name in SOLID_SETS:
            elements_object = mesh.Elements(name=name, type="hex8")
            for i, indices in enumerate(entries):
                cell_block = hex8_meshio.cells[i]
                for j in indices:
                    elements_object.add_element(
                        mesh.Hex8Element(
                            id=j + 1, text=",".join(map(str, cell_block.data[j, :] + 1))
                        )
                    )
            febmesh.elements.append(elements_object)
    return febmesh


@pytest.fixture(scope="session")
def hex20_febmesh(hex20_meshio):
    febmesh = mesh.Mesh()
    nodes_object = mesh.Nodes(name="hex20_nodes")
    for i, node in enumerate(hex20_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    febmesh.nodes.append(nodes_object)

    for name, entries in hex20_meshio.cell_sets.items():
        if name in SOLID_SETS:
            elements_object = mesh.Elements(name=name, type="hex20")
            for i, indices in enumerate(entries):
                cell_block = hex20_meshio.cells[i]
                for j in indices:
                    elements_object.add_element(
                        mesh.Hex20Element(
                            id=j + 1, text=",".join(map(str, cell_block.data[j, :] + 1))
                        )
                    )
            febmesh.elements.append(elements_object)
    return febmesh


@pytest.fixture(scope="session")
def hex27_febmesh(hex27_meshio):
    febmesh = mesh.Mesh()
    nodes_object = mesh.Nodes(name="hex27_nodes")
    for i, node in enumerate(hex27_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    febmesh.nodes.append(nodes_object)

    for name, entries in hex27_meshio.cell_sets.items():
        if name in SOLID_SETS:
            elements_object = mesh.Elements(name=name, type="hex27")
            for i, indices in enumerate(entries):
                cell_block = hex27_meshio.cells[i]
                for j in indices:
                    elements_object.add_element(
                        mesh.Hex27Element(
                            id=j + 1, text=",".join(map(str, cell_block.data[j, :] + 1))
                        )
                    )
            febmesh.elements.append(elements_object)
    return febmesh
