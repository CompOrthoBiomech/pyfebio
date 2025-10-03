import meshio

import pyfebio as feb

from_gmsh = meshio.gmsh.read("../../assets/gmsh/hex8.msh")
mesh = feb.mesh.translate_meshio(from_gmsh)

my_model = feb.model.Model(
    mesh=mesh, control=feb.control.Control(time_steps=10, step_size=0.1, time_stepper=None)
)

for i, part in enumerate(my_model.mesh.elements):
    mat = feb.material.NeoHookean(
        name=part.name,
        id=i + 1,
        E=feb.material.MaterialParameter(text=10.0 * (i + 1)),
        v=feb.material.MaterialParameter(text=0.3),
    )
    my_model.material.add_material(mat)
    my_model.mesh_domains.add_solid_domain(
        feb.meshdomains.SolidDomain(name=part.name, mat=part.name)
    )

fix_bottom = my_model.boundary.add_bc(
    feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1)
)

move_top = my_model.boundary.add_bc(
    feb.boundary.BCPrescribedDisplacement(
        node_set="top", dof="z", value=feb.boundary.Value(lc=1, text=0.5)
    )
)

my_model.load_data.add_load_curve(
    feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "1.0,1.0"]))
)
adaptor = feb.meshadaptor.HexRefineAdaptor(
    elem_set="bottom-layer",
    max_iters=2,
    criterion=feb.meshadaptor.RelativeErrorCriterion(
        error=0.01, data=feb.meshadaptor.StressCriterion()
    ),
)
my_model.meshadaptor.add_adaptor(adaptor)

my_model.output.add_plotfile(
    feb.output.OutputPlotfile(
        all_vars=[
            feb.output.Var(type="displacement"),
            feb.output.Var(type="stress error"),
        ]
    )
)

my_model.save("mesh_adapt.feb")
feb.model.run_model("mesh_adapt.feb")
