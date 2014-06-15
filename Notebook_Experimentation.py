# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

# <codecell>

%reload_ext Display_Utils
from Display_Utils import Pic, NucleotideDisplay

# <codecell>

from PIL import Image
im = Image.new('L', (4,10))
im.putdata([1,2,3,5,4,6,7,2,3,0,4,4])
imshow(im, cmap=cm.Greys_r, interpolation='nearest')

# <codecell>

Pic([1,2,3,4,5,6], 2)

# <codecell>

ceil?

# <codecell>

im = Image.new('RGB', (2,2))
im.putdata([(255,0,0), (0,255,0), (0,0,255), (0,0,0)])
imshow(im, interpolation='nearest')

# <codecell>

nd = NucleotideDisplay('AAGCTAGCGCAGACTCAGCACACACACGCTCGATGCACTGCATCCGATCGACGCCTAGCATCGACTCAGCAT')
nd

# <codecell>

from IPython.html.widgets import interact, interactive, fixed
from IPython.html import widgets
from IPython.display import clear_output, display, HTML

def width_slide(Width):
    nd.set_width(Width)
    nd.show()

# <codecell>

interact(width_slide, Width=(1,40))

# <codecell>


