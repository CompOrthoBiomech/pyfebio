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
    return mesh.translate_meshio(tet4_meshio)


@pytest.fixture(scope="session")
def tet10_febmesh(tet10_meshio):
    return mesh.translate_meshio(tet10_meshio)


@pytest.fixture(scope="session")
def hex8_febmesh(hex8_meshio):
    return mesh.translate_meshio(hex8_meshio)


@pytest.fixture(scope="session")
def hex20_febmesh(hex20_meshio):
    return mesh.translate_meshio(hex20_meshio)


@pytest.fixture(scope="session")
def hex27_febmesh(hex27_meshio):
    return mesh.translate_meshio(hex27_meshio)
