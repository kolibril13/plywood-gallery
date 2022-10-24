import json
from base64 import b64decode
from io import BytesIO, StringIO
from pathlib import Path

import PIL
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output


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
        help=("Cell can be of type 'Normal', 'Header', and 'Dependent'"),
    )
    @magic_arguments.argument(
        "--style",
        "-s",
        default="",
        help=("Add extra css style for the gallery enteries"),
    )
    @cell_magic
    def capture_png(self, line, cell):
        """Saves the png image and the css style for the html page"""
        args = magic_arguments.parse_argstring(PlywoodGalleryMagic.capture_png, line)

        postpath = args.path
        chapter_name = ChapterConfig.chapter_name
        chapter_name_underscore = chapter_name.replace(" ", "_")
        joson_file_path = ChapterConfig.json_path
        prepath = ChapterConfig.path.name  # get the last child folder name
        ChapterConfig.cell_counter += 1
        # include chaptername
        path = f"{prepath}/{chapter_name_underscore}_{ChapterConfig.cell_counter:03}_{postpath}"

        # path = path.split(".png")[0] + str(time.time_ns()) + ".png"
        if not path:
            raise ValueError("No path found!")

        style = args.style
        style = style.strip('"')  # remove quotes

        styles = {
            "Normal": "border: 3px solid #007AB8;",
            "Header": "border: 3px solid #ED6A5A;",
            "Dependend": "border: 3px solid #A8DCF0;",
        }
        try:
            default_style = styles[args.celltype]
        except KeyError:
            raise ValueError("Not a valid cell type!")

        style = default_style + style

        raw_code_block = cell
        code_block = ""

        for codeline in StringIO(raw_code_block):
            if "#NOT" in codeline:
                pass
            if "# NOT" in codeline:
                pass
            else:
                code_block += codeline

        new_codeblock = ""
        for codeline in StringIO(code_block):
            if "#ONLY" in codeline:
                codeline = codeline.replace("#ONLY", "")
                new_codeblock += codeline
            if "# ONLY" in codeline:  # TODO Write Test for this
                codeline = codeline.replace("# ONLY", "")
                new_codeblock += codeline
            else:
                pass

        if new_codeblock:  # checks if there are lines that include "#ONLY" OR "# ONLY"
            code_block = new_codeblock

        # make sure that javascript can read the single quote character
        code_block = code_block.replace("'", "&#39;")
        code_block = code_block.strip("\n")

        # read + update + write json
        with open(joson_file_path, "r") as jsonFile:
            all_content = json.load(jsonFile)

        data = all_content["plywood_content"]
        if chapter_name not in data:
            data[chapter_name] = []

        chapter_content = data[chapter_name]
        chapter_content.append(
            {
                "image_path": path,
                "celltype": args.celltype,
                "css": style,
                "code": code_block,
            }
        )

        data[chapter_name] = chapter_content

        all_content["plywood_content"] = data
        with open(joson_file_path, "w") as jsonFile:
            json.dump(all_content, jsonFile, indent=2, sort_keys=False)

        # save the output
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)  # idea by @krassowski

        # save image
        for output in result.outputs:
            display(output)
            data = output.data
            if "image/png" in data:
                png_bytes = data["image/png"]
                if isinstance(png_bytes, str):
                    png_bytes = b64decode(png_bytes)
                assert isinstance(png_bytes, bytes)
                bytes_io = BytesIO(png_bytes)
                image = PIL.Image.open(bytes_io)
                image.save(path, "png")


class ChapterConfig:
    """Recives instructions from  capture_png_test"""

    cell_counter = 0
    chapter_name = ""
    path = Path.cwd() / "gallery_assets/"  # cwd of folder where jupyter notebook is in
    json_path = Path.cwd() / path / "gallery_parameters.json"

    @staticmethod
    def set_chapter_name(new_chapter):
        """Makes a new chapter"""
        ChapterConfig.chapter_name = new_chapter

    def set_assets_folder_name(new_assets_folder_name):  # TODO Some more exploration of this feature is required.
        """Name for the folder where the images and the json file are saved in."""
        path = (
            Path.cwd() / new_assets_folder_name
        )  # cwd of folder where jupyter notebook is in
        ChapterConfig.path = path
        ChapterConfig.json_path = Path.cwd() / path / "gallery_parameters.json"

    # ChapterConfig.generate_json() # remove this? -> yes

    @staticmethod
    def reset_counter():
        """Sets the counter back to 0"""
        ChapterConfig.cell_counter = 0

    @staticmethod
    def sort(chapter_order):
        """Sort chapters according to the list that is given.
        TODO: Make exception when name did not occur."""

        # sort chapter
        import json

        new_order = chapter_order
        joson_file_path = ChapterConfig.json_path
        with open(joson_file_path, "r") as jsonFile:
            all_content = json.load(jsonFile)

        data = all_content["plywood_content"]

        temp_data = []

        for chapter_name in new_order:
            temp_data.append(data[chapter_name])
            data.pop(chapter_name)

        new_data = {}
        for chapter_name, temp in zip(new_order, temp_data):
            new_data[chapter_name] = temp

        new_data.update(data)
        
        all_content["plywood_content"] = new_data
        with open(joson_file_path, "w") as jsonFile:
            json.dump(all_content, jsonFile, indent=2, sort_keys=False)

    @staticmethod
    def clean(chapter_name):
        """clean only one specific chapter"""
        with open(ChapterConfig.json_path, "r") as jsonFile:
            all_content = json.load(jsonFile)

        data = all_content["plywood_content"]

        if chapter_name in data:
            chapter_content = data[chapter_name]
        else:
            raise KeyError(
                f"Cleaning the chapter '{chapter_name}' is not possible because it is not defined in the json file. Probably it got deleted already before."
            )

        for entry in chapter_content:
            image = entry["image_path"]
            whole_path = ChapterConfig.path.parent / image
            try:
                whole_path.unlink()
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"""It was not possible to delete '{whole_path.parts[-1]}' because this file occurs in the json file,
                        however not on the disk. Probably images in the folder '/{ChapterConfig.json_path.parts[-2]}'
                        got renamed without renaming the corresponding json entry. In this case, it's recomended
                        to run the clean_all command once and re-execute the plywood gallery from scratch."""
                )
            print(
                f"Deleted '{whole_path.parts[-1]}' from the folder '/{ChapterConfig.json_path.parts[-2]}' "
            )

        data.pop(chapter_name)

        jp = ChapterConfig.json_path
        print(f"Removed entry '{chapter_name}' from '{jp.relative_to(jp.parents[1])}'")

        all_content["plywood_content"] = data
        with open(ChapterConfig.json_path, "w") as jsonFile:
            json.dump(all_content, jsonFile, indent=2, sort_keys=False)

    @staticmethod
    def __rmtree(f: Path):
        """Private method that deletes a folder and all its files and subfolders, used in clean_all"""
        if f.is_file():
            f.unlink()
        else:
            for child in f.iterdir():
                ChapterConfig.__rmtree(child)
            f.rmdir()

    @staticmethod
    def clean_all(skip_warning=False):
        """Cleans the whole gallery_assets tree. User will be asked to confirm the cleaning first
        After cleaning, a new json file will be created."""

        path = ChapterConfig.path

        print(f"This path and all its child elements will be removed:{path}")

        if not skip_warning:
            if input("are you sure? (y/n)") != "y":
                raise ValueError("Could not delete folder because no permission")
            else:
                pass

        try:
            ChapterConfig.__rmtree(path)
            print(f"Deleted '{path}' and all containing files and folder.")
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The path {path} does not exist and therefore could not be deleted."
            )

    @staticmethod
    def generate_json():
        """Creates a new empty json file for gallery information."""
        path = ChapterConfig.path
        path.mkdir(parents=False, exist_ok=True)
        # create json file
        joson_file_path = ChapterConfig.json_path

        import pkg_resources
        core_version = pkg_resources.get_distribution("plywood_gallery").version

        json_default = {
            "plywood_metadata": {"plywood_gallery_core_version": f"{core_version}"},
            "plywood_content": {},
        }

        with open(joson_file_path, "w") as jsonFile:
            json.dump(json_default, jsonFile, indent=2)

        print(f"Successfully created {ChapterConfig.json_path}!🦫")
