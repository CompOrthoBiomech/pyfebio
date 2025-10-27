import pyfebio as feb


def test_hex_refine_adaptor(hex8_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=hex8_febmesh, control_=feb.control.Control(time_steps=3, step_size=1 / 3.0, time_stepper=None))
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    adaptor = feb.meshadaptor.HexRefineAdaptor(
        elem_set="bottom-layer",
        max_iters=2,
        criterion=feb.meshadaptor.RelativeErrorCriterion(error=0.01, data=feb.meshadaptor.StressCriterion()),
    )
    my_model.meshadaptor_.add_adaptor(adaptor)
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(feb.boundary.BCPrescribedDisplacement(node_set="top", dof="z", value=feb.boundary.Value(lc=1, text=1.0)))
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))
    my_model.output_.add_plotfile(
        feb.output.OutputPlotfile(all_vars=[feb.output.Var(type="displacement"), feb.output.Var(type="stress error")])
    )
    my_model.save(tmp_path / "hex_refine_adaptor.feb")
    result = feb.model.run_model(tmp_path / "hex_refine_adaptor.feb")
    assert result == 0


def test_mmg_remesh_adaptor(tet4_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=tet4_febmesh, control_=feb.control.Control(time_steps=4, step_size=0.25, time_stepper=None))
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    adaptor = feb.meshadaptor.MMGRemeshAdaptor(
        min_element_size=0.05,
        criterion=feb.meshadaptor.RelativeErrorCriterion(error=0.01, data=feb.meshadaptor.StressCriterion()),
    )
    my_model.meshadaptor_.add_adaptor(adaptor)
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(feb.boundary.BCPrescribedDisplacement(node_set="top", dof="z", value=feb.boundary.Value(lc=1, text=1.0)))
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))
    my_model.output_.add_plotfile(
        feb.output.OutputPlotfile(all_vars=[feb.output.Var(type="displacement"), feb.output.Var(type="stress error")])
    )
    my_model.save(tmp_path / "mmg_remesh_adaptor.feb")
    result = feb.model.run_model(tmp_path / "mmg_remesh_adaptor.feb")
    assert result == 0
