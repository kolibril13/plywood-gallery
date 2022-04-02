from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def load_jinja2_template():
    templates_dir = Path(__file__).resolve().parent / "template"
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("template_index.html")
    return template
