# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Interact

# <markdowncell>

# The `interact` function provides a high-level interface for creating user interface controls to use in exploring code and data interactively.

# <codecell>

from IPython.html.widgets import interact, interactive, fixed
from IPython.html import widgets
from IPython.display import clear_output, display, HTML

# <headingcell level=2>

# Basic interact

# <markdowncell>

# Here is a simple function that displays its arguments as an HTML table:

# <codecell>

def show_args(**kwargs):
    s = '<h3>Arguments:</h3><table>\n'
    for k,v in kwargs.items():
        s += '<tr><td>{0}</td><td>{1}</td></tr>\n'.format(k,v)
    s += '</table>'
    display(HTML(s))

# <codecell>

show_args(a=10, b='Hi There', c=True)

# <markdowncell>

# Let's use this function to explore how `interact` works.

# <codecell>

i = interact(show_args,
         Temp=(0,10),
         Current=(0.,10.,0.01),
         z=True,
         Text=u'Type here!',
         #Algorithm=['This','That','Other'],
         a=widgets.FloatSliderWidget(min=-10.0, max=10.0, step=0.1, value=5.0, description="Float (a)")
         )

# <codecell>

i.widget

# <codecell>


