import os.path

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Render:

    BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_DIRECTORY = os.path.join(BASE_DIRECTORY, "templates")


    def __init__(self):
        self.env = self.__set_render_environment()

    def __set_render_environment(self):
        return Environment(
            autoescape=select_autoescape(enabled_extensions="yaml", default_for_string=True),
            loader=FileSystemLoader(searchpath=self.TEMPLATE_DIRECTORY),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def get_template(self, template_name):
        return self.env.get_template(template_name)

    def get_rendered_template(self, template_name, **kwargs):
        template = self.get_template(template_name)
        return template.render(**kwargs)
