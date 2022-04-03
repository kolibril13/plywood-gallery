from .plywood_tools import PlywoodGalleryMagic, ChapterManager
from .quickstart import quickstart
from .generate_html import generate_html_from_jinja2_and_yaml
from IPython import get_ipython  # register cell magic

try:
    ipy = get_ipython()
    ipy.register_magics(PlywoodGalleryMagic)
except:
    pass
