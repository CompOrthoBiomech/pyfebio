from pyfebio import mesh, model


def test_instantiate_model():
    my_model = model.Model()
    assert isinstance(my_model, model.Model)


def test_add_hex8_mesh(hex8_meshio):
    my_model = model.Model()
    nodes_object = mesh.Nodes()
    for i, node in enumerate(hex8_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    elements_object = mesh.Elements()
    for cell_block in hex8_meshio.cells:
        for i in range(cell_block.data.shape[0]):
            elements_object.add_element(
                mesh.Hex8Element(id=i + 1, text=",".join(map(str, cell_block.data[i, :] + 1)))
            )

    my_model.mesh.nodes.append(nodes_object)
    my_model.mesh.elements.append(elements_object)


def test_add_tet4_mesh(tet4_meshio):
    my_model = model.Model()
    nodes_object = mesh.Nodes()
    for i, node in enumerate(tet4_meshio.points):
        nodes_object.add_node(mesh.Node(id=i + 1, text=",".join(map(str, node))))
    elements_object = mesh.Elements(type="tet4")
    for cell_block in tet4_meshio.cells:
        for i in range(cell_block.data.shape[0]):
            elements_object.add_element(
                mesh.Tet4Element(id=i + 1, text=",".join(map(str, cell_block.data[i, :] + 1)))
            )

    my_model.mesh.nodes.append(nodes_object)
    my_model.mesh.elements.append(elements_object)
