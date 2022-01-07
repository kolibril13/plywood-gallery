from .tools import MyMagic

from IPython import get_ipython # register cell magic
ipy = get_ipython()
ipy.register_magics(MyMagic)

