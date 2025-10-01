import meshio

import pyfebio as feb

from_gmsh = meshio.gmsh.read("../../assets/gmsh/hex20.msh")
mesh = feb.mesh.translate_meshio(from_gmsh)

my_model = feb.model.BiphasicModel(mesh=mesh)

for i, part in enumerate(my_model.mesh.elements):
    mat = feb.material.BiphasicMaterial(
        name=part.name,
        id=i + 1,
        solid=feb.material.NeoHookean(id=i + 1),
        permeability=feb.material.ConstantIsoPerm(
            perm=feb.material.MaterialParameter(text=1e-3 * (i + 1))
        ),
    )
    my_model.material.add_material(mat)
    my_model.mesh_domains.add_solid_domain(
        feb.meshdomains.SolidDomain(name=part.name, mat=part.name)
    )

fix_bottom = my_model.boundary.add_bc(
    feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1)
)

drain_top = my_model.boundary.add_bc(feb.boundary.BCZeroFluidPressure(node_set="top"))

move_top = my_model.boundary.add_bc(
    feb.boundary.BCPrescribedDisplacement(
        node_set="top", dof="z", value=feb.boundary.Value(lc=1, text=-0.5)
    )
)

my_model.load_data.add_load_curve(
    feb.loaddata.LoadCurve(
        id=1, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "0.1,1.0", "1.0,1.0"])
    )
)
my_model.output.add_plotfile(
    feb.output.OutputPlotfile(
        all_vars=[
            feb.output.Var(type="displacement"),
            feb.output.Var(type="effective fluid pressure"),
        ]
    )
)

my_model.save("biphasic_hex20.feb")
feb.model.run_model("biphasic_hex20.feb")
