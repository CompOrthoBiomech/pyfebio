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
            my_model.mesh_domains.add_solid_domain(
                feb.meshdomains.SolidDomain(name=element.name, mat=element.name)
            )
        model_file = tmp_path.joinpath(
            f"{my_model.material.all_materials[0].type.replace(' ', '_')}.feb"
        )
        my_model.save(model_file)
        result = feb.model.run_model(model_file)
        assert result.returncode == 0
