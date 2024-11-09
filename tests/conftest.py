import os, sys
import pytest

base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def base_data_path():
    return os.path.join(str(base_path), "tests", "data")


@pytest.fixture
def templates_path(base_data_path):
    return os.path.join(base_data_path, "templates")


@pytest.fixture
def single_map_path(base_data_path):
    return os.path.join(base_data_path, "single_map", "mongo")


@pytest.fixture
def single_map_rendered_path(base_data_path):
    return os.path.join(base_data_path, "single_map", "rendered.yaml")


@pytest.fixture
def multi_map_path(base_data_path):
    return os.path.join(base_data_path, "multi_map", "mongo")


@pytest.fixture
def multi_map_rendered_path(base_data_path):
    return os.path.join(base_data_path, "multi_map", "rendered.yaml")


def map_path_bad_values(base_data_path):
    return os.path.join(base_data_path, "bad_maps", "bad-values-file")


def map_path_bad_map(base_data_path):
    return os.path.join(base_data_path, "bad_maps", "bad-maps-file")
