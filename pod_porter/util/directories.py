"""
utilities for directories
"""

import os
import tempfile
import shutil
from uuid import uuid4


def create_temp_working_directory() -> str:
    """Create a temporary working directory

    :rtype: str
    :returns: The path to the temporary working directory
    """
    working_directory = os.path.join(tempfile.gettempdir(), str(uuid4()))

    os.makedirs(working_directory)

    return working_directory


def delete_temp_working_directory(working_directory: str) -> None:
    """Delete the temporary working directory

    :type working_directory: str
    :param working_directory: The path to the temporary working

    :rtype: None
    :returns: Nothing it deletes the directory
    """
    shutil.rmtree(working_directory)
