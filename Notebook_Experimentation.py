# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

# <codecell>

from IPython.html.widgets import interact, interactive, fixed
from IPython.html import widgets
from IPython.display import clear_output, display, HTML

# <codecell>

from PIL import Image
im = Image.new('L', (4,4))
im.putdata([1,2,3,5,4,6,7,2,3,0,4,4])
imshow(im, cmap=cm.Greys_r, interpolation='nearest')

# <codecell>

Pic([1,2,3,4,5,6], 2)

# <codecell>

im = Image.new('RGB', (2,2))
im.putdata([(255,0,0), (0,255,0), (0,0,255), (0,0,0)])
imshow(im, interpolation='nearest')

# <codecell>

%reload_ext Display_Utils
from Display_Utils import Pic, NucleotideDisplay

# <codecell>

nd = NucleotideDisplay('AAGCTAGCGCAGACTCAGCACACACACGCTCGATGCACTGCATCCGATCGACGCCTAGCATCGACTCAGCAT')
nd

# <codecell>

interactive_nucleotide = interact(width_slide, Width=(1,40))

# <codecell>


# <codecell>

interactive_nucleotide.widget

# <codecell>

widgets.IntTextWidget().keys

# <codecell>

int_range = widgets.IntSliderWidget()
display(int_range)

def on_value_change(name, value):
    print(name, value)

int_range.on_trait_change(on_value_change)

# <codecell>

int_range.max = 10

# <codecell>

def new_button(clicked):
    button = widgets.ButtonWidget()
    button.clicks = 0
    clicked.clicks += 1
    button.description = "%d" % clicked.clicks
    display(button)
    button.on_click(new_button)
button = widgets.ButtonWidget(description = "Start")
button.clicks = 0
display(button)
button.on_click(new_button)

# <codecell>

container = widgets.ContainerWidget()
display(container)
container.children = [widgets.IntSliderWidget()]

# <codecell>

container.children.append(widgets.IntProgressWidget())

# <codecell>

container.children

# <codecell>

form = widgets.ContainerWidget()
first = widgets.TextWidget(description="First Name:")
last = widgets.TextWidget(description="Last Name:")

student = widgets.CheckboxWidget(description="Student:", value=False)
school_info = widgets.ContainerWidget(visible=False, children=[
    widgets.TextWidget(description="School:"),
    widgets.IntTextWidget(description="Grade:", min=0, max=12)
    ])

pet = widgets.TextWidget(description="Pet's Name:")
form.children = [first, last, student, school_info, pet]
display(form)

def on_student_toggle(name, value):
    if value:
        school_info.visible = True
    else:
        school_info.visible = False
student.on_trait_change(on_student_toggle, 'value')

# <codecell>

label = widgets.LatexWidget()
label.value = "$\\textbf{ALERT:} Hello World!$"
container = widgets.ContainerWidget(children=[label])

# # set_css used to set a single CSS attribute.
# container.set_css('border', '3px solid black') # Border the container

# # set_css used to set multiple CSS attributes.
# container.set_css({'padding': '6px', # Add padding to the container
#                    'background': 'yellow'}) # Fill the container yellow

display(container)
container.add_class('corner-all')
label.add_class('alert')

# <codecell>

display(container)

# <codecell>

import time
label = widgets.LatexWidget(value = "$\\textbf{ALERT:} Hello World!$")
display(label)

# Apply twitter bootstrap alert class to the label.
label.add_class("alert")

# Animate through additional bootstrap label styles 3 times
additional_alert_styles = ['alert-error', 'alert-info', 'alert-success']
for i in range(100 * len(additional_alert_styles)):
    label.add_class(additional_alert_styles[i % 3])
    label.remove_class(additional_alert_styles[(i-1) % 3])
    time.sleep(1)

# <codecell>

import time
label = widgets.LatexWidget(value = "$\\textbf{ALERT:} Hello World!$")
display(label)

# Apply twitter bootstrap alert class to the label.
label.add_class("alert")

# Animate through additional bootstrap label styles 3 times
additional_alert_styles = ['alert-error', 'alert-info', 'alert-success']
for i in range(3 * len(additional_alert_styles)):
    label.add_class(additional_alert_styles[i % 3])
    label.remove_class(additional_alert_styles[(i-1) % 3])
    time.sleep(1)

# <codecell>

import time
labe = widgets.LatexWidget(value = "$\\textbf{ALERT:} Hello World!$")
display(labe)

# Apply twitter bootstrap alert class to the label.
labe.add_class("alert")

# Animate through additional bootstrap label styles 3 times
additional_alert_styles = ['alert-error', 'alert-info', 'alert-success']
for i in range(3 * len(additional_alert_styles)):
    labe.add_class(additional_alert_styles[i % 3])
    labe.remove_class(additional_alert_styles[(i-1) % 3])
    time.sleep(1)

# <codecell>

print('hi')

# <codecell>

import winsound
def annoy():     
    for i in range(1, 10):             
        winsound.Beep(i * 100, 200)

annoy()

# <codecell>


