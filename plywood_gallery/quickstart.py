from pathlib import Path


def quickstart(destination_folder=None):

    source_path = Path(__file__).resolve().parent / "quickstart_template"
    src0 = source_path / "gallery_config.yaml"
    src1 = source_path / "html_build.ipynb"
    src2 = source_path / "gallery_notebook.ipynb"
    src3 = source_path / "gallery_assets/gallery_parameters.json"
    src4 = source_path / "gallery_assets/Chapter_1_001_Foo.png"
    src5 = source_path / "gallery_assets/Chapter_2_002_Bar.png"
    src6 = source_path / "gallery_assets/Chapter_2_003_HelloWorld.png"
    src7 = source_path / "icon.png"
    src8 = source_path / "preview_image.png"
    if destination_folder is None:
        dest_path = Path.cwd()
    else:
        dest_path = destination_folder  # TODO: typecheck here!

    dest0 = dest_path / "gallery_config.yaml"
    dest1 = dest_path / "html_build.ipynb"
    dest2 = dest_path / "gallery.ipynb"
    dest3 = dest_path / "gallery_assets/gallery_parameters.json"
    dest4 = dest_path / "gallery_assets/Chapter_1_001_Foo.png"
    dest5 = dest_path / "gallery_assets/Chapter_2_002_Bar.png"
    dest6 = dest_path / "gallery_assets/Chapter_2_003_HelloWorld.png"
    dest7 = dest_path / "icon.png"
    dest8 = dest_path / "preview_image.png"

    for dest in [dest0, dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8]:
        if dest.exists():
            raise ValueError(
                f"The file {dest} already exist. Please delete that file and try again"
            )

    dest_subfolder = dest_path / "gallery_assets"
    dest_subfolder.mkdir(parents=False, exist_ok=True)

    dest0.write_bytes(src0.read_bytes())
    print(f"Successfully created {dest0}")

    dest1.write_bytes(src1.read_bytes())
    print(f"Successfully created {dest1}")

    dest2.write_bytes(src2.read_bytes())
    print(f"Successfully created {dest2}")

    dest3.write_bytes(src3.read_bytes())
    print(f"Successfully created {dest3}")

    dest4.write_bytes(src4.read_bytes())
    print(f"Successfully created {dest4}")

    dest5.write_bytes(src5.read_bytes())
    print(f"Successfully created {dest5}")

    dest6.write_bytes(src6.read_bytes())
    print(f"Successfully created {dest6}")

    dest7.write_bytes(src7.read_bytes())
    print(f"Successfully created {dest7}")

    dest8.write_bytes(src8.read_bytes())
    print(f"Successfully created {dest8}")

    print(
        "Congratulations, the trees were cut down and the plywood gallery project files are now in place. 🌲🪚"
    )
    print(
        "Next step: Setup the `index.html` page with the notebook `html_build.ipynb`"
    )
