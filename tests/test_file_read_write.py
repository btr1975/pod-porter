import os
import shutil
import pytest
from pod_porter.util.file_read_write import write_file, create_tar_gz_file, extract_tar_gz_file, create_new_map


def test_write_file(tmp_path):
    path = tmp_path

    write_file(path=str(path), file_name="test.txt", data="Hello, World!")

    assert os.path.exists(path / "test.txt")


create_tar_gz_file_table = [
    ("single_map_path"),
    ("multi_map_path"),
    ("multi_map_with_ignore_path"),
]


@pytest.mark.parametrize("map_type", create_tar_gz_file_table)
def test_create_tar_gz_file(tmp_path, map_type, request):
    the_temp_path_path = str(tmp_path)
    tar_file_name = "test.tar.gz"
    dst_path = os.path.join(the_temp_path_path, "mongo")

    shutil.copytree(request.getfixturevalue(map_type), dst_path)

    create_tar_gz_file(
        path=os.path.join(the_temp_path_path, "mongo"), file_name=tar_file_name, output_path=the_temp_path_path
    )

    assert os.path.exists(os.path.join(the_temp_path_path, tar_file_name))

    shutil.rmtree(dst_path)

    extract_tar_gz_file(path=os.path.join(the_temp_path_path, tar_file_name), output_path=the_temp_path_path)

    assert os.path.exists(os.path.join(the_temp_path_path, dst_path))


def test_create_new_map(tmp_path):
    the_temp_path_path = str(tmp_path)
    map_name = "test-map"

    create_new_map(map_name_and_path=os.path.join(the_temp_path_path, map_name))

    assert os.path.exists(os.path.join(the_temp_path_path, map_name))
