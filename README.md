# Plywood Gallery

This repo will turn your Jupyter cell output images into a gallery, that enables you to quickly access your code by clicking on the gallery entries. Thereby, one can distinguish three cell types: "Header", "Normal" and "Dependent".   
You can find an minimal example gallery here:   
https://kolibril13.github.io/plywood-gallery-minimal-example/   
*Add Screen recording Here*  
**NOTE: Still work in progress, there might be breaking changes**

# Installation

* Install with  
    ```
    pip install plywood-gallery
    ```

* Open a python console and type:
    ```py
    >>> from plywood_gallery import quickstart, generate_html
    >>> quickstart()
    >>> # now, set project details in gallery_config.yaml e.g. project name, description, etc. 
    >>> generate_html(yaml_file="gallery_config.yaml", html_file="index.html")
    ```
All needed files are now generated.  
* Open `index.html`.  
This can be done with `from plywood_gallery import open_webpage; open_webpage()`  
 or alternatively in VS Code by clicking 'Live Preview: Show Preview'.  
* Add your code to `gallery.ipynb`.   

* Start crafting!
* Note: Everytime you change settings in `gallery_config.yaml` the function `generate_html` has to be called.  
 This can be done with the helper notebook  `build_html.ipynb` that is created by the quickstart.

# Intended workflow

Add the **`%%capture_png`** magic in Jupyter cells and the output images will automatically and in real-time be added to your gallery.   
There will be two phases of building the gallery, the *preparation phase* and the *deployment phase.*

## 1. Preparation phase

During the preparation phase, you can tinker around your cells and debug them and run them again and again.

Every single cell run will create a new entry in the plywood gallery, so running cell A and cell B  in the order AABA will also display the cells in the order AABA and no previous cells will be overwritten.  
This behavior can be used as a visual version control system to see how your plots evolve over the preparation process.  
*There is no "replace plywood gallery entry" yet, but might be implemented in the future, which would render AABA to AB.*

## 2. Publish phase

When you want to publish your gallery notebook e.g. on GitHub pages, then first clean all cells from the preparation phase with the ChapterConfig  
```py
from plywood_tools import ChapterConfig
ChapterConfig.clean_all() # cleans all cells from all chapters
#ChapterConfig.clean("Array 2D")  # cleans all cells from a specified chapter
```

And all previous cells will be deleted.
Next, restart the kernel and click "Run All".

**Why is the kernel restart necessary?**  
In the deployment phase, it is very important that cells are executed from top to button with a freshly started kernel to avoid unwanted artifacts from the preparation phase.

# User guide

**Chapters**  

All gallery entries must be placed in chapters, chapter names are defined as follows:
```py
from plywood_gallery import ChapterConfig
ChapterConfig.set_chapter_name("Array 2D")
```
As soon as a new name is given, this new chapter will be added to the gallery below.
Chapters can be sorted by 
```py
from plywood_gallery import ChapterConfig
ChapterConfig.sort(["2D Array", "3D Arrays"])
```

**Cellmagic**  
One can run the `%%capture_png` with three arguments:
```
--path: (required)
    the path where the image will be saved to
--celltype: (optional)
    Cell can be of type 'Normal', 'Header', and 'Dependent'
--style: (optional)
    Add extra css style for the gallery enteries
```
**--path**:  
A basic cell can look like this:
```py
%%capture_png --path MyExample.png
import matplotlib.pyplot as plt
plt.plot([1,2],[10,20])
```
This will generate the file `gallery_assets/2D_Arrays_001_MyExample.png`. Note that plywood makes sure that file names are unique and can be easily sorted in the file explorer.
Running this cell again would generate `gallery_assets/2D_Arrays_002_MyExample.png`.   
**--style**:  
Change the gallery entry's size, border width or other CSS parameters.  
**--celltype**:    
This is a powerful feature that has to be used carefully.  
Here is its purpose:  

* **Header:**  
Define imports and make definitions of functions

* **Normal:**  
Show usage of imports and functions that you've made in the header cell. WARNING: All normal cells should ALWAYS be independent of each other. Try to not change variables in these cells, and if you have to, make sure to not use them in other normal cells again. If you need to use them again, make sure to rest their value before adding another "Normal cell". This is crucial because a user should always be able to run the cell in the combination "Header+Normal"
* **Dependent**:  
The purpose of this cell is to show slight changes of function calls or post-processing of what happened in a "Normal cell". It should only have few lines of code and only change as few parameters as possible. This makes it possible to see slight visual adjustments in the plots and easily associate the code changes to the visual changes.  
 "Dependent" Cells can be run in the combination "Header+Normal+Dependent", as well as "Header+Normal+Dependent+Dependent".


# Tips and Tricks

* Best you run the notebook in a Jupyter notebook instance and open the website separate (e.g. with a split-screen or second monitor) to keep track of the live updates.

* Multiple notebooks can be used for the same gallery

* When you want one line of your Jupyter cell to be executed, but not to be added to the gallery, simply add the comment `#NOT` at the end of this code line.

# VS Code Extension
With the [Plywood-Gallery-For-VSCode](https://github.com/Rickaym/plywood-gallery-for-vscode/) Extension,  plywood galleries can be displaied in the VS Code side panel.  
 As soon as one gallery entry is clicked, the code is automatically copied to the last current cursor position in a python scripts or Jupyter notebook cell.  
*Add Screen recording Here*


# How it works
Jupyter writes the image to the path and adds information about image_path, style, cell type, and corresponding code into a JSON file.   
This JSON file is read by JavaScript and the elements are placed on an HTML page.

# Notebook formatting
Formatting with black can be done this way:
`black --python-cell-magics capture_png  docs/gallery.ipynb`

# Updating
Get the latest version of the plywood gallery with   
`pip install plywood_gallery --update`
# Attribution

Thanks to @christopher-besch for discussing the project architecture with me.  
Thanks to @krassowski for the help to caputre the png output images.  
Thanks to @Rickaym for some inspirations about the JSON files and VS Code related things.  
Thanks to @behackl for providing the Github Actions auto-release script.