from pathlib import Path


def quickstart():
    
        
    source_path = Path(__file__).resolve().parent / "template" 
    src1 =  source_path / "template_index.html"
    src2 =  source_path / "new_gallery.ipynb"
    src3 =  source_path / "gallery_assets/gallery_parameters.json"
    src4 =  source_path / "gallery_assets/Template_Chapter_001_Template.png"


    dest_path = Path.cwd()  
    dest1 = dest_path / "new_index.html"
    dest2 = dest_path / "new_gallery.ipynb"
    dest3 = dest_path / "gallery_assets/gallery_parameters.json"
    dest4 = dest_path / "gallery_assets/Template_Chapter_001_Template.png"

    for dest in [dest1, dest2, dest3, dest4]:
        if dest.exists():
            raise ValueError(f"The file {dest} already exist. Please delete that file and try again")

    dest_subfolder = dest_path / "gallery_assets" 
    dest_subfolder.mkdir(parents=False, exist_ok=True)


    dest1.write_bytes(src1.read_bytes()) 
    dest2.write_bytes(src2.read_bytes()) 
    dest3.write_bytes(src3.read_bytes())
    dest4.write_bytes(src4.read_bytes()) 

    print(f"Sucessfuly created \n{dest1}\n{dest2}\n{dest3}\n{dest4} ")