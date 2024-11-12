"""
utility functions for reading and writing files
"""

import os
import tarfile
from pod_porter.render.render import Render


def write_file(path: str, file_name: str, data: str) -> None:
    """Write data to a file

    :type path: str
    :param path: The path to the file
    :type file_name: str
    :param file_name: The name of the file
    :type data: str
    :param data: The data to write to the file

    :rtype: None
    :returns: Nothing it writes the data to the file
    """
    with open(os.path.join(path, file_name), "w", encoding="utf-8", newline="\n") as file:
        file.write(data)


def create_new_map(map_name_and_path: str) -> None:
    """Create a new map

    :type map_name_and_path: str
    :param map_name_and_path: The full path to create the new map

    :rtype: None
    :returns: Nothing it creates the new map
    """
    os.makedirs(map_name_and_path)
    map_templates_path = os.path.join(map_name_and_path, "templates")
    os.mkdir(map_templates_path)
    render_vars = {"data": {"map_name": os.path.split(map_name_and_path)[1]}}

    render = Render()

    map_file = render.from_file(template_name="new-map.j2", render_vars=render_vars)
    values_file = render.from_file(template_name="new-values.j2", render_vars=render_vars)
    service_file = render.from_file(template_name="new-service.j2", render_vars=render_vars)
    volumes_file = render.from_file(template_name="new-volumes.j2", render_vars=render_vars)

    write_file(path=map_name_and_path, file_name="Map.yaml", data=map_file)
    write_file(path=map_name_and_path, file_name="values.yaml", data=values_file)
    write_file(path=map_templates_path, file_name="service-example.yaml", data=service_file)
    write_file(path=map_templates_path, file_name="volumes-example.yaml", data=volumes_file)


def create_tar_gz_file(path: str, file_name: str, output_path: str) -> None:
    """Create a tar.gz file

    :type path: str
    :param path: The path to the directory to tar.gz
    :type file_name: str
    :param file_name: The name of the file
    :type output_path: str
    :param output_path: The path to save the tar.gz file

    :rtype: None
    :returns: Nothing it creates the tar.gz file
    """
    with tarfile.open(os.path.join(output_path, file_name), "w:gz") as tar:
        tar.add(path, arcname=os.path.basename(path))


def extract_tar_gz_file(path: str, output_path: str) -> None:
    """Extract a tar.gz file

    :type path: str
    :param path: The full path to the tar.gz
    :type output_path: str
    :param output_path: The path to save the extracted files

    :rtype: None
    :returns: Nothing it extracts the tar.gz file
    """
    with tarfile.open(path, "r:gz") as tar:
        tar.extractall(path=output_path)
