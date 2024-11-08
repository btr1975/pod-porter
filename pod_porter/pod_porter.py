"""

"""

from typing import List
import os
from yaml import safe_load


class PorterMap:

    def __init__(self, path: str) -> None:
        self.path = path

        self.map_data = self._get_map()
        self.values_data = self._get_values()
        self.templates = self._get_templates()
        self.services = self._get_service_templates()
        self.volumes = self._get_volume_templates()

        if not self.map_data:
            raise ValueError("map_data is empty")

        if not self.values_data:
            raise ValueError("values_data is empty")

    @staticmethod
    def get_yaml_data(path: str) -> dict:
        with open(path, "r") as file:
            data = safe_load(file.read())

        return data

    def _get_templates(self) -> List[str]:
        template_files = []
        templates_path = os.path.join(self.path, "templates")

        for item in os.listdir(templates_path):
            if os.path.isfile(os.path.join(templates_path, item)):
                template_files.append(os.path.abspath(os.path.join(templates_path, item)))

        return template_files

    def _get_service_templates(self) -> List[dict]:
        services = []
        for template in self.templates:
            template_dict = self.get_yaml_data(template)
            if template_dict.get("services"):
                services.append(template_dict["services"])

        return services

    def _get_volume_templates(self) -> List[dict]:
        volumes = []
        for template in self.templates:
            template_dict = self.get_yaml_data(template)
            if template_dict.get("volumes"):
                volumes.append(template_dict["volumes"])

        return volumes

    def _get_map(self):
        map_path = os.path.join(self.path, "map.yaml")

        if not os.path.isfile(map_path):
            raise FileNotFoundError("map.yaml not found")

        return self.get_yaml_data(map_path)

    def _get_values(self):
        values_path = os.path.join(self.path, "values.yaml")

        if not os.path.isfile(values_path):
            raise FileNotFoundError("values.yaml not found")

        return self.get_yaml_data(values_path)
