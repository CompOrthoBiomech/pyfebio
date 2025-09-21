from typing import get_args

import pyfebio as feb


def test_unconstrained_material(hex8_febmesh, tmp_path):
    for material_cls in get_args(feb.material.UnconstrainedMaterials):
        my_model = feb.model.Model(mesh=hex8_febmesh)
        for i, element in enumerate(my_model.mesh.elements):
            my_mat = material_cls(name=element.name, id=i + 1)
            if hasattr(my_mat, "mat_axis"):
                my_mat.mat_axis = feb.material.MaterialAxisVector()
            elif hasattr(my_mat, "fiber"):
                my_mat.fiber = feb.material.FiberVector()
            my_model.material.add_material(my_mat)
            my_model.mesh_domains.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
        model_file = tmp_path.joinpath(f"{my_model.material.all_materials[0].type.replace(' ', '_')}.feb")
        my_model.save(model_file)
        result = feb.model.run_model(model_file)
        assert result.returncode == 0, f"{material_cls.__name__} failed"


def test_efd_donnan_equilibrium(hex8_febmesh, tmp_path):
    my_model = feb.model.Model(mesh=hex8_febmesh)
    for i, element in enumerate(my_model.mesh.elements):
        my_mat = feb.material.EllipsoidalFiberDistributionDonnanEquilibrium(
            name=element.name, id=i + 1, cF0=feb.material.DynamicMaterialParameter(lc=i + 1, text=1)
        )
        my_model.material.add_material(my_mat)
        my_model.mesh_domains.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
        my_model.load_data.add_load_curve(
            feb.loaddata.LoadCurve(id=i + 1, points=feb.loaddata.CurvePoints(points=["0,0", "1,150"]))
        )
    my_model.boundary.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    model_file = tmp_path.joinpath(f"{my_model.material.all_materials[0].type.replace(' ', '_')}.feb")
    my_model.save(model_file)
    result = feb.model.run_model(model_file, silent=True)
    assert result.returncode == 0


def test_osmotic_virial_pressure(hex20_febmesh, tmp_path):
    my_model = feb.model.Model(mesh=hex20_febmesh)
    for i, element in enumerate(my_model.mesh.elements):
        my_mat = feb.material.SolidMixture(name=element.name, id=i + 1)
        my_mat.add_solid(
            feb.material.OsmoticVirialPressure(id=i + 1, cr=feb.material.DynamicMaterialParameter(lc=i + 1, text=5000.0))
        )
        my_mat.add_solid(feb.material.ContinuousFiberDistribution())
        my_model.material.add_material(my_mat)
        my_model.mesh_domains.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
        my_model.load_data.add_load_curve(
            feb.loaddata.LoadCurve(id=i + 1, interpolate="SMOOTH", points=feb.loaddata.CurvePoints(points=["0,0", "1,1"]))
        )
    my_model.boundary.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    model_file = tmp_path.joinpath(f"{my_model.material.all_materials[0].type.replace(' ', '_')}.feb")
    my_model.save(model_file)
    result = feb.model.run_model(model_file, silent=False)
    assert result.returncode == 0


def test_uncoupled_material(hex8_febmesh, tmp_path):
    for material_cls in get_args(feb.material.UncoupledMaterials):
        my_model = feb.model.Model(mesh=hex8_febmesh)
        for i, element in enumerate(my_model.mesh.elements):
            my_mat = material_cls(name=element.name, id=i + 1)
            if hasattr(my_mat, "mat_axis"):
                my_mat.mat_axis = feb.material.MaterialAxisVector()
            elif hasattr(my_mat, "fiber"):
                my_mat.fiber = feb.material.FiberVector()
            my_model.material.add_material(my_mat)
            my_model.mesh_domains.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
        model_file = tmp_path.joinpath(f"{my_model.material.all_materials[0].type.replace(' ', '_')}.feb")
        my_model.save(model_file)
        result = feb.model.run_model(model_file, silent=True)
        assert result.returncode == 0, f"{material_cls.__name__} failed"
