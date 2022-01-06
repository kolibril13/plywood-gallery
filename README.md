# plywood
## https://kolibril13.github.io/plywood/
This repo will turn your jupyter cell output images into a gallery html page, that enables you to quickly acsess your code by clicking on the gallery enteries:  
*Screenrecording Here*


## Intended workflow:

* Add the **`%%capture_png`** magic in Jupyter cells and the output images will automatically and in real time be added to your gallery. 

* there will be two phases of building the gallery: preparation phase & deployment phase

### 1. Preparation phase

During the preparation phase, you can tinker around your cells and debug them and run them again and again.

Every single cell run will create a new entery in the plywood gallery, so running cell A and cell B  in the order AABABB will also display the cells in the order AABABB and no previous cells will be overwritten.
This behaviour can be also used to have an visual version control system of your notebook execution history.
This is nothing else then a visual notebook execution history and therefore can be used as a version control systems about how your plots and graphics evolve over the preparation process. 

There is no "replace plywood gallery entery" yet, but might be implemented in future, that would render AABABB to AB.

### 2. Deployment phase

When you want to publish your gallery notebook on Github pages, then first clean all cells from the preoparation phase with the chaptermanager  
```py
from plywood_gallery import chaptermanager
chaptermanager.remove("ChapterName")

```
and all previous cells will be deleted.
Next, restart the kernel and click "Run ALl".

**Why is kernel restart necessary?**  
In the deployment phase, it is very important that cells are executed from top to button with a fresh started kernel to avoid unwanted artifacts from the preperation phase.



## Tips and Tricks:

Best you run the notebook in a jupyter notebook instance and open the website seperate (e.g. with splitscreen or second monitor) to keep track of the live updates.



# Usage Currently:

Download this repo.
Add your code to `gallery.ipynb`.
Open `index.html`
Start coding! 


# In Future (NOT YET!):

pip install plywoodGallery
run generate_template.py
Add your code to `gallery.ipynb`.


##  Usage:
* add `%%capture_png imgs/example.png` into a directory


* documentation schreiben in github readme:
    * "INCLUDE ONLY" "NOT"





## Todo:
* add a copy button to the code cells
* find better cell IDs
* maybe add image alt


#### Warning: This repo is only a proof of concept, and very much work in progress
