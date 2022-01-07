from .plywood_tools import  PlywoodGalleryMagic , ChapterManager

from IPython import get_ipython # register cell magic
ipy = get_ipython()
ipy.register_magics(PlywoodGalleryMagic)