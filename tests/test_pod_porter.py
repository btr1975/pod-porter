import pytest
from pod_porter.pod_porter import PorterMapsRunner


def test_porter_map_runner_single(single_map_path, single_map_rendered_path):
    obj = PorterMapsRunner(path=single_map_path, release_name="thing")

    assert obj.render_compose() == open(single_map_rendered_path, "r").read()
    assert str(obj) == f'PorterMapRunner(path="{single_map_path}", release_name="thing")'


def test_porter_map_other_values(single_map_path, single_map_rendered_path_other_values, other_values_file):
    obj = PorterMapsRunner(path=single_map_path, release_name="thing", values_override=other_values_file)

    assert obj.render_compose() == open(single_map_rendered_path_other_values, "r").read()
    assert str(obj) == f'PorterMapRunner(path="{single_map_path}", release_name="thing")'


def test_porter_map_runner_multi(multi_map_path, multi_map_rendered_path):
    obj = PorterMapsRunner(path=multi_map_path, release_name="thing")

    assert obj.render_compose() == open(multi_map_rendered_path, "r").read()
    assert str(obj) == f'PorterMapRunner(path="{multi_map_path}", release_name="thing")'


porter_map_runner_bad_table = [
    ("map_path_bad_map", TypeError),
    ("map_path_bad_values", FileNotFoundError),
    ("map_path_no_map", FileNotFoundError),
]


@pytest.mark.parametrize("path, error", porter_map_runner_bad_table)
def test_porter_map_runner_bad(path, error, request):
    if error:
        with pytest.raises(error):
            PorterMapsRunner(path=request.getfixturevalue(path), release_name="thing")
