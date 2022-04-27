# Make a release:

1. Update version number in pyproject.toml
2. Tag the main branch with the new version number (e.g. "v0.0.5"). Be careful. Don't make a github release.
The github action defined in `pypi-publish.yml` will automatically make a github release when it finds a new tag in the form 'v*.*.*'.
The `pypi-publish.yml` workflow will then also automatically run poetry and publish the changes at pypi. 