import pytest
from pod_porter.util.schemas import MapSchema


map_schema_table = [
    ("map_data", None),
    ("map_data_bad_api_version", ValueError),
    ("map_data_bad_name", ValueError),
    ("map_data_bad_description", ValueError),
    ("map_data_bad_version", ValueError),
    ("map_data_bad_app_version", ValueError),
]


@pytest.mark.parametrize("data, error", map_schema_table)
def test_map_schema(data, error, request, map_data_as_json, map_data_as_dict, map_data_as_yaml):
    if error:
        with pytest.raises(error):
            MapSchema(**request.getfixturevalue(data))

    else:
        obj = MapSchema(**request.getfixturevalue(data))
        assert obj.dict() == map_data_as_dict
        assert obj.json() == map_data_as_json
        assert obj.yaml() == map_data_as_yaml
