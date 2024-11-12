"""
Specific Data Schemas for the Pod Porter Application
"""

from typing import Literal
import json
import re
from dataclasses import dataclass

import yaml


@dataclass
class _BaseSchema:
    """Base Dataclass Schema"""

    def dict(self) -> dict:
        """Get a dict representation of the Dataclass

        :rtype: dict
        :returns: A dict representation of the Dataclass
        """
        return self.__dict__

    def json(self, pretty=False) -> str:
        """Get a JSON representation of the Dataclass

        :type pretty: bool
        :param pretty: Get pretty JSON

        :rtype: str
        :returns: A JSON representation of the Dataclass
        """
        if pretty:
            indent = 4

        else:
            indent = None

        return json.dumps(self.dict(), indent=indent)

    def yaml(self) -> str:
        """Get a YAML representation of the Dataclass

        :rtype: str
        :returns: A YAML representation of the Dataclass
        """
        return yaml.safe_dump(self.dict(), indent=2)

    @staticmethod
    def validate_string(name: str, value: str) -> None:
        """Validate a string

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string, but received {type(value)}")

    @staticmethod
    def validate_string_no_spaces(name: str, value: str) -> None:
        """Validate a string to have no spaces

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        regex = re.compile(r"^\S+$")

        if not regex.match(value):
            raise ValueError(f"{name} must not contain spaces")

    @staticmethod
    def validate_string_no_spaces_begin_end(name: str, value: str) -> None:
        """Validate a string to have no spaces at the beginning or end

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        regex = re.compile(r"^\S.*\S$")

        if not regex.match(value):
            raise ValueError(f"{name} must not contain spaces at the beginning or end")

    @staticmethod
    def validate_api_version(name: str, value: str) -> None:
        """Validate the api version

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        allowed_versions = ["v1"]

        if value not in allowed_versions:
            raise ValueError(f"{name} must be one of {allowed_versions}")

    @staticmethod
    def validate_semantic_version(name: str, value: str) -> None:
        """Validate a string is a semantic version

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        regex = re.compile(r"^\d+\.\d+\.\d+$")

        if not regex.match(value):
            raise ValueError(f"{name} must be a semantic version")


@dataclass
class MapSchema(_BaseSchema):
    """Map.yaml Schema

    :type api_version: Literal["v1"]
    :cvar api_version: Name of the Inventory
    :type name: str
    :cvar name: Name of the Inventory
    :type description: str
    :cvar description: Description of the Inventory
    :type version: str
    :cvar version: Description of the Inventory
    :type app_version: str
    :cvar app_version: Description of the Inventory
    """

    api_version: Literal["v1"]
    name: str
    description: str
    version: str
    app_version: str

    def __post_init__(self):
        self.validate_api_version("api_version", self.api_version)
        self.validate_string_no_spaces("name", self.name)
        self.validate_string_no_spaces_begin_end("description", self.description)
        self.validate_semantic_version("version", self.version)
        self.validate_string_no_spaces("app_version", self.app_version)
