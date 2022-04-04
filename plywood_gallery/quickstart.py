from pathlib import Path


def quickstart(destination_folder=False):

    source_path = Path(__file__).resolve().parent / "quickstart_template"
    src0 = source_path / "template_html_configuration.yaml"
    src1 = source_path / "template_html_build.ipynb"
    src2 = source_path / "template_gallery_notebook.ipynb"
    src3 = source_path / "gallery_assets/gallery_parameters.json"
    src4 = source_path / "gallery_assets/X1_001_Foo.png"
    src5 = source_path / "gallery_assets/X2_002_Bar.png"
    src6 = source_path / "gallery_assets/X2_003_HelloWorld.png"

    if not destination_folder:
        dest_path = Path.cwd()
    else:
        dest_path = destination_folder  # TODO: typecheck here!

    dest0 = dest_path / "html_configuration.yaml"
    dest1 = dest_path / "html_build.ipynb"
    dest2 = dest_path / "gallery.ipynb"
    dest3 = dest_path / "gallery_assets/gallery_parameters.json"
    dest4 = dest_path / "gallery_assets/X1_001_Foo.png"
    dest5 = dest_path / "gallery_assets/X2_002_Bar.png"
    dest6 = dest_path / "gallery_assets/X2_003_HelloWorld.png"

    for dest in [dest0, dest1, dest2, dest3, dest4, dest5, dest6]:
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

    dest6.write_bytes(src6.read_bytes())
    print(f"Sucessfuly created {dest6}")

    print(
        "Congratiulations, the trees were cut down and the plywood gallery project files are now in place. 🌲🪚"
    )
    print(
        "Next step: Setup the `index.html` page with the notebook `html_build.ipynb`"
    )
