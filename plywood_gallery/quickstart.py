from pathlib import Path


def quickstart(destination_folder=False):

    source_path = Path(__file__).resolve().parent / "template"
    src0 = source_path / "template_setup_notebook.ipynb"
    src1 = source_path / "template_gallery_notebook.ipynb"
    src2 = source_path / "gallery_assets/gallery_parameters.json"
    src3 = source_path / "gallery_assets/X1_001_Foo.png"
    src4 = source_path / "gallery_assets/X2_002_Bar.png"
    src5 = source_path / "gallery_assets/X2_003_HelloWorld.png"

    if destination_folder == False:
        dest_path = Path.cwd()
    else:
        dest_path = destination_folder  # TODO: typecheck here!
    dest0 = dest_path / "setup_notebook.ipynb"
    dest1 = dest_path / "gallery.ipynb"
    dest2 = dest_path / "gallery_assets/gallery_parameters.json"
    dest3 = dest_path / "gallery_assets/X1_001_Foo.png"
    dest4 = dest_path / "gallery_assets/X2_002_Bar.png"
    dest5 = dest_path / "gallery_assets/X2_003_HelloWorld.png"

    for dest in [dest0, dest1, dest2, dest3, dest4, dest5]:
        if dest.exists():
            raise ValueError(
                f"The file {dest} already exist. Please delete that file and try again"
            )

    dest_subfolder = dest_path / "gallery_assets"
    dest_subfolder.mkdir(parents=False, exist_ok=True)

    dest0.write_bytes(src0.read_bytes())
    print(f"Sucessfuly created {dest0}")

    dest1.write_bytes(src1.read_bytes())
    print(f"Sucessfuly created {dest1}")

    dest2.write_bytes(src2.read_bytes())
    print(f"Sucessfuly created {dest2}")

    dest3.write_bytes(src3.read_bytes())
    print(f"Sucessfuly created {dest3}")

    dest4.write_bytes(src4.read_bytes())
    print(f"Sucessfuly created {dest4}")

    dest5.write_bytes(src5.read_bytes())
    print(f"Sucessfuly created {dest5}")
    print("Next step: Setup the html page with setup_notebook.ipynb")