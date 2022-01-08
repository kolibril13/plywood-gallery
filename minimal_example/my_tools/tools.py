from IPython.core.magic import (Magics, magics_class, cell_magic)
from IPython.core import magic_arguments

@magics_class
class MyMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "--style",
        "-s",
        help=("Add extra style"),
    )
    @cell_magic
    def flying_circus(self, line, cell):
        "my cell magic"        
        args = magic_arguments.parse_argstring(MyMagic.flying_circus, line)
        print(args.style)
