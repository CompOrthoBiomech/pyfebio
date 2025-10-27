from copy import deepcopy
from typing import get_args

import pytest

import pyfebio as feb


@pytest.fixture(scope="module")
def base_model(hex8_contact_febmesh):
    my_model = feb.model.Model(mesh_=hex8_contact_febmesh)
    for i, part in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(
            feb.material.NeoHookean(
                id=i + 1,
                name=part.name,
                E=feb.material.MaterialParameter(text=100.0),
                v=feb.material.MaterialParameter(text=0.1),
            )
        )
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=part.name, mat=part.name))
    my_model.mesh_.add_surface_pair(feb.mesh.SurfacePair(name="contact", primary="bottom-box-top", secondary="top-box-bottom"))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom-box-bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="top-box-top", x_dof=1, y_dof=1, z_dof=0))
    my_model.boundary_.add_bc(
        feb.boundary.BCPrescribedDisplacement(node_set="top-box-top", dof="z", value=feb.boundary.Value(lc=1, text=-0.15))
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))
    my_model.output_.add_plotfile(
        feb.output.OutputPlotfile(
            all_vars=[
                feb.output.Var(type="displacement"),
                feb.output.Var(type="contact pressure"),
                feb.output.Var(type="contact gap"),
            ]
        )
    )
    return my_model


@pytest.fixture(scope="module")
def base_biphasic_model(hex20_contact_febmesh):
    my_model = feb.model.BiphasicModel(mesh_=hex20_contact_febmesh)
    for i, part in enumerate(my_model.mesh_.elements):
        mat = feb.material.BiphasicMaterial(
            name=part.name,
            id=i + 1,
            solid=feb.material.NeoHookean(id=i + 1, E=feb.material.MaterialParameter(text=1.0), v=feb.material.MaterialParameter(text=0.1)),
            permeability=feb.material.ConstantIsoPerm(),
        )
        my_model.material_.add_material(mat)
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=part.name, mat=part.name))
    my_model.mesh_.add_surface_pair(feb.mesh.SurfacePair(name="contact", primary="bottom-box-top", secondary="top-box-bottom"))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom-box-bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="top-box-top", x_dof=1, y_dof=1, z_dof=0))
    my_model.boundary_.add_bc(
        feb.boundary.BCPrescribedDisplacement(node_set="top-box-top", dof="z", value=feb.boundary.Value(lc=1, text=-0.1))
    )
    my_model.boundary_.add_bc(feb.boundary.BCZeroFluidPressure(node_set="top-box-left"))
    my_model.boundary_.add_bc(feb.boundary.BCZeroFluidPressure(node_set="bottom-box-left"))
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "0.1,1", "1,1"])))
    my_model.output_.add_plotfile(
        feb.output.OutputPlotfile(
            all_vars=[
                feb.output.Var(type="displacement"),
                feb.output.Var(type="nodal fluid flux"),
                feb.output.Var(type="fluid pressure"),
                feb.output.Var(type="contact pressure"),
                feb.output.Var(type="contact gap"),
            ]
        )
    )
    return my_model


def test_sliding_contact(base_model, tmp_path):
    for contact_cls in get_args(feb.contact.SlidingContactType):
        my_model = deepcopy(base_model)
        my_model.contact_.add_contact(contact_cls(name="sliding_contact", surface_pair="contact", auto_penalty=1, laugon="AUGLAG"))
        my_model.save(tmp_path / f"{contact_cls.__name__}.feb")
        result = feb.model.run_model(tmp_path / f"{contact_cls.__name__}.feb")
        assert result == 0, f"Failed to run model for {contact_cls.__name__}"


def test_biphasic_sliding_contact(base_biphasic_model, tmp_path):
    for contact_cls in get_args(feb.contact.SlidingBiphasicContactType):
        my_model = deepcopy(base_biphasic_model)
        my_model.contact_.add_contact(contact_cls(name="sliding_contact", surface_pair="contact", auto_penalty=1, laugon="AUGLAG"))
        my_model.save(tmp_path / f"{contact_cls.__name__}.feb")
        result = feb.model.run_model(tmp_path / f"{contact_cls.__name__}.feb")
        assert result == 0, f"Failed to run model for {contact_cls.__name__}"
