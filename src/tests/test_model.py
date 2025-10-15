import pyfebio as feb


def test_instantiate_model():
    my_model = feb.model.Model()
    assert isinstance(my_model, feb.model.Model)


def test_tet4_model(tet4_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=tet4_febmesh)
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14"),
        )
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))
    my_model.save(tmp_path.joinpath("model.feb"))
    result = feb.model.run_model(f"febio4 -i {tmp_path.joinpath('model.feb')}")
    assert result.returncode == 0


def test_tet10_model(tet10_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=tet10_febmesh)
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14"),
        )
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))

    my_model.save(tmp_path.joinpath("model.feb"))
    result = feb.model.run_model(f"febio4 -i {tmp_path.joinpath('model.feb')}")
    assert result.returncode == 0


def test_hex8_model(hex8_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=hex8_febmesh)
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14"),
        )
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))

    my_model.save(tmp_path.joinpath("model.feb"))
    result = feb.model.run_model(f"febio4 -i {tmp_path.joinpath('model.feb')}")
    assert result.returncode == 0


def test_hex20_model(hex20_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=hex20_febmesh)
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14"),
        )
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))

    my_model.save(tmp_path.joinpath("model.feb"))
    result = feb.model.run_model(f"febio4 -i {tmp_path.joinpath('model.feb')}")
    assert result.returncode == 0


def test_hex27_model(hex27_febmesh, tmp_path):
    my_model = feb.model.Model(mesh_=hex27_febmesh)
    for i, element in enumerate(my_model.mesh_.elements):
        my_model.material_.add_material(feb.material.NeoHookean(name=element.name, id=i + 1))
        my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name=element.name, mat=element.name))
    my_model.boundary_.add_bc(feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1))
    my_model.boundary_.add_bc(
        feb.boundary.BCRigidDeformation(
            node_set="top",
            pos="0.5,0.5,0.0",
            rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14"),
        )
    )
    my_model.loaddata_.add_load_curve(feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"])))

    my_model.save(tmp_path.joinpath("model.feb"))
    result = feb.model.run_model(f"febio4 -i {tmp_path.joinpath('model.feb')}")
    assert result.returncode == 0
