# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Ipython Notebook2.0 supports interactive widgets and javascript.  Consider doing: https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/VxxwGoET1CE

# <codecell>

%pylab inline

# <codecell>

from PIL import Image
im = Image.new('L', (4,3))
im.putdata([1,2,3,5,4,6,7,])
imshow(im, cmap=cm.Greys_r, interpolation='nearest')

# <codecell>


# <codecell>

from io import BytesIO

from IPython.core import display
from PIL import Image


def display_pil_image(im):
   """Displayhook function for PIL Images, rendered as PNG."""

   b = BytesIO()
   im.save(b, format='png')
   data = b.getvalue()

   ip_img = display.Image(data=data, format='png', embed=True)
   return ip_img._repr_png_()


# register display func with PNG formatter:
png_formatter = get_ipython().display_formatter.formatters['image/png']
dpi = png_formatter.for_type(Image.Image, display_pil_image)

# <codecell>

from PIL import Image
from PIL.ImageDraw import Draw
img = Image.new("RGBA", (100, 100))
draw = Draw(img)
draw.rectangle(((0,0), (100, 100)), fill=(255, 100, 0))
# img.save("foo.png")
imshow(img)

# <codecell>


