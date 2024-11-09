"""
Pod Porter Main Application
"""

from typing import List
import os
from yaml import safe_load, safe_dump
from pod_porter.render.render import Render


class PorterMap:
    """A class to represent the PorterMap

    :type path: str
    :param path: The path to the directory containing the map.yaml and values.yaml files

    :rtype: None
    :returns: Nothing
    """

    def __init__(self, path: str) -> None:
        self.path = path

        self._map_data = self._get_map()
        self._values_data = self._get_values()
        self._templates = self._get_templates()
        self._compose = {}
        self._services = self._get_service_templates()
        self._configs = self._get_config_templates()
        self._volumes = self._get_volume_templates()
        self._secrets = self._get_secrets_templates()
        self._networks = self._get_network_templates()

        if not self._map_data:
            raise ValueError("map_data is empty")

        if not self._values_data:
            raise ValueError("values_data is empty")

    @staticmethod
    def get_yaml_data(path: str) -> dict:
        """Load the data from a yaml file and return it

        :type path: str
        :param path: The path to the yaml file

        :rtype: dict
        :returns: The data from the yaml
        """
        with open(path, "r") as file:
            data = safe_load(file.read())

        return data

    def _get_templates(self) -> List[str]:
        """Get a list of all the template files in the templates directory

        :rtype: List[str]
        :returns: A list of all the template files in the templates directory
        """
        template_files = []
        templates_path = os.path.join(self.path, "templates")

        for item in os.listdir(templates_path):
            if os.path.isfile(os.path.join(templates_path, item)):
                template_files.append(os.path.abspath(os.path.join(templates_path, item)))

        return template_files

    def _get_compose_type_data(self, compose_type: str) -> dict:
        """Get the data for a specific compose type from the templates

        :type compose_type: str
        :param compose_type: The compose type to get the data for

        :rtype: dict
        :returns: The data for the compose type
        """
        services = {compose_type: {}}
        for template in self._templates:
            template_dict = self.get_yaml_data(template)
            if template_dict.get(compose_type):
                services.get(compose_type).update(template_dict[compose_type])

        return services

    def _get_service_templates(self) -> dict:
        """Get the service data from the templates

        :rtype: dict
        :returns: The service data from the templates
        """
        services = self._get_compose_type_data("services")

        self._compose.update(services)

        return services

    def _get_volume_templates(self) -> dict:
        """Get the volume data from the templates

        :rtype: dict
        :returns: The volume data from the templates
        """
        volumes = self._get_compose_type_data("volumes")

        self._compose.update(volumes)

        return volumes

    def _get_network_templates(self) -> dict:
        """Get the network data from the templates

        :rtype: dict
        :returns: The network data from the templates
        """
        networks = self._get_compose_type_data("networks")

        self._compose.update(networks)

        return networks

    def _get_config_templates(self) -> dict:
        """Get the config data from the templates

        :rtype: dict
        :returns: The config data from the templates
        """
        configs = self._get_compose_type_data("configs")

        self._compose.update(configs)

        return configs

    def _get_secrets_templates(self) -> dict:
        """Get the secrets data from the templates

        :rtype: dict
        :returns: The secrets data from the templates
        """
        secrets = self._get_compose_type_data("secrets")

        self._compose.update(secrets)

        return secrets

    def _get_map(self) -> dict:
        """Load the map.yaml file and return the data

        :rtype: dict
        :returns: The data from the map.yaml
        """
        map_path = os.path.join(self.path, "map.yaml")

        if not os.path.isfile(map_path):
            raise FileNotFoundError("map.yaml not found")

        return self.get_yaml_data(map_path)

    def _get_values(self) -> dict:
        """Load the values.yaml file and return the data

        :rtype: dict
        :returns: The data from the values.yaml
        """
        values_path = os.path.join(self.path, "values.yaml")

        if not os.path.isfile(values_path):
            raise FileNotFoundError("values.yaml not found")

        return {"values": self.get_yaml_data(values_path)}

    def render_compose(self) -> str:
        """Render the compose file

        :rtype: str
        :returns: The rendered compose file
        """
        render_obj = Render()
        data = render_obj.from_string(template_string=safe_dump(self._compose), render_vars=self._values_data)
        return render_obj.from_file(template_name="compose-layout.j2", render_vars={"compose_data": data})
