# from IPython.core.magic import (Magics, magics_class, cell_magic)
# from IPython import get_ipython
# from IPython.utils.capture import capture_output

# @magics_class
# class MyMagic(Magics):
#     @cell_magic
#     def caputre_png_test(self, line, cell):
#         print("hello caputre_png_test")
#         with capture_output(stdout=False, stderr=False, display=False) as result:
#             for output in result.outputs:
#                 data = output.data
#                 print(data.keys())

#     @cell_magic
#     def another_new_cellmagic(self, line, cell):
#         "my cell magic"
#         print("Hello another_new_cellmagic")


