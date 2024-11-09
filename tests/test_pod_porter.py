import pytest
from pod_porter.pod_porter import PorterMap


def test_porter_map_single(single_map_path, single_map_rendered_path):
    obj = PorterMap(path=single_map_path, release_name="thing")

    assert obj.render_compose() == open(single_map_rendered_path, "r").read()
