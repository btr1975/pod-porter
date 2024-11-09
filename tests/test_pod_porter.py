import pytest
from pod_porter.pod_porter import PorterMapsRunner
from tests.conftest import map_path_bad_map, map_path_bad_values


def test_porter_map_runner_single(single_map_path, single_map_rendered_path):
    obj = PorterMapsRunner(path=single_map_path, release_name="thing")

    assert obj.render_compose() == open(single_map_rendered_path, "r").read()
    assert str(obj) == f'PorterMapRunner(path="{single_map_path}", release_name="thing")'


def test_porter_map_runner_multi(multi_map_path, multi_map_rendered_path):
    obj = PorterMapsRunner(path=multi_map_path, release_name="thing")

    assert obj.render_compose() == open(multi_map_rendered_path, "r").read()
    assert str(obj) == f'PorterMapRunner(path="{multi_map_path}", release_name="thing")'


porter_map_runner_bad_table = [
    (map_path_bad_map, ValueError),
]


@pytest.mark.parametrize("path, error", porter_map_runner_bad_table)
def test_porter_map_runner_bad(path, error, base_data_path):

    with pytest.raises(error):
        PorterMapsRunner(path=path(base_data_path), release_name="thing")
