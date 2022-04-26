# TODO:

current project folder structure:

* docs: example of a minimal  plywood gallery, can be seen on github pages
* plywood_gallery: stuff, that will be delivered by pip install (infrastructure+templates)

# Version number changes

+ in Project.toml

## tasks:

* setup auto release
* check all flake8 warnings 
* Add screen recordings
* Make YAML robust when parameter is not provided
* Implementing more tests
* Maybe test the cell magic with a default notebook and https://github.com/chrisjsewell/pytest-notebook ?
* write documentation
* Hyperlinks for the chapter names
* Continue writing the readme
* doublecheck and refactor caputre_png cell magic
* make the "NOT" operator optional 
* prof read readme again


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
* Plywood Notebooks with thre colors and hierarchical execution (tree-based execution, maybe with caching?)
* Re-Execute PlywoodGallery with own variables in jupyter notebook to enable predictable coding, similar to https://github.com/lux-org/lux

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