"""
Pod Porter Main Application
"""

from typing import List, Optional
import os
from yaml import safe_load, safe_dump
from pod_porter.render.render import Render
from pod_porter.util.directories import create_temp_working_directory, delete_temp_working_directory
from pod_porter.util.file_read_write import write_file
from pod_porter.util.schemas import MapSchema


class _PorterMap:  # pylint: disable=too-many-instance-attributes
    """A class to represent the PorterMap

    :type path: str
    :param path: The path to the directory containing the map.yaml and values.yaml files
    :type release_name: Optional[str] = None
    :param release_name: The name of the release
    :type values_override: values_override: Optional[str] = None
    :param values_override: The path to the yaml to override with

    :rtype: None
    :returns: Nothing
    """

    def __init__(self, path: str, release_name: Optional[str] = None, values_override: Optional[str] = None) -> None:
        self._temp_working_directory = create_temp_working_directory()
        self._path = path
        self._release_name = release_name or "release-name"
        self._map_data = self._get_map()
        self._values_data = self._get_values(values_override=values_override)

        if not self._map_data:
            raise ValueError("map_data is empty")

        self._templates = self._get_templates(templates_path=os.path.join(self._path, "templates"))
        self._pre_render()
        self._templates_pre_render = self._get_templates(templates_path=self._temp_working_directory)
        self._compose = {}
        self._services = self._get_service_templates()
        self._configs = self._get_config_templates()
        self._volumes = self._get_volume_templates()
        self._secrets = self._get_secrets_templates()
        self._networks = self._get_network_templates()

    def __repr__(self) -> str:
        """Return the string representation of the object

        :rtype: str
        :returns: The string representation of the object
        """
        return f'PorterMap(path="{self._path}", release_name="{self._release_name}")'

    def get_services(self) -> dict:
        """Get the services data

        :rtype: dict
        :returns: The services data
        """
        return self._services

    def get_configs(self) -> dict:
        """Get the configs data

        :rtype: dict
        :returns: The configs data
        """
        return self._configs

    def get_volumes(self) -> dict:
        """Get the volumes data

        :rtype: dict
        :returns: The volumes data
        """
        return self._volumes

    def get_secrets(self) -> dict:
        """Get the secrets data

        :rtype: dict
        :returns: The secrets data
        """
        return self._secrets

    def get_networks(self) -> dict:
        """Get the networks data

        :rtype: dict
        :returns: The networks data
        """
        return self._networks

    def get_temp_working_directory(self) -> str:
        """Get the temp working directory

        :rtype: str
        :returns: The working directory
        """
        return self._temp_working_directory

    def get_map_data(self) -> MapSchema:
        """Get the map data

        :rtype: MapSchema
        :returns: The map data
        """
        return self._map_data

    @staticmethod
    def get_yaml_data(path: str) -> dict:
        """Load the data from a yaml file and return it

        :type path: str
        :param path: The path to the yaml file

        :rtype: dict
        :returns: The data from the yaml
        """
        with open(path, "r", encoding="utf-8") as file:
            data = safe_load(file.read())

        return data

    @staticmethod
    def _get_templates(templates_path: str) -> List[str]:
        """Get a list of all the template files in the templates directory

        :type templates_path: str
        :param templates_path: The path to the templates directory

        :rtype: List[str]
        :returns: A list of all the template files in the templates directory
        """
        template_files = []

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
        for template in self._templates_pre_render:
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

    def _get_map(self) -> MapSchema:
        """Load the map.yaml file and return the data

        :rtype: MapSchema
        :returns: The validated data from the map.yaml
        """
        map_path = os.path.join(self._path, "Map.yaml")

        if not os.path.isfile(map_path):
            raise FileNotFoundError("Map.yaml not found")

        return MapSchema(**self.get_yaml_data(map_path))

    def _get_values(self, values_override: Optional[str] = None) -> dict:
        """Load the values.yaml file and return the data

        :rtype: dict
        :returns: The data from the values.yaml
        """
        if not values_override:
            values_path = os.path.join(self._path, "values.yaml")

        else:
            values_path = values_override

        if not os.path.isfile(values_path):
            raise FileNotFoundError(f"values file '{values_path}' not found")

        return {"values": self.get_yaml_data(values_path), "release": {"name": self._release_name}}

    def _pre_render(self) -> None:
        """Pre-render the templates from the map

        :rtype: None
        :returns: Nothing it writes rendered templates to the temp working directory
        """
        templates_path = os.path.join(self._path, "templates")
        render_obj = Render(templates_dir=templates_path)
        for path in self._templates:
            template = os.path.split(path)[1]
            write_file(
                self._temp_working_directory,
                template,
                render_obj.from_file(template_name=template, render_vars=self._values_data),
            )


class PorterMapsRunner:  # pylint: disable=too-many-instance-attributes
    """A class to represent the PorterMapRunner for collecting and running maps

    :type path: str
    :param path: The path to the directory containing the map.yaml and values.yaml files
    :type release_name: Optional[str] = None
    :param release_name: The name of the release

    :rtype: None
    :returns: Nothing
    """

    def __init__(self, path: str, release_name: Optional[str] = None, values_override: Optional[str] = None) -> None:
        self._path = path
        self._release_name = release_name or "release-name"
        self._values_override = values_override
        self._toplevel_map_data = None
        self._all_maps = self._collect_maps()
        self._services = {"services": {}}
        self._configs = {"configs": {}}
        self._volumes = {"volumes": {}}
        self._secrets = {"secrets": {}}
        self._networks = {"networks": {}}
        self._compose = {}
        self._merge_maps()

    def __repr__(self) -> str:
        """Return the string representation of the object

        :rtype: str
        :returns: The string representation of the object
        """
        return f'PorterMapRunner(path="{self._path}", release_name="{self._release_name}")'

    def get_map_data(self) -> MapSchema:
        """Get the map data

        :rtype: MapSchema
        :returns: The map data
        """
        return self._toplevel_map_data

    def _collect_maps(self) -> List[_PorterMap]:
        """Collect all the maps in the directory

        :rtype: List[_PorterMap]
        :returns: A list of PorterMap objects
        """
        top_level_map = _PorterMap(
            path=self._path, release_name=self._release_name, values_override=self._values_override
        )

        self._toplevel_map_data = top_level_map.get_map_data()

        maps = [top_level_map]

        if os.path.isdir(os.path.join(self._path, "maps")):
            for single_map in os.listdir(os.path.join(self._path, "maps")):
                maps.append(
                    _PorterMap(path=os.path.join(self._path, "maps", single_map), release_name=self._release_name)
                )

        return maps

    def render_compose(self) -> str:
        """Render the compose file

        :rtype: str
        :returns: The rendered compose file
        """
        render_obj = Render()
        return render_obj.from_file(
            template_name="compose-layout.j2", render_vars={"compose_data": safe_dump(self._compose)}
        )

    def _merge_maps(self) -> None:
        """Merge all the maps into a single compose file

        :rtype: None
        :returns: Nothing
        """
        for single_map in self._all_maps:
            self._services["services"].update(single_map.get_services().get("services"))
            self._configs["configs"].update(single_map.get_configs().get("configs"))
            self._volumes["volumes"].update(single_map.get_volumes().get("volumes"))
            self._secrets["secrets"].update(single_map.get_secrets().get("secrets"))
            self._networks["networks"].update(single_map.get_networks().get("networks"))
            delete_temp_working_directory(single_map.get_temp_working_directory())
        self._compose.update(self._services)
        self._compose.update(self._configs)
        self._compose.update(self._volumes)
        self._compose.update(self._secrets)
        self._compose.update(self._networks)
