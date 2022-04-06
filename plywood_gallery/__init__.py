from .plywood_tools import PlywoodGalleryMagic, ChapterManager
from .quickstart import quickstart
from .generate_html import generate_html_from_jinja2_and_yaml
from IPython import get_ipython  # register cell magic
import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

print(f"Plywood Gallery v{__version__}")

try:
    ipy = get_ipython()
    ipy.register_magics(PlywoodGalleryMagic)
except:
    pass
