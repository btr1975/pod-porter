"""
utility functions for reading and writing files
"""

import os
import tarfile


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
