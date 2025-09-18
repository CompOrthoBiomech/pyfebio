from pyfebio import material, meshdomains, model


def test_instantiate_model():
    my_model = model.Model()
    assert isinstance(my_model, model.Model)


def test_add_tet4_mesh(tet4_febmesh):
    my_model = model.Model(mesh=tet4_febmesh)

    for i, part in enumerate(tet4_febmesh.elements):
        my_model.material.add_material(material.NeoHookean(id=i + 1, name=part.name))
        my_model.mesh_domains.add_solid_domain(
            meshdomains.SolidDomain(name=part.name, mat=part.name)
        )


def test_add_tet10_mesh(tet10_febmesh):
    my_model = model.Model(mesh=tet10_febmesh)

    for i, part in enumerate(tet10_febmesh.elements):
        my_model.material.add_material(material.NeoHookean(id=i + 1, name=part.name))
        my_model.mesh_domains.add_solid_domain(
            meshdomains.SolidDomain(name=part.name, mat=part.name)
        )


def test_add_hex8_mesh(hex8_febmesh):
    my_model = model.Model(mesh=hex8_febmesh)

    for i, part in enumerate(hex8_febmesh.elements):
        my_model.material.add_material(material.NeoHookean(id=i + 1, name=part.name))
        my_model.mesh_domains.add_solid_domain(
            meshdomains.SolidDomain(name=part.name, mat=part.name)
        )


def test_add_hex20_mesh(hex20_febmesh):
    my_model = model.Model(mesh=hex20_febmesh)

    for i, part in enumerate(hex20_febmesh.elements):
        my_model.material.add_material(material.NeoHookean(id=i + 1, name=part.name))
        my_model.mesh_domains.add_solid_domain(
            meshdomains.SolidDomain(name=part.name, mat=part.name)
        )


def test_add_hex27_mesh(hex27_febmesh):
    my_model = model.Model(mesh=hex27_febmesh)

    for i, part in enumerate(hex27_febmesh.elements):
        my_model.material.add_material(material.NeoHookean(id=i + 1, name=part.name))
        my_model.mesh_domains.add_solid_domain(
            meshdomains.SolidDomain(name=part.name, mat=part.name)
        )
