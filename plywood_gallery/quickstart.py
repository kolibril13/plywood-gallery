from pathlib import Path


def quickstart():

    src = Path(__file__).resolve() / "template" / "template_index.html"
    dest = Path.cwd()

   # dest.write_bytes(src.read_bytes()) #for binary files
    dest.write_text(src.read_text()) #for text files
