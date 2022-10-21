from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import pkg_resources
from yaml import load, SafeLoader


def load_jinja2_template():
    templates_dir = Path(__file__).resolve().parent / "jinja2_template"
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("template_index.html")
    return template


def generate_html_from_jinja2_and_yaml(yaml_file=None, index_html_file=None, batch_processing=False):

    if batch_processing is True:
        print("WARNING: This feature is work in progress")
        with open(yaml_file, "r") as file:
            html__batch_configuration_parameter = load(file, SafeLoader)
            print(f"Successfully read batch file {yaml_file}")
            all_yaml_files = html__batch_configuration_parameter["gallery_configs"]
            print(all_yaml_files)
            for yaml_entry in all_yaml_files:
                generate_html_from_jinja2_and_yaml(yaml_file=yaml_entry, index_html_file=f"web_{yaml_entry[:-5]}.html", batch_processing=False)
            return 0

    template = load_jinja2_template()

    if yaml_file is None:
        yaml_file = Path.cwd() / "gallery_config.yaml"

    if index_html_file is None:
        index_html_file = Path.cwd() / "index.html"

    with open(yaml_file, "r") as file:
        html_configuration_parameter = load(file, SafeLoader)
        print(f"Successfully read {yaml_file}")

    project_name = html_configuration_parameter["project_name"]
    repository_url = html_configuration_parameter["repository_url"]
    user_content_version = html_configuration_parameter["user_content_version"]
    core_version = pkg_resources.get_distribution("plywood_gallery").version
    description = html_configuration_parameter["description"]
    favicon = html_configuration_parameter["favicon"]
    preview_image = html_configuration_parameter["preview_image"]
    gallery_parameters_path = html_configuration_parameter["gallery_parameters_path"]

    with open(index_html_file, "w") as fh:
        fh.write(
            template.render(
                project_name=project_name,
                repository_url=repository_url,
                user_content_version=user_content_version,
                core_version=core_version,
                description=description,
                favicon=favicon,
                preview_image=preview_image,
                gallery_parameters_path=gallery_parameters_path,
            )
        )
        print(f"Successfully created {index_html_file}")
        print(
            "Now you can start crafting your examples with the file gallery.ipynb and see the results in `index.html`!🚪 "
        )
        print(
            "Just opening index.html in the browser won't load the interactive parts, so better use `from plywood_gallery import open_webpage; open_webpage()` or in VS Code select 'Live Preview: Show Preview' in VSCode to start the page with a server"
        )
