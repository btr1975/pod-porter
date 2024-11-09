"""
Rendering engine
"""

from typing import Optional
import os.path

from jinja2 import Environment, FileSystemLoader, BaseLoader, select_autoescape


class Render:
    """Render the templates class

    :type templates_dir: Optional[str] = None
    :param templates_dir: The directory where the templates are located

    :rtype: None
    :returns: Nothing
    """

    BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_DIRECTORY = os.path.join(BASE_DIRECTORY, "templates")

    def __init__(self, templates_dir: Optional[str] = None) -> None:
        if templates_dir:
            self.templates_dir = templates_dir

        else:
            self.templates_dir = self.TEMPLATE_DIRECTORY

        self.env_file_render = self.__set_template_file_render_environment()
        self.env_string_render = self.__set_template_string_render_environment()

    def __set_template_file_render_environment(self) -> Environment:
        """Private method to set the template file render environment

        :rtype: jinja2.Environment
        :returns: The template file render environment
        """
        return Environment(
            autoescape=select_autoescape(enabled_extensions="yaml", default_for_string=True),
            loader=FileSystemLoader(searchpath=self.templates_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    @staticmethod
    def __set_template_string_render_environment() -> Environment:
        """Private method to set the template string render environment

        :rtype: jinja2.Environment
        :returns: The template file render environment
        """
        return Environment(
            autoescape=select_autoescape(enabled_extensions="yaml", default_for_string=True),
            loader=BaseLoader(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def from_file(self, template_name: str, render_vars: dict) -> str:
        """Render the template from a file

        :type template_name: str
        :param template_name: The name of the template to render
        :type render_vars: dict
        :param render_vars: The variables to render the template with

        :rtype: str
        :returns: The rendered template
        """
        template = self.env_file_render.get_template(name=template_name)
        return template.render(render_vars)

    def from_string(self, template_string: str, render_vars: dict):
        """Render the template from a string

        :type template_string: str
        :param template_string: The string of the template to render
        :type render_vars: dict
        :param render_vars: The variables to render the template with

        :rtype: str
        :returns: The rendered template
        """
        template = self.env_string_render.from_string(source=template_string)
        return template.render(render_vars)
