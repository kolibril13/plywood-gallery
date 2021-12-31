from IPython.core.magic import register_cell_magic
                                

@register_cell_magic
def cmagicXX(line, cell):
    get_ipython().run_cell_magic(
        'capture',
        ' --no-stderr --no-stdout result',
        cell
    )
    argument_array= line.split('-style')
    path = argument_array[0]
    path.replace(" ", "")
    style = str(*argument_array[1:])
    style=style.lstrip() # remove leading whitespace
    print(path)
    print(style)
    
    #print(type(line))
    #return line, cell