import pytest
from pod_porter.pod_porter import PorterMapsRunner


porter_map_runner_table = [
    ("single_map_path", "single_map_rendered_path", "other_values_none"),
    ("single_map_path", "single_map_rendered_path_other_values", "other_values_file"),
    ("multi_map_path", "multi_map_rendered_path", "other_values_none"),
    ("multi_map_path", "multi_map_rendered_path", "other_values_file_with_global"),
    ("multi_map_with_ignore_path", "multi_map_with_ignore_rendered_path", "other_values_none"),
]


@pytest.mark.parametrize("map_path, map_render, other_values", porter_map_runner_table)
def test_porter_map(map_path, map_render, other_values, request):
    obj = PorterMapsRunner(
        path=request.getfixturevalue(map_path),
        release_name="thing",
        values_override=request.getfixturevalue(other_values),
    )

    assert obj.render_compose() == open(request.getfixturevalue(map_render), "r").read()
    assert str(obj) == f'PorterMapRunner(path="{request.getfixturevalue(map_path)}", release_name="thing")'


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
