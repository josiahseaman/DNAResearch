# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=4>

# These were copied out of Notebook_Experimentation when the were all grown up.

# <codecell>

from pylab import *
from math import ceil
from PIL import Image

# <codecell>

class Pic():
    def __init__(self, data, width=None, height=None):
        self.width = width if width else int(sqrt(len(data))) #TODO: 2D arrays
        self.height = height if height else int(ceil(len(data) / width))
        self.data = data
        
    def set_width(self, width):
        self.width = width
        self.height = int(ceil(len(self.data) / width))
        #you could clip the data...  self.data = self.data[:width*self.height]
        
    def show(self):
        im = Image.new('L', (self.width, self.height))
        im.putdata(self.data)
        imshow(im, cmap=cm.Greys_r, interpolation='nearest')
        
    def __repr__(self):
        self.show()  #this actually get the graph out there
        return str((self.width, self.height))

# <codecell>

from collections import defaultdict
class NucleotideDisplay(Pic):
    color_map = defaultdict(lambda: (125,125,125), A=(0,0,0), G=(0,255,0), C=(255,0,0), T=(0,0,255)) #color RGB
    def __init__(self, data):
        width = int(sqrt(len(data)))
        super().__init__(data, width=width)
        
    def show(self):
        im = Image.new('RGB', (self.width, self.height))
        im.putdata(self.nucleotide_to_color(self.data))
        imshow(im, interpolation='nearest')
        
    def nucleotide_to_color(self, sequence):
        #Pad with extra gray pixels?
        return [self.color_map[nucleotide] for nucleotide in sequence]

# <headingcell level=5>

# Use 2D histogram for Oligomer Display and Isochore Heatmap  http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist2d

# <headingcell level=3>

# Iso-surfaces

# <markdowncell>

# Is there anything in Skittle Research we could use iso-surfaces for?
# * threshholding boundaries between DNA elements
#    * ...in Nucleotide Display when it's very zoomed out

# <codecell>


