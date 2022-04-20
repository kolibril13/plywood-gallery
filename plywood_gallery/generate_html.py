from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import pkg_resources


def load_jinja2_template():
    templates_dir = Path(__file__).resolve().parent / "jinja2_template"
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("template_index.html")
    return template


def generate_html_from_jinja2_and_yaml(yaml_file=None, index_html_file=None):
    template = load_jinja2_template()

    if yaml_file is None:
        yaml_file = Path.cwd() / "html_configuration.yaml"

    if index_html_file is None:
        index_html_file = Path.cwd() / "index.html"

    from yaml import load, SafeLoader

    with open(yaml_file, "r") as file:
        html_configuration_parameter = load(file, SafeLoader)
        print(f"Sucessfuly read {yaml_file}")

    project_name = html_configuration_parameter["project_name"]
    repository_url = html_configuration_parameter["repository_url"]
    user_content_version = html_configuration_parameter["user_content_version"]

    # TODO this works, but does not seem to be the best solution
    core_version = pkg_resources.get_distribution("plywood_gallery").version

    description = html_configuration_parameter["description"]
    favicon = html_configuration_parameter["favicon"]
    custom_footer = html_configuration_parameter["custom_footer"]
    gallary_parameters_path = html_configuration_parameter["gallary_parameters_path"]

    with open(index_html_file, "w") as fh:
        fh.write(
            template.render(
                project_name=project_name,
                repository_url=repository_url,
                user_content_version=user_content_version,
                core_version=core_version,
                description=description,
                favicon=favicon,
                custom_footer=custom_footer,
                gallary_parameters_path=gallary_parameters_path,
            )
        )
        print(f"Sucessfuly created {index_html_file}")
        print(
            "Now you can start crafting your examples with the file gallery.ipynb and see the results in `index.html`!🚪 "
        )
        print(
            "Just opening index.html in the browser won't load the interactive parts, so better use `from plywood_gallery import open_webpage; open_webpage()` or in VS Code select 'Live Preview: Show Preview' in VSCode to start the page with a server"
        )
