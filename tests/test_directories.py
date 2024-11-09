import os
import pytest
from pod_porter.util.directories import create_temp_working_directory, delete_temp_working_directory


def test_create_temp_working_directory():
    working_directory = create_temp_working_directory()
    assert os.path.exists(working_directory)
    delete_temp_working_directory(working_directory)
    assert not os.path.exists(working_directory)
