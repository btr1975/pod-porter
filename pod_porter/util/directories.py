"""
utilities for directories
"""

from pathlib import Path
import tempfile
import shutil
from uuid import uuid4


def create_temp_working_directory() -> str:
    """Create a temporary working directory

    :rtype: str
    :returns: The path to the temporary working directory
    """
    working_directory = Path(tempfile.gettempdir()).joinpath(str(uuid4()))
    working_directory.mkdir(exist_ok=True)

    return working_directory.as_posix()


def delete_temp_working_directory(working_directory: str) -> None:
    """Delete the temporary working directory

    :type working_directory: str
    :param working_directory: The path to the temporary working

    :rtype: None
    :returns: Nothing it deletes the directory
    """
    shutil.rmtree(working_directory)
