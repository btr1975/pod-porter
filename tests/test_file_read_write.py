import os
import pytest
from pod_porter.util.file_read_write import write_file


def test_write_file(tmp_path):
    path = tmp_path

    write_file(path=str(path), file_name="test.txt", data="Hello, World!")

    assert os.path.exists(path / "test.txt")
