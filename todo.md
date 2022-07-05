# TODO:

current project folder structure:

* docs: example of a minimal  plywood gallery, can be seen on github pages
* plywood_gallery: stuff, that will be delivered by pip install (infrastructure+templates)

# Version number changes

+ in Project.toml

## tasks:

* find new fonts for html
* optimize CSS template in "Minimal Gallery"
* Add screen recordings
* better batch infrastructure
* Make YAML robust when parameter is not provided
* Implementing more tests
* Maybe test the cell magic with a default notebook and https://github.com/chrisjsewell/pytest-notebook ?
* write documentation
* Hyperlinks for the chapter names
* Continue writing the readme
* make the "NOT" operator optional 
* prof read readme again
* Always show Code of Header with 50% opacity 


* Make gallery for
    * py ffmpeg
    * Matplotlib plottypes https://matplotlib.org/devdocs/plot_types/index.html 
    * Clusteralgorithmen https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html in plywood gallery umwandeln
    * More Pathlib examples, e.g. for  :

```python=
from pathlib import Path

base_directory = Path("/ceph/uprp/work/AG_Salditt/2021/GINIX/run100/JHM/PCLS_ROD_3_A_PCO_tomo01")
include_text = "PCLS"
exclude_text = "BINNED"
suffix = ".raw"

file_names = []
for subp in base_directory.rglob("*"): # using python assignment operator: x &= 3 equals x = x & 3
    cond = True
    cond &= include_text in subp.name
    cond &= exclude_text not in subp.name
    cond &= (suffix == subp.suffix)
    if cond is True:
        file_names.append(subp)
file_names.sort()
print(*file_names, sep="\n")
```

* better chapter managing:
* update dict:
```python=
# Python code to merge dict using update() method

dict1 = {'A': 10, 'B': 2}
dict2 = {'c': 3, 'A': 4}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
 
# changes made in dict2
print(dict2)
```



## Whislist:
* Copy button to the code cells
* find better cell IDs so user does not have to give names
* maybe add image alt
* parameter "Titel" in JSON 
* parameter "HoverText" in JSON  (?)
* Filter cells by search bar
* Websiteperformance: Lazy load images on Website visit
* Animated code transitions
* experimental_iterator_capture_png
* Parameterslider for certain variables might be possible?
* Plywood Notebooks with three colors and hierarchical execution (tree-based execution, maybe with caching?)
* Re-Execute PlywoodGallery with own variables in jupyter notebook to enable predictable coding, similar to https://github.com/lux-org/lux
* Renderer to pdf cheatsheet

## pipe dreams

A neural network that is trained by images as input data and code as prediction.
Similar, to detexify https://detexify.kirelabs.org/classify.html , one can draw a picutre of the thing one wants to achieve (barplot, 3D view, scatter, etc) and Plywood will provide you possible code snippets to achieve this resul, similar to CodePilot.



# Possible usecase: 
Gallery,   
Part of sphinx documentation,  
Cheat Sheet,  
Version control  
Personal snippet generator

All kinds of images can be used: 
* For graphical output, best use the graphical output
* For snippets without graphical output, use any placeholder image:
Emoji combinations, bootstrap icons, a Landscape, your favorite cartoon character, cute  cats, image of your grandparents, any mnemonic aid that gives an association with the code snippet. 
