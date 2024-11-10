import os, sys
import pytest
import json
import yaml

base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


def helper_get_file_data(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    return data


@pytest.fixture
def base_data_path() -> str:
    return os.path.join(str(base_path), "tests", "data")


@pytest.fixture
def templates_path(base_data_path) -> str:
    return os.path.join(base_data_path, "templates")


@pytest.fixture
def single_map_path(base_data_path) -> str:
    return os.path.join(base_data_path, "single_map", "mongo")


@pytest.fixture
def single_map_rendered_path(base_data_path) -> str:
    return os.path.join(base_data_path, "single_map", "rendered.yaml")


@pytest.fixture
def single_map_rendered_path_other_values(base_data_path) -> str:
    return os.path.join(base_data_path, "other-values-files", "rendered.yaml")


@pytest.fixture
def multi_map_path(base_data_path) -> str:
    return os.path.join(base_data_path, "multi_map", "mongo")


@pytest.fixture
def multi_map_rendered_path(base_data_path) -> str:
    return os.path.join(base_data_path, "multi_map", "rendered.yaml")


@pytest.fixture
def map_path_bad_values(base_data_path) -> str:
    return os.path.join(base_data_path, "bad_maps", "bad-values-file")


@pytest.fixture
def map_path_bad_map(base_data_path) -> str:
    return os.path.join(base_data_path, "bad_maps", "bad-maps-file")


@pytest.fixture
def map_path_no_map(base_data_path) -> str:
    return os.path.join(base_data_path, "bad_maps", "no-maps-file")


@pytest.fixture
def other_values_file(base_data_path) -> str:
    return os.path.join(base_data_path, "other-values-files", "other1.yaml")


@pytest.fixture
def map_data(base_data_path) -> dict:
    return yaml.safe_load(helper_get_file_data(os.path.join(base_data_path, "good_maps", "map.json")))


@pytest.fixture
def map_data_bad_api_version() -> dict:
    data = {
        "api_version": "v5",
        "name": "mongo",
        "description": "MongoDB map",
        "version": "1.0.0",
        "app_version": "4.4.0",
    }

    return data


@pytest.fixture
def map_data_bad_name() -> dict:
    data = {
        "api_version": "v1",
        "name": "mongo something",
        "description": "MongoDB map",
        "version": "1.0.0",
        "app_version": "4.4.0",
    }

    return data


@pytest.fixture
def map_data_bad_description() -> dict:
    data = {
        "api_version": "v1",
        "name": "mongo",
        "description": " MongoDB map",
        "version": "1.0.0",
        "app_version": "4.4.0",
    }

    return data


@pytest.fixture
def map_data_bad_version() -> dict:
    data = {
        "api_version": "v1",
        "name": "mongo",
        "description": "MongoDB map",
        "version": "1.0.bad",
        "app_version": "4.4.0",
    }

    return data


@pytest.fixture
def map_data_bad_app_version() -> dict:
    data = {
        "api_version": "v1",
        "name": "mongo",
        "description": "MongoDB map",
        "version": "1.0.0",
        "app_version": "4.bad.0",
    }

    return data


@pytest.fixture
def map_data_as_yaml(base_data_path) -> str:
    return helper_get_file_data(os.path.join(base_data_path, "good_maps", "map.yaml"))


@pytest.fixture
def map_data_as_json(base_data_path) -> str:
    return helper_get_file_data(os.path.join(base_data_path, "good_maps", "map.json"))


@pytest.fixture
def map_data_as_dict(base_data_path) -> dict:
    return json.loads(helper_get_file_data(os.path.join(base_data_path, "good_maps", "map.json")))
