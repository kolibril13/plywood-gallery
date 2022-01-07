import json
import os
import shutil
import time
from base64 import b64decode
from io import BytesIO
from IPython import get_ipython
from IPython.core.magic import register_cell_magic

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import seaborn as sns


def rmtree(f: Path):
    if f.is_file():
        f.unlink()
    else:
        for child in f.iterdir():
            rmtree(child)
        f.rmdir()

def clean_all(path):
    # delete all previous files
    try:
        rmtree(path)
    except:
        pass

    path.mkdir(parents=False, exist_ok=False)
    # create json file
    joson_file_path = "gallery_assets/gallery_parameters.json"
    with open(joson_file_path, "w") as jsonFile:
        json.dump({}, jsonFile, indent=2)