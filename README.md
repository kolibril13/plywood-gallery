# Plywood Gallery 🌲🪚 -- 🪵🪓 --🚪

This repo will turn your Jupyter cell output images into a gallery, that enables you to quickly access your code by clicking on the gallery entries. Thereby, one can distinguish three cell types: "Header", "Normal" and "Dependent". 
You can find an example gallery here: https://kolibril13.github.io/plywood-gallery/   
*Add Screen recording Here*  
**NOTE: Still work in progress, there might be breaking changes**

# Installation

* Install with  
    ```
    pip install plywood-gallery
    ```

* Open a python script or python console and type:
    ```py
    from plywood_gallery import quickstart
    quickstart()
    ```
    This will init the project structure files.  
* Set up your project details in `html_configuration.yaml` e.g. project name, description, etc.  
* Run the function `generate_html_from_jinja2_and_yaml` in the notebook  `html_build.ipynb`.  
All needed files are now generated.  
* Open `index.html`.  Just loading index.html in the browser won't load the interactive parts, so better use `from plywood_gallery import ChapterManager; ChapterManager.open_webpage()` or in VS Code select 'Live Preview: Show Preview' in VS Code to start the page with a server.  
* Add your code to `gallery.ipynb`.   

* Start crafting! ✔️

# Intended workflow

Add the **`%%capture_png`** magic in Jupyter cells and the output images will automatically and in real-time be added to your gallery.   
There will be two phases of building the gallery, the *preparation phase* and the *deployment phase.*

## 1. Preparation phase

During the preparation phase, you can tinker around your cells and debug them and run them again and again.

Every single cell run will create a new entry in the plywood gallery, so running cell A and cell B  in the order AABABB will also display the cells in the order AABABB and no previous cells will be overwritten. 
This behavior can also be used to have a visual version control system of your notebook execution history. 
This is nothing else than a visual notebook execution history, and therefore can be used as a version control system about how your plots and graphics evolve over the preparation process.  
There is no "replace plywood gallery entry" yet, but might be implemented in the future, which would render AABABB to AB.

## 2. Deployment phase

When you want to publish your gallery notebook e.g. on GitHub pages, then first clean all cells from the preparation phase with the chaptermanager  
```py
from plywood_tools import ChapterManager
ChapterManager.clean_all() # cleans all cells from all chapters
#ChapterManager.clean("Array 2D")  # cleans all cells from a specified chapter
```

And all previous cells will be deleted.
Next, restart the kernel and click "Run All".

**Why is the kernel restart necessary?**  
In the deployment phase, it is very important that cells are executed from top to button with a freshly started kernel to avoid unwanted artifacts from the preparation phase.

# User guide

**Chapters**  

All gallery entries need to be in chapters, chapter names are defined like this:
```py
from plywood_gallery import ChapterManager
ChapterManager.set_chapter_name("Array 2D")
```
As soon as there is a new name assigned, this new chapter will be added in the gallery below.
Chapters can be sorted by 
```py
from plywood_gallery import chaptermanager
chaptermanager.sort(["2D Array", "3D Arrays"]) # Not yet Implemented
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
Change the gallery entries size, border width or whatever is possible in CSS!  
**--celltype**:    
This is a very powerful feature that has to be used carefully.  
Here is their purpose:  

* **Header:**  
Define imports and make definitions of functions

* **Normal:**  
Show usage of imports and functions that you've made in the header cell. WARNING: All normal cells should ALWAYS be independent of each other. Try to not change variables in these cells, and if you have to, make sure to not use them in other normal cells again. If you need to use them again, make sure to rest their value before adding another "Normal cell". This is crucial because a user should always be able to run the cell in the combination "Header+Normal"
* **Dependent**:  
The purpose of this cell is to show slight changes of function calls or post-processing of what happened in a "Normal cell". It should only have very few lines of code and only change as few parameters as possible. That makes it possible, to see the slight visual adjustments in plots, and then easily associate the code changes with the visual changes. "Dependent" Cells can be run in the combination "Header+Normal+Dependent", but also "Header+Normal+Dependent+Dependent".



**Side Note: Why is this useful?**   
Current sphinx documentation of SciPy, Matplotlib, scikit-image, etc. have really nice examples, but they might be complex and convoluted (E.g. [this Matplotlib example](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html#sphx-glr-gallery-shapes-and-collections-artist-reference-py)   with 91 lines of code).
This new gallery approach has the potential to declutter graphical examples drastically, by splitting them into small chunks that are easy to grasp. The user will only see the lines s/he needs and does not have to bother about the rest. And in case that the user wants to go more in-depth, there is still the Header cell.
Of course, writing a plywood-style gallery adds an extra layer of complexity, but the benefit can be tremendous: Users don't have to fight their way to a code jungle anymore, but they get nicely served what they were looking for.
Furthermore, one does not have to make a sphinx build to see how the example looks in the gallery, it gets added in real-time.


# Tips and Tricks

* Best you run the notebook in a Jupyter notebook instance and open the website separate (e.g. with a split-screen or second monitor) to keep track of the live updates.

* Multiple notebooks can be used for the same gallery

* When you want one line of your Jupyter cell to be executed, but not to be added to the gallery, simply add the comment `#NOT` at the end of this code line.

# VS Code Plugin
Coming soon:
Display your plywood galleries in the VS Code side panel with the VS Code extension. As soon as one gallery entry is clicked, the code is automatically copied to the last current cursor position in a VS Code opened python script or VS Code Jupyter notebook cell.
*Add Screen recording Here*


# How it works
Jupyter writes the image to the path and adds information about image_path, style, cell type, and corresponding code into a JSON file.   
This JSON file is read by JavaScript and the elements are placed on an HTML page.

# Notebook formatting
Formatting with black can be done this way:
`black --python-cell-magics capture_png  docs/gallery.ipynb`


# Attribution

Thanks to @christopher-besch for discussing the project architecture with me.
Thanks to @krassowski for the help to caputre the png output images.
Thanks to @Rickaym for some inspirations about the JSON files and VS Code related things.