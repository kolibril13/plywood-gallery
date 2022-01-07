from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, cell_magic)
from IPython import get_ipython
# structure from https://ipython.readthedocs.io/en/stable/config/custommagics.html


@magics_class
class MyMagic(Magics):
    @cell_magic
    def another_new_cellmagic(self, line, cell):
        "my cell magic"
        print("Hello another_new_cellmagic")

    @cell_magic
    def caputre_png_test(self, line, cell):
        print("hello caputre_png_test")
        get_ipython().run_cell_magic(
            'capture',
            ' --no-stderr --no-stdout result',
            cell
        )
        for output in result.outputs:
            data = output.data
            print(data.keys())
