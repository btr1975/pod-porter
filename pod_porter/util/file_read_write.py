"""
utility functions for reading and writing files
"""

import os


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
