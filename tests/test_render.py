import pytest
from pod_porter.render.render import Render


def test_render_from_string():
    obj = Render()
    response = obj.from_string(template_string="Hello, {{ name }}!", render_vars={"name": "World"})

    assert response == "Hello, World!"


def test_render_from_fileg(templates_path):
    obj = Render(templates_dir=templates_path)
    response = obj.from_file(template_name="test-template.j2", render_vars={"data": "Hello, World!"})

    assert response == "Hello, World!"
