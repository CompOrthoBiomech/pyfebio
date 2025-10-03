import meshio

import pyfebio as feb

from_gmsh = meshio.gmsh.read("../../assets/gmsh/hex27_contact.msh")
mesh = feb.mesh.translate_meshio(from_gmsh)

my_model = feb.model.Model(mesh=mesh)

for i, part in enumerate(my_model.mesh.elements):
    mat = feb.material.NeoHookean(
        name=part.name,
        id=i + 1,
        E=feb.material.MaterialParameter(text=1.0),
        v=feb.material.MaterialParameter(text=0.3),
    )
    my_model.material.add_material(mat)
    my_model.mesh_domains.add_solid_domain(
        feb.meshdomains.SolidDomain(name=part.name, mat=part.name)
    )

my_model.mesh.add_surface_pair(
    feb.mesh.SurfacePair(name="contact", primary="bottom-box-top", secondary="top-box-bottom")
)
my_model.boundary.add_bc(
    feb.boundary.BCZeroDisplacement(node_set="bottom-box-bottom", x_dof=1, y_dof=1, z_dof=1)
)
my_model.boundary.add_bc(
    feb.boundary.BCZeroDisplacement(node_set="top-box-top", x_dof=0, y_dof=1, z_dof=0)
)
my_model.boundary.add_bc(
    feb.boundary.BCPrescribedDisplacement(
        node_set="top-box-top", dof="z", value=feb.boundary.Value(lc=1, text=-0.15)
    )
)
my_model.boundary.add_bc(
    feb.boundary.BCPrescribedDisplacement(
        node_set="top-box-top", dof="x", value=feb.boundary.Value(lc=1, text=0.3)
    )
)
my_model.contact.add_contact(
    feb.contact.SlidingElastic(
        name="sliding_contact", surface_pair="contact", auto_penalty=1, laugon="AUGLAG", two_pass=1
    )
)
my_model.load_data.add_load_curve(
    feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0,0", "1,1"]))
)
my_model.output.add_plotfile(
    feb.output.OutputPlotfile(
        all_vars=[
            feb.output.Var(type="displacement"),
            feb.output.Var(type="contact pressure"),
            feb.output.Var(type="contact gap"),
        ]
    )
)
my_model.save("contact.feb")
feb.model.run_model("contact.feb")
