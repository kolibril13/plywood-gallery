# Changelog

## 0.0.9

* add `plywood_metadata` identifier in json, and adjust sort, clean and quickstart accordingly.

## 0.0.8

* Tweak template
* Rename parameter `index_html_file` to `html_file`
* Rename `generate_html_from_jinja2_and_yaml` to `generate_html`
* Add icon and preview_image to template.
* Remove upper limits from dependencies.
## 0.0.7
* add `preview_image` in `gallery_config.yaml`
* Remove `custom_footer` in `gallery_config.yaml`
* Add OpenGraph tags
* Update the HTML template -> much improved CSS
* shift minimal example to separate repo
* add parameter `batch_processing` to `generate_html`. This will likely be removed again.
## 0.0.6

* Rename `html_configuration.yaml` to `gallery_config.yaml`

## 0.0.5
* setup autorelease
* internal restructuring
## 0.0.4
* Json file is not created automatically anymore, call `ChapterManager.generate_json()` instead.
* Implemented Testing structure
* Refactor of `open_webpage` function
* Rename ChapterManager -> ChapterConfig
* Fix typo in gallery_parameters_path.