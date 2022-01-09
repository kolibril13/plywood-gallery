from pathlib import Path


def quickstart():

    src = Path(__file__).resolve().parent / "template" / "template_index.html"
    dest = Path.cwd() / "new_index.html"
    print(src,dest)
    #dest.write_bytes(src.read_bytes()) #for binary files # better this?
    dest.write_text(src.read_text()) #for text files

    src = Path(__file__).resolve().parent / "template" / "template_gallery.ipynb"
    dest = Path.cwd() / "new_gallery.ipynb"
    print(src,dest)
    dest.write_text(src.read_text()) #for text files
