"""

"""

import os
from yaml import safe_load


class PorterMap:

    def __init__(self, path: str) -> None:
        self.path = path

    def _get_map(self):
        os.path.isfile(os.path.join(self.path, "map.yaml"))

    def _get_values(self):
        os.path.isfile(os.path.join(self.path, "values.yaml"))
