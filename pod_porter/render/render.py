from jinja2 import Environment, FileSystemLoader, select_autoescape


class Render:
    def __init__(self):
        self.env = self.__set_render_environment()

    @staticmethod
    def __set_render_environment():
        return Environment(
            autoescape=select_autoescape(enabled_extensions="yaml", default_for_string=True),
            loader=FileSystemLoader(searchpath="templates"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
