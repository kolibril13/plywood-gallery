import json
from base64 import b64decode
from io import BytesIO, StringIO
from pathlib import Path

import PIL
from IPython.core import magic_arguments
from IPython.core.magic import (
    Magics,
    cell_magic,
    magics_class
)
from IPython.utils.capture import capture_output
from IPython.display import display


def rmtree(f: Path):
    if f.is_file():
        f.unlink()
    else:
        for child in f.iterdir():
            rmtree(child)
        f.rmdir()


class ChapterManager:
    """Recives instructions from  capture_png_test"""
    cell_counter = 0
    chapter_name = ""
    path = Path.cwd() / "gallery_assets/" # cwd of folder where jupyter notebook is in
    json_path = Path.cwd() / "gallery_assets/gallery_parameters.json"
    @staticmethod
    def set_chapter_name(new_chapter):
        """Makes a new chapter"""
        ChapterManager.chapter_name =  new_chapter    

    @staticmethod
    def reset_counter():
        """Sets the counter back to 0"""
        ChapterManager.cell_counter = 0

    @staticmethod
    def sort(chapter):
        """Sort chapters in a certain way"""
        raise NotImplementedError

    @staticmethod
    def clean(chapter):
        """clean only one specific chapter"""
        raise NotImplementedError

    @staticmethod
    def clean_all(skip_warning= False):
        """Cleans the whole gallery_assets tree. User will be asked to confirm the cleaning first"""
        print(f"This path and all its child elements will be removed:{ChapterManager.path}")
        if input("are you sure? (y/n)") != "y":
            raise ValueError("Could not delete folder because no permission")
        else:
            path  = ChapterManager.path
        try:
            rmtree(path)
        except:
            raise ValueError("Something went wrong")

        path.mkdir(parents=False, exist_ok=False)
        # create json file
        joson_file_path = ChapterManager.json_path
        with open(joson_file_path, "w") as jsonFile:
            json.dump({}, jsonFile, indent=2)


@magics_class
class PlywoodGalleryMagic(Magics):
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
    @cell_magic
    def capture_png(self,line, cell):
        """Saves the png image and the css style for the html page"""
        args = magic_arguments.parse_argstring(PlywoodGalleryMagic.capture_png, line)

        postpath = args.path
        chapter_name= ChapterManager.chapter_name
        chapter_name_underscore = chapter_name.replace(" ", "_")
        joson_file_path = ChapterManager.json_path
        prepath = ChapterManager.path.name # get the last child folder name
        ChapterManager.cell_counter += 1
        # include chaptername
        path = f"{prepath}/{chapter_name_underscore}_{ChapterManager.cell_counter:03}_{postpath}"

        #path = path.split(".png")[0] + str(time.time_ns()) + ".png"
        if not path:
            raise ValueError('No path found!')

        style = args.style
        style = style.strip('"')  # remove quotes

        styles = {
            'Normal': 'border: 3px solid #007AB8;',
            'Header': 'border: 3px solid #ED6A5A;',
            'Dependend': 'border: 3px solid #A8DCF0;'
        }
        try:
            default_style = styles[args.celltype]
        except KeyError:
            raise ValueError('Not a valid cell type!')

        style = default_style + style

        raw_code_block = cell
        code_block = ""

        for codeline in StringIO(raw_code_block):
            if "#NOT" in codeline:
                pass
            else:
                code_block += codeline

        new_codeblock = ""
        for codeline in StringIO(code_block):
            if "#ONLY" in codeline:
                codeline = codeline.replace("#ONLY", "")
                new_codeblock += codeline
            else:
                pass

        if new_codeblock:  # checks if there are lines that include "#ONLY"
            code_block = new_codeblock

        # make sure that javascript can read the single quote character
        code_block = code_block.replace("'", "&#39;")
        code_block = code_block.strip("\n")

        # read + update + write json
        with open(joson_file_path, "r") as jsonFile:
            data = json.load(jsonFile)

        if not chapter_name in data:
            data[chapter_name] = []

        chapter_content = data[chapter_name]
        chapter_content.append(
            [{"image_path": path,
            "celltype": args.celltype,
            "css": style,
            "code": code_block}])

        data[chapter_name] = chapter_content
        with open(joson_file_path, "w") as jsonFile:
            json.dump(data, jsonFile, indent=2, sort_keys=False)


        # save the output
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell) # idea by @krassowski 

        # save image
        for output in result.outputs:
            display(output)
            data = output.data
            if 'image/png' in data:
                png_bytes = data['image/png']
                if isinstance(png_bytes, str):
                    png_bytes = b64decode(png_bytes)
                assert isinstance(png_bytes, bytes)
                bytes_io = BytesIO(png_bytes)
                image = PIL.Image.open(bytes_io)
                image.save(path, 'png')