from plywood_gallery import ChapterManager


def test_chaptermanager_counter():
    """Test the Methods of ChapterManager"""
    # check that ChapterManager.cell_counter is working
    ChapterManager.cell_counter = 12
    assert ChapterManager.cell_counter == 12

    ChapterManager.reset_counter()
    assert ChapterManager.cell_counter == 0


def test_chaptermanager_json_path():

    """Testing location of the json_file"""
    assert ChapterManager.json_path.name == "gallery_parameters.json"
    assert ChapterManager.json_path.parents[0].name == "gallery_assets"

    """Create file and test existence"""
    ChapterManager.set_assets_folder_name("my_new_example_assets")

    assert ChapterManager.json_path.name == "gallery_parameters.json"
    assert ChapterManager.json_path.parents[0].name == "my_new_example_assets"

    assert ChapterManager.json_path.exists() is True

    ChapterManager.clean_all(skip_warning=True)

    assert ChapterManager.json_path.exists() is False

