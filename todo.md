# Todo:

current project structure:

+ Use jinja2 Templates! :)

* docs: index.html, generate_entries.js , minimal_examply.ipynb, that are under actrive development and published on github pages
* dummy: only debugging stuff, todo list
* plywood_gallery: stuff, that will be delivered by pip install
* template: index.html, generate_entries.js , minimal_examply.ipynb that are used to generate quickstart examples for users.


# Important things to consider before release:
* How to provide the html page? Best idea: 
```
pip install plywood_gallery
```

```py
>>> from plywood_gallery import `quickstart`
>>> quickstart()
```

Then got to `gallery.ipynb` and start coding.

# Version number changes

* in docs/javascript_entries.js
* in template/javascript_entries.js
+ in Project.toml

## Think of dependencies:
```
Ipython , Pillow, ipykernel, matplotlib, scipy, seaborn
```




# Installation
pip install plywoodX
run generate_template.py
Add your code to `gallery.ipynb`.


## Whislist:
* add a copy button to the code cells
* find better cell IDs so user does not have to give names
* maybe add image alt



# Possible usecase: 
Gallery, 
Part of sphinx documentation,
Cheat Sheet,
Version control
Personal snippet generator
