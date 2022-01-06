from IPython.core.magic import register_cell_magic
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)


@magic_arguments()
@argument(
    "--option",
    "-o",
    help=("Add an option here"),
)
@argument(
    "--style",
    "-s",
    default="foo",
    help=("Add some style arguments"),
)
@register_cell_magic
def my_cell_magic(line, cell):
    args = parse_argstring(my_cell_magic, line)
    print(f"{args.option=}")
    print(f"{args.style=}")
    print(f"{cell=}")
