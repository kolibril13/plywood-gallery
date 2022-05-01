from plywood_gallery import quickstart

from pathlib import Path


def test_ChapterConfig_counter():
    """Test the Template and cell magic"""

    temp_quickstart_data_dir = Path(__file__).parent.absolute() / "temp_quickstart_data"

    temp_quickstart_data_dir.mkdir(exist_ok=True)
    quickstart(temp_quickstart_data_dir)

    # remove files
    Path(temp_quickstart_data_dir / "gallery_config.yaml").unlink()
    Path(temp_quickstart_data_dir / "html_build.ipynb").unlink()
    Path(temp_quickstart_data_dir / "gallery.ipynb").unlink()
    Path(temp_quickstart_data_dir / "gallery_assets/gallery_parameters.json").unlink()
    Path(temp_quickstart_data_dir / "gallery_assets/X1_001_Foo.png").unlink()
    Path(temp_quickstart_data_dir / "gallery_assets/X2_002_Bar.png").unlink()
    Path(temp_quickstart_data_dir / "gallery_assets/X2_003_HelloWorld.png").unlink()

    # remove dirs
    Path(temp_quickstart_data_dir / "gallery_assets").rmdir()
    Path(temp_quickstart_data_dir).rmdir()
