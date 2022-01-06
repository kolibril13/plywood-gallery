# plywood

This repo will turn your jupyter cell output images into a gallery, that enables you to quickly acsess your code by clicking on the gallery enteries. Thereby, one can distinguish three cell types: "Header", "Normal" and "Dependend". 
You can find an example gallery here: https://kolibril13.github.io/plywood/   
*Add Screenrecording Here*  
**NOTE : Still work in progress, there might be breaking changes**

# Installation
Download this repo. (pypi package might come soon)  
Add your code to `gallery.ipynb`.  
Open `index.html`  
Start coding! 

# Intended workflow:

Add the **`%%capture_png`** magic in Jupyter cells and the output images will automatically and in real time be added to your gallery.   
There will be two phases of building the gallery, the *preparation phase* and the *deployment phase.*

## 1. Preparation phase

During the preparation phase, you can tinker around your cells and debug them and run them again and again.

Every single cell run will create a new entery in the plywood gallery, so running cell A and cell B  in the order AABABB will also display the cells in the order AABABB and no previous cells will be overwritten.
This behaviour can be also used to have an visual version control system of your notebook execution history.
This is nothing else then a visual notebook execution history and therefore can be used as a version control systems about how your plots and graphics evolve over the preparation process. 

There is no "replace plywood gallery entery" yet, but might be implemented in future, that would render AABABB to AB.

## 2. Deployment phase

When you want to publish your gallery notebook e.g. on Github pages, then first clean all cells from the preoparation phase with the chaptermanager  
```py
from plywood_gallery import chaptermanager
chaptermanager.remove("ChapterName")
```
and all previous cells will be deleted.
Next, restart the kernel and click "Run All".

**Why is the kernel restart necessary?**  
In the deployment phase, it is very important that cells are executed from top to button with a fresh started kernel to avoid unwanted artifacts from the preperation phase.

# User guide

**Chapters**  
New chapters will be added by assigning the the variable `chapter_name`, e.g. `chapter_name = "2D Arrays"`
As soon as there is a new name assigned, this new chapter will be added in the gallery below.
Chapters can be sorted by 
```py
from plywood_gallery import chaptermanager
chaptermanager.sort(["2D Array", "3D Arrays"])
```

**Cellmagic**  
One can run the `%%capture_png` with three arguments:
```
--path: (required)
    the path where the image will be saved to
--celltype: (optional)
    Cell can be of type 'Normal', 'Header', and 'Dependend'
--style: (optional)
    Add extra css style for the gallery enteries
```
**--path**:  
A basic cell can look like this:
```py
%%capture_png --path imgs/MyExample.png
import matplotlib.pyplot as plt
plt.plot([1,2],[10,20])
```
This will generate the file `imgs/2D_Arrays_001_MyExample.png`. Note that plywood makes sure that file names are unique and can be easily sorted in the file explorer.
Running this cell again would generate `imgs/2D_Arrays_002_MyExample.png`.   
**--style**:  
Change the gallery enteries size, border width or whatever is possible in css!  
**--celltype**:    
This is a very powerful feature that has to be used carefully.  
Here is their purpose:  

* **Header:**
Define imports and make definitions of functions

* **Normal:**
Show usage of imports and functions that you've made in the header cell. WARNING: All normal cells should ALWAYS be independent of each other. Try to not change variables in these cells, and if you have to, make sure to not use them in other normal cells agian. If you need to use them again, make sure to rest their value before adding another "Normal cell". This is crutial, because a user should always be able to run the cell in the combination "Header+Normal"
* **Dependend**:  
The purpose of this cell is to show slight changes of function calls or post-processing of what happend in a "Normal cell". It should only have a very few lines of code, and only change as few parameters as possible. That makes it possible, to see the slight visual adjustments in plots, and then easyly associate the codechanges with the visual changes. "Dependend" Cells can be run in the combination "Header+Normal+Dependend", but also "Header+Normal+Dependend+Dependend".



**SideNote**: Currently, Sphinx documentation suffers from cluttering: Most useres want to have one line of code to see how to apply 
As this adds an extra layer of complexity in the writing process of documentation, the benefit can be tremendous:



# Outlook:
As soon as you have your gallery, it will be easy to create vs Code extensions from it:  
*Add Screenrecording Here*


# Tips and Tricks:

* Best you run the notebook in a jupyter notebook instance and open the website seperate (e.g. with splitscreen or second monitor) to keep track of the live updates.

* Multiple notebooks can be used for the same gallery

# How it works: