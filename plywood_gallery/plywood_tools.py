from __future__ import print_function
from IPython.core.magic import (Magics, magics_class,
                                cell_magic)
import json
from pathlib import Path
from IPython.core import magic_arguments
from IPython.core.magic import register_cell_magic


def rmtree(f: Path):
    if f.is_file():
        f.unlink()
    else:
        for child in f.iterdir():
            rmtree(child)
        f.rmdir()


class ChapterManager:
    """recives instructions from  capture_png_test"""
    cell_counter = 0
    chapter_name = ""
    path = Path.cwd() / "gallery_assets/" # cwd of folder where jupyter notebook is in
    json_path = Path.cwd() / "gallery_assets/gallery_parameters.json"
    @staticmethod
    def set_chapter_name(new_chapter):
        """Makes a new chapter"""
        ChapterManager.chapter_name =  new_chapter     

    @staticmethod
    def sort(chapter):
        """Sort chapters in a certain way"""
        raise NotImplementedError

    @staticmethod
    def clean(chapter):
        """clean only one specific chapter"""
        raise NotImplementedError

    @staticmethod
    def clean():
        path  = ChapterManager.path
        """Cleans the whole gallery_assets tree"""
        try:
            rmtree(path)
        except:
            pass
        path.mkdir(parents=False, exist_ok=False)
        # create json file
        joson_file_path = ChapterManager.json_path
        with open(joson_file_path, "w") as jsonFile:
            json.dump({}, jsonFile, indent=2)


@magics_class
class PlywoodGalleryMagic(Magics):
    """Sends instruction to ChapterManager like increment cell counter.
    Here comes the magic, syntax is like here:  https://ipython.readthedocs.io/en/stable/config/custommagics.html
    """
    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=("the path where the image will be saved to"),
    )
    @magic_arguments.argument(
        "--celltype",
        "-c",
        default="Normal",
        help=("Cell can be of type 'Normal', 'Header', and 'Dependend'"),
    )
    @magic_arguments.argument(
        "--style",
        "-s",
        default="",
        help=("Add extra css style for the gallery enteries"),
    )
    def capture_png_test(self, line, cell):
        "my cell magic"
        args = magic_arguments.parse_argstring(PlywoodGalleryMagic.capture_png_test, line)
        print(args.path)
        print(args.celltype)

        ChapterManager.cell_counter +=1
        print("hello Test magic")
        # return line, cell