from __future__ import print_function
from IPython.core.magic import (Magics, magics_class,
                                cell_magic)
import json
from IPython.core.magic import register_cell_magic
from pathlib import Path


def rmtree(f: Path):
    if f.is_file():
        f.unlink()
    else:
        for child in f.iterdir():
            rmtree(child)
        f.rmdir()


class ChapterManager:
    def clean_all(path):
        """Cleans the whole gallery_assets tree"""
        try:
            rmtree(path)
        except:
            pass

        path.mkdir(parents=False, exist_ok=False)
        # create json file
        joson_file_path = "gallery_assets/gallery_parameters.json"
        with open(joson_file_path, "w") as jsonFile:
            json.dump({}, jsonFile, indent=2)

    def init_chapter(chapter):
        """Initilizes the first chapter"""
        raise NotImplementedError

    def clean(path, chapter):
        """clean only one specific chapter"""
        raise NotImplementedError

    def sort(path, chapter):
        """Sort chapters in a certain way"""
        raise NotImplementedError


@magics_class
class CapturePngTEST(Magics):
    """Here comes the magic, syntax is like here:  https://ipython.readthedocs.io/en/stable/config/custommagics.html
    """
    @cell_magic
    def capture_png_test(self, line, cell):
        "my cell magic"
        print("hello Test magic")
        #return line, cell
