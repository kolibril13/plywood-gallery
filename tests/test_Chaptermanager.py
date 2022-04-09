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
    print(ChapterManager.json_path.name)
    print(ChapterManager.json_path.parents[0].name)
    print(ChapterManager.json_path.parents[1].name)

    assert ChapterManager.json_path.name == "gallery_parameters.json"
    assert ChapterManager.json_path.parents[0].name == "gallery_assets"
    assert ChapterManager.json_path.parents[1].name == "tests"


# ChapterManager.set_assets_folder_name("my_new_example_assets") 