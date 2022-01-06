# plywood

This repo will turn your jupyter cell output images into a gallery html page, that enables you to quickly acsess your code by clicking on the gallery enteries. Thereby, one can distinguish three cell types: "Header", "Normal" and "Dependend". 
You can find an example gallery here: https://kolibril13.github.io/plywood/   
*Add Screenrecording Here*
**NOTE : Still work in progress, there might be breaking changes**

# Installation
Download this repo. (pypi package might come soon)
Add your code to `gallery.ipynb`.
Open `index.html`
Start coding! 

# Intended workflow:

* Add the **`%%capture_png`** magic in Jupyter cells and the output images will automatically and in real time be added to your gallery. 

* there will be two phases of building the gallery: preparation phase & deployment phase

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
Next, restart the kernel and click "Run ALl".

**Why is kernel restart necessary?**  
In the deployment phase, it is very important that cells are executed from top to button with a fresh started kernel to avoid unwanted artifacts from the preperation phase.

## User guide
New chapters will be added by assigning the the variable `chapter_name`, e.g. `chapter_name = "3D Arrays"`
As soon as there is a new name assigned, this new chapter will be added in the gallery below 


* documentation schreiben in github readme:
    * "INCLUDE ONLY" "NOT"




# Outlook:
As soon as you have your gallery, it will be easy to create vs Code extensions from it:
*Add Screenrecording Here*


## Tips and Tricks:

* Best you run the notebook in a jupyter notebook instance and open the website seperate (e.g. with splitscreen or second monitor) to keep track of the live updates.

* Multiple notebooks can be used for the same gallery