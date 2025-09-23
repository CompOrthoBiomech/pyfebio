import math
import subprocess
from pathlib import Path
from typing import Optional, Union

from pydantic_xml import BaseXmlModel, attr, element

from .boundary import Boundary
from .constraints import Constraints
from .contact import Contact
from .control import Control, Solver
from .discrete import Discrete
from .globals import Globals
from .include import Include
from .initial import Initial
from .loaddata import LoadData
from .loads import Loads
from .material import Material, RigidBody
from .mesh import (
    Elements,
    Mesh,
    Node,
    Nodes,
    Tet4Element,
)
from .meshadaptor import MeshAdaptor
from .meshdata import MeshData
from .meshdomains import MeshDomains, SolidDomain
from .module import Module
from .output import Output
from .rigid import Rigid
from .step import Step

SectionTypes = Union[
    Module,
    Globals,
    Control,
    Material,
    RigidBody,
    MeshDomains,
    Mesh,
    MeshData,
    Discrete,
    LoadData,
    Loads,
    Rigid,
    Initial,
    Boundary,
    Contact,
    Constraints,
    Step,
    Output,
    Include,
]


class FEBioRoot(BaseXmlModel, tag="febio_spec", validate_assignment=True):
    version: str = attr(default="4.0")
    sections: list[SectionTypes] = element(default=[])

    def add_section(self, section: SectionTypes):
        self.sections.append(section)

    def save(self, filename: str):
        xml = self.to_xml(
            pretty_print=True,
            encoding="ISO-8859-1",
            xml_declaration=True,
            skip_empty=True,
        )
        with open(filename, "wb") as fid:
            fid.write(xml)  # type: ignore


class Model(BaseXmlModel, tag="febio_spec", validate_assignment=True):
    version: str = attr(default="4.0")
    module: Optional[Module] = element(default=Module(), tag="Module")
    globals: Globals = element(default=Globals(), tag="Globals")
    control: Optional[Control] = element(default=Control(), tag="Control")
    material: Material = element(default=Material(), tag="Material")
    mesh: Mesh = element(default=Mesh(), tag="Mesh")
    mesh_domains: MeshDomains = element(default=MeshDomains(), tag="MeshDomains")
    mesh_data: MeshData = element(default=MeshData(), tag="MeshData")
    meshadaptor: MeshAdaptor = element(default=MeshAdaptor())
    discrete: Discrete = element(default=Discrete(), tag="Discrete")
    load_data: LoadData = element(default=LoadData(), tag="LoadData")
    loads: Loads = element(default=Loads(), tag="Loads")
    rigid: Rigid = element(default=Rigid(), tag="Rigid")
    initial: Initial = element(default=Initial(), tag="Initial")
    boundary: Boundary = element(default=Boundary(), tag="Boundary")
    contact: Contact = element(default=Contact(), tag="Contact")
    constraints: Constraints = element(default=Constraints(), tag="Constraints")
    step: Step = element(default=Step(), tag="Step")
    output: Output = element(default=Output(), tag="Output")

    def save(self, filename: str):
        xml = self.to_xml(
            pretty_print=True,
            encoding="ISO-8859-1",
            xml_declaration=True,
            skip_empty=True,
        )
        with open(filename, "wb") as fid:
            fid.write(xml)  # type: ignore

    def add_simple_rigid_body(self, origin: tuple[float, float, float], name: str):
        element_id = self.mesh.elements[-1].all_elements[-1].id + 1
        node_id_start = self.mesh.nodes[-1].all_nodes[-1].id + 1
        connectivity = [node_id for node_id in range(node_id_start, node_id_start + 4)]
        sqrt3over2 = math.sqrt(3.0) / 2.0
        ideal_tet = [
            [-1.0, -sqrt3over2, -sqrt3over2],
            [1.0, -sqrt3over2, -sqrt3over2],
            [0.0, sqrt3over2, -sqrt3over2],
            [0.0, 0.0, sqrt3over2],
        ]
        new_tet = [[tet[i] + origin[i] for tet in ideal_tet] for i in range(3)]
        nodes = [Node(id=node_id_start + i, text=",".join(map(str, new_tet[i]))) for i in range(4)]
        node_domain = Nodes(name=name, all_nodes=nodes)
        element = Tet4Element(id=element_id, text=",".join(map(str, connectivity)))
        element_domain = Elements(name=name, all_elements=[element], type="tet4")
        self.mesh.add_node_domain(node_domain)
        self.mesh.add_element_domain(element_domain)

        material_id = self.material.all_materials[-1].id + 1

        material = RigidBody(name=name, id=material_id)
        self.material.add_material(material)
        self.mesh_domains.add_solid_domain(SolidDomain(name=name, mat=name))


class BiphasicModel(Model):
    module: Optional[Module] = element(default=Module(type="biphasic"))
    control: Optional[Control] = element(default=Control(analysis="STEADY-STATE", solver=Solver(type="biphasic", ptol=0.01)))


def run_model(filepath: str | Path, silent: bool = False) -> subprocess.CompletedProcess:
    if silent:
        return subprocess.run(f"febio4 -i {filepath} -silent", shell=True)
    else:
        return subprocess.run(f"febio4 -i {filepath}", shell=True)
