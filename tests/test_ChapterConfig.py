from plywood_gallery import ChapterConfig


def test_ChapterConfig_counter():
    """Test the Methods of ChapterConfig"""
    # check that ChapterConfig.cell_counter is working
    ChapterConfig.cell_counter = 12
    assert ChapterConfig.cell_counter == 12

    ChapterConfig.reset_counter()
    assert ChapterConfig.cell_counter == 0


def test_ChapterConfig_json_path():

    """Testing location of the json_file"""
    assert ChapterConfig.json_path.name == "gallery_parameters_path.json"
    assert ChapterConfig.json_path.parents[0].name == "gallery_assets"

    # """Create file and test existence"""
    ChapterConfig.set_assets_folder_name("my_new_example_assets")

    assert ChapterConfig.json_path.name == "gallery_parameters_path.json"
    assert ChapterConfig.json_path.parents[0].name == "my_new_example_assets"

    ChapterConfig.generate_json()
    assert ChapterConfig.json_path.exists() is True

    ChapterConfig.clean_all(skip_warning=True)

    assert ChapterConfig.json_path.exists() is False
