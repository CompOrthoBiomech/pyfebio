import pyfebio as feb

# manually create the nodes
all_nodes = [
    feb.mesh.Node(id=1, text="-2.0,-1.0,-10"),
    feb.mesh.Node(id=2, text="2.0,-1.0,-10"),
    feb.mesh.Node(id=3, text="2.0,1.0,-10"),
    feb.mesh.Node(id=4, text="-2.0,1.0,-10"),
    feb.mesh.Node(id=5, text="-2.0,-1.0,0"),
    feb.mesh.Node(id=6, text="2.0,-1.0,0"),
    feb.mesh.Node(id=7, text="2.0,1.0,0"),
    feb.mesh.Node(id=8, text="-2.0,1.0,0"),
    feb.mesh.Node(id=9, text="-2.0,-1.0,0"),
    feb.mesh.Node(id=10, text="2.0,-1.0,0"),
    feb.mesh.Node(id=11, text="2.0,1.0,0"),
    feb.mesh.Node(id=12, text="-2.0,1.0,0"),
    feb.mesh.Node(id=13, text="-2.0,-1.0,10"),
    feb.mesh.Node(id=14, text="2.0,-1.0,10"),
    feb.mesh.Node(id=15, text="2.0,1.0,10"),
    feb.mesh.Node(id=16, text="-2.0,1.0,10"),
]

# create a Nodes object
nodes = feb.mesh.Nodes(name="Nodes", all_nodes=all_nodes)

# create Hex8Element for rigid bodies
# each of these is a separate Elements object
# so they are unique parts
body_a = feb.mesh.Elements(name="BodyA", type="hex8", all_elements=[feb.mesh.Hex8Element(id=1, text="1,2,3,4,5,6,7,8")])
body_b = feb.mesh.Elements(name="BodyB", type="hex8", all_elements=[feb.mesh.Hex8Element(id=2, text="9,10,11,12,13,14,15,16")])

# create the base model
my_model = feb.model.Model()
# add the Nodes
my_model.mesh_.add_node_domain(nodes)
# add the Elements (parts)
my_model.mesh_.add_element_domain(body_a)
my_model.mesh_.add_element_domain(body_b)

# create rigid body materials for BodyA and BodyB
my_model.material_.add_material(feb.material.RigidBody(name="BodyA", center_of_mass="0,0,0"))
my_model.material_.add_material(feb.material.RigidBody(name="BodyB", center_of_mass="0,0,0"))
# assign solid domains to the rigid bodies
my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name="BodyA", mat="BodyA"))
my_model.meshdomains_.add_solid_domain(feb.meshdomains.SolidDomain(name="BodyB", mat="BodyB"))

# we need two more rigid bodies for the purpose of creating our
# three cylinder linkage. We use the convenience function
# add_simple_rigid_body() to create these
my_model.add_simple_rigid_body(origin=(0.0, 0.0, 0.0), name="GhostA")
my_model.add_simple_rigid_body(origin=(0.0, 0.0, 0.0), name="GhostB")

# fix BodyA in space
my_model.rigid_.add_rigid_bc(feb.rigid.RigidFixed(rb="BodyA", Rx_dof=1, Ry_dof=1, Rz_dof=1, Ru_dof=1, Rw_dof=1, Rv_dof=1))

# define a RigidCylindricalJoint connector between BodyA and GhostA
# this is the internal-external rotation / inferior-superior translation axis
# prescribe rotation and translation
my_model.rigid_.add_rigid_connector(
    feb.rigid.RigidCylindricalJoint(
        name="IERot_ISTranslation",
        body_a="BodyA",
        body_b="GhostA",
        joint_axis="0.0,0.0,1.0",
        transverse_axis="1.0,0.0,0.0",
        prescribed_rotation=1,
        prescribed_translation=1,
        rotation=feb.rigid.Value(lc=1, text=1.57),
        translation=feb.rigid.Value(lc=2, text=1.0),
    )
)
# define a RigidCylindricalJoint connector between GhostA and GhostB
# this is the varus-valgus rotation / anterior-posterior translation axis
# prescribe rotation and translation
my_model.rigid_.add_rigid_connector(
    feb.rigid.RigidCylindricalJoint(
        name="VVRot_APTranslation",
        body_a="GhostA",
        body_b="GhostB",
        joint_axis="0.0,1.0,0.0",
        transverse_axis="1.0,0.0,0.0",
        prescribed_rotation=1,
        prescribed_translation=1,
        rotation=feb.rigid.Value(lc=3, text=1.57),
        translation=feb.rigid.Value(lc=4, text=1.0),
    )
)
# define a RigidCylindricalJoint connector between GhostB and BodyB
# this is the flexion-extension rotation / medial-lateral translation axis
# prescribe rotation and translation
my_model.rigid_.add_rigid_connector(
    feb.rigid.RigidCylindricalJoint(
        name="Flexion_MLTranslation",
        body_a="GhostB",
        body_b="BodyB",
        joint_axis="1.0,0.0,0.0",
        transverse_axis="0.0,0.0,1.0",
        prescribed_rotation=1,
        prescribed_translation=1,
        rotation=feb.rigid.Value(lc=5, text=1.57),
        translation=feb.rigid.Value(lc=6, text=1.0),
    )
)

# load curve for internal-external rotation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=1, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "0.5,1.0", "1.5,-1.0", "2.0,0.0"]))
)
# load curve for inferior-superior translation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=2, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "2.0,0.0", "2.5,1.0", "3.5,-1.0", "4.0,0.0"]))
)
# load curve for varus-valgus rotation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=3, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "4.0,0.0", "4.5,1.0", "5.5,-1.0", "6.0,0.0"]))
)
# load curve for anterior-posterior translation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=4, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "6.0,0.0", "6.5,1.0", "7.5,-1.0", "8.0,0.0"]))
)
# load curve for flexion-extension rotation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=5, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "8.0,0.0", "8.5,1.0", "9.5,-1.0", "10.0,0.0"]))
)
# load curve for medial-lateral translation
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(id=6, points=feb.loaddata.CurvePoints(points=["0.0,0.0", "10.0,0.0", "10.5,1.0", "11.5,-1.0", "12.0,0.0"]))
)

# must point load curve; note interpolate="STEP"
my_model.loaddata_.add_load_curve(
    feb.loaddata.LoadCurve(
        id=7,
        interpolate="STEP",
        points=feb.loaddata.CurvePoints(points=[f"{i * 0.25},0.25" for i in range(48)]),
    )
)


# change the number of time steps and step_size
# to cover 12 second simulation time
my_model.control_ = feb.control.Control(time_steps=24, step_size=0.5)

# set dtmax of time_stepper to must point load curve
# this guarantees we have a solution at the beginning and end of
# each dof trajectory
my_model.control_.time_stepper.dtmax = feb.control.TimeStepValue(lc=7, text=0.5)

# save and run the model
my_model.save("three_cylinder_joint.feb")
feb.model.run_model("three_cylinder_joint.feb")
