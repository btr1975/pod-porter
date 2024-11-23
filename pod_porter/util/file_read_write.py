"""
utility functions for reading and writing files
"""

import os
import tarfile
import fnmatch
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


def get_ignore_patterns(ignore_file_path: str) -> list:
    """Get the list of files and directories to ignore

    :type ignore_file_path: str
    :param ignore_file_path: The path to the ignore file

    :rtype: list
    :returns: A list of files and directories to ignore
    """
    ignore_list = []
    if not os.path.isfile(ignore_file_path):
        return ignore_list

    with open(ignore_file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("#"):
                continue

            if line.strip() == "":
                continue

            ignore_list.append(line.strip())

    return ignore_list


def should_ignore(path: str, patterns: list) -> bool:
    """Check if a file or directory should be ignored

    :type path: str
    :param path: The full path to the file or directory
    :type patterns: list
    :param patterns: The list of files and directories to ignore

    :rtype: bool
    :returns: True if the file or directory should be ignored, False otherwise
    """
    for pattern in patterns:
        if pattern.startswith("!"):
            if path.startswith(pattern[1:]):
                return False

        if fnmatch.fnmatch(path, pattern):
            return True

        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True

    return False


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
    ignore_file = render.from_file(template_name="new-porterignore.j2", render_vars=render_vars)
    service_file = render.from_file(template_name="new-service.j2", render_vars=render_vars)
    volumes_file = render.from_file(template_name="new-volumes.j2", render_vars=render_vars)

    write_file(path=map_name_and_path, file_name="Map.yaml", data=map_file)
    write_file(path=map_name_and_path, file_name="values.yaml", data=values_file)
    write_file(path=map_name_and_path, file_name=".porterignore", data=ignore_file)
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
    exclude_patters = get_ignore_patterns(os.path.join(path, ".porterignore"))
    with tarfile.open(os.path.join(output_path, file_name), "w:gz") as tar:
        for dir_path, dir_names, file_names in os.walk(path):
            for pattern in exclude_patters:
                if pattern.endswith("/"):
                    if os.path.normpath(pattern) in dir_names:
                        dir_names.remove(os.path.normpath(pattern))
                    continue

            for file in file_names:
                file_path = os.path.join(dir_path, file)

                if should_ignore(file_path, exclude_patters):
                    continue

                tar.add(file_path, arcname=os.path.join(os.path.basename(path), os.path.relpath(file_path, path)))


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
