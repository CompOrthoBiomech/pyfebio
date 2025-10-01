import meshio

import pyfebio as feb

from_gmsh = meshio.gmsh.read("../../assets/gmsh/hex20.msh")
mesh = feb.mesh.translate_meshio(from_gmsh)

my_model = feb.model.Model(mesh=mesh)

for i, part in enumerate(my_model.mesh.elements):
    mat = feb.material.NeoHookean(
        name=part.name,
        id=i + 1,
        E=feb.material.MaterialParameter(text=1.0 * (i + 1)),
        v=feb.material.MaterialParameter(text=0.3),
    )
    my_model.material.add_material(mat)
    my_model.mesh_domains.add_solid_domain(
        feb.meshdomains.SolidDomain(name=part.name, mat=part.name)
    )

fix_bottom = my_model.boundary.add_bc(
    feb.boundary.BCZeroDisplacement(node_set="bottom", x_dof=1, y_dof=1, z_dof=1)
)

twist_top = my_model.boundary.add_bc(
    feb.boundary.BCRigidDeformation(
        node_set="top", pos="0.5,0.5,0.0", rot=feb.boundary.Value(lc=1, text="0.0,0.0,3.14")
    )
)

my_model.load_data.add_load_curve(
    feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "1.0,1.0"]))
)

my_model.save("elastic_hex20.feb")
feb.model.run_model("elastic_hex20.feb")
