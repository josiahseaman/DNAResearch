# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%matplotlib inline
from pylab import *
import matplotlib.pyplot as plt
from IPython.core.display import Image

# <codecell>

data = []
for y in range(10):
    data.append([y+x for x in range(10)])
# print(data)
Image(data=data)

# <headingcell level=1>

# Matplot Lib

# <codecell>

alpha = 0.7
phi_ext = 2 * pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * cos(phi_p)*cos(phi_m) - alpha * cos(phi_ext - 2*phi_p)
phi_m = linspace(0, 2*pi, 100)
phi_p = linspace(0, 2*pi, 100)
X,Y = meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

# <codecell>

fig, ax = plt.subplots()

p = ax.pcolor(X/(2*pi), Y/(2*pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)

# <codecell>

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random

bignum = 10
data = []
for i in range(bignum):
    data.append([random.random() for x in range(bignum)])
mat = np.array(data)  #random.random((bignum, bignum))
X, Y = np.mgrid[:bignum, :bignum]

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
surf = ax.plot_surface(X,Y,mat)
plt.show()

# <headingcell level=2>

# Most simple Pixel Map

# <codecell>

def basic_func(x, y):
    return x+y

X, Y = np.mgrid[:bignum, :bignum]
Z = basic_func(X, Y)

# <codecell>

fig, ax = plt.subplots()
p = ax.pcolor(X, Y, Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)

# <headingcell level=2>

# Basic Repeat Map

# <codecell>

raster_width = 11
seq = 'TCTCGTGAACCGTTCTTTCCCGCGGACGTGATGGATGTGGGTGCCTTTATTTGCGACGATATGGTCCGTAAATTAGGTCTCGTTGTTTGTACCCTCTCACTTGGCCGCTTCAACTTTTTTCCGATAATGTCTAATGCACCGACGGAATTATTGTACAGAGTAGCAAGCTCAGGTTGCACGGCAGACCTTGCCGCGTCGGGTCTGCGCACCACCCAAATCTGGGCGCGTCTGGGCCTCGCTGCTACACTGGTTAACCATGCTTCAGACTCTGTGACGATGAAATATCCAAACGACGTTGAATAAAAACGACGGGGAGCGGCGGTGATTTTTATCAATCGCGGTGAAGCAGTTATGCTCGACATCTATTAACAACAGGAGAAAGGCGCCACCGCTCCGGTGTATTATACACTGGGCCGTTTGACCGTCTCATCGACGGGCAACATGACCAAACCGCACATGCATTTCTCGGGCCGAATCGCCCGCGCCTACTGGAAAGCCGGCTCTGGCGATTATGCCGATTTTGAAAGTTTTCTTTCATCCAAAGCGTATATTATTCAGTTTCAAATATCGACCTTGCTGAAGAAAATCAAAGTGATCTTTTTATTTAAAGGCAATGATGGCGATGTACTTAATCGTGCGATCGCTTTGCGGCAGGGCCCCCGTTGGAATAGATTTGATATGCAGGAGCTGTATCCGATCTGGCATATTCTGTCCAATTAACAGCGCAATATCAACGCTGCGCTGTCTCTGCTGGTCGGCGAACACGGACTGATTCAGTCTCCTTTGGCAGGTTTCGTACAAGGTACCACGCTGAGCGCCCTGGGCCAACGGGACTTTGCACTGCGTAAGGACGCAGTGGAAGTGGGCTCCCTGAACCCTGAAGCCGGTGAAGACAAACGTACGACCATCATCTTTACCTATGTACTGCAGCAGCAAGGTTACAAATCCGGTAAATGTTGCGGCGAGGATAAATATGACGTTATTCTGAAAGAAGGGATTATCTACTATACCGTAGTTCTGATCATCCGGGGCTTCAAAGATTCAGACAAGGACGAAGATGACGGACTTAAACATGCGCTTGAAGGATTCGAAGGCGAACGTGGCGCTGCTCTGTCGACTGTAGCATCCGCGTCCGCATGGAGGAGTGGTCAACATAACGGCACCACCCCTTCGTCAAAGGTGGCGCAAGAACTCCGCCAGAAACGCTGCAATTCCAATACAAACATCACCTGCCCACACGTAAACCTTGAACTTAACAAGATATATCGGCTCTTCCCGCTCCAAAACTAAAAGATACCGGACGTGATCGCGATCAGAGGCAAATACTTGACTCATAAGCTGTCAACGGTTGATTTACTGGGTTTTTCTCCGCCAACCTGTCTGCGCTTGCATGATTATGAAGCCGTGTCAGATCCGATGAAAGTGGCGAATTTCCATAACCAGATGGGTTTCTTGGTAGGCGATGCCATCTTCGTTCAGGAACTCATCAAACAGACGGTCGCGCTGATCATTAACAAAGTAAAAAACCCTGGTGGCCTGAAACAGCGAGCCTCAGAAAAACCGAACTCTCAGCTAGTTTGAGGTGGGTCTAATCATGAGCCAGCACTGCGCGACCGTGGGTCTCGTATTCTGGGTGAGCGCGTGCGTGACGATATTCTGTATCTTGTTAACATGGGTTTTAAACATTCGTTCTTGGCTGACCGTGTCATCATGATCAAGATTGAAGAAGAGCTGCATTTTCATACCCAGAGCTACGAGGTCACCTCGCTCGGACAGGGGGTCAGTAATTACCTGGTCACAGCCGATGCGAAAGCCCCAAAACGTCGCCAACTGGCATATCATCTTGGTACTGGGTTCTCATCATTCTACGCTGGGGCGGATGATCAGGCGTCGCGCGTGGAAGTCAAACAGATGCAACGGATCCTGATTGCAGCCGCCCTGCCGGGCCTCCGAAAGAAATTGCGCCTGGATGCACACAATGAATTTATTGTCCCAATCATGACCGAGTTCGACCAGACCGGCCCCTTAACCTTAGGCTACGCATCAGAAAAACGCGCGCTCGATAACATCATGGTGAGTCAGGATTCTGTGCTGGGGAATCTCTTTATGAAATTTTTAGGTGTGCTGGTGGTCGGTATCAGCCGGACAGCGATAGCGGACCCAGATAAGTATATGGCTATTCTGCTGGGTGCGGTTTTCGACATGCTGGCGATGAAAATCATTGAAGTCTTAGATGTTACGTCCAACCGCAACTATTTGACCAATCGCCGTACGACGGAAATCGCAGCTGTGGCAGAAACCTGTGAGGACGGAGCGTTTGTGATGCTGCTGACCACGTGGCTGGGCAAGAAGTCGGATTCCCTGAAGTTCCCTAACTTAGTGATTGTCTATTATATAGTTATGGTCGGCGGCCCGTGCACCGGAGAGCAGCAGAAACGTGCTACAGCAGCCATGAGTAGCGAAATTGCGCTCCAGCCGTATTTCCGCTTCCGCCGGATTGAGCACACTGTCCGCGGCCGCGTCTTTTGACTGGAAAAAAGTTTCGGCGAAGACGCCGGCGATAATCTGGTCTCCAACAAAACCAAACGTCGCGGTAAAGGGCCGCAGTTTAAATATGTGGAACTGGCAGAACTGACCTTAATCAAGCTGTCGATTTGAGGCGGTGTAGCTAACATGGGAGGTAATGCACGTCATGGAATGAAAGGCATTCTGGGTCCGCTGCGCGTTGCCTCTTTAGCTTATCAGGCGAAAGGTGTCATCGGTTTATCTATGTTAAAAAACTGGGCTCCGGCCTAACAAAAAAATCTGCTGTCAGTTGCTGTACTGGTCCCGCTGAGCGCGAGCACAGGGAGCGCCCTGGAAATGGTGCGCGGTCTGAAAGAAGGCAACGCAGTCTTGGTGGCGAAGATGGGGATCGCCAAAGGAGCGACAGGTCGCTGGGCGGCTGTGGCAGATGGTAACGTCGCACCTCCGCTTCGCGAGCAATTAAACTTTCAGGCT'

# <codecell>

seq = 'CTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTACTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTAGTTACTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGCCTTGC'

# <codecell>

seq[1*x_size: 1*x_size + raster_width]

# <codecell>

sum([True, False, True])

# <codecell>

x_size = 75 # frequency range
y_size = int(len(seq) / raster_width) # number of lines: (cut off the end)

# <codecell>

def repeat_score(x, y):
    start_str =  seq[y*raster_width     : (y+1)*raster_width]
    target_str = seq[y*raster_width + x : (y+1)*raster_width + x]
    actual_width = min(len(start_str), len(target_str))
    return sum([start_str[i] == target_str[i] for i in range(actual_width)])

# <codecell>

[[repeat_score(x,y) for x in range(1,x_size-1)] for y in range(y_size-10)]

# <codecell>

X, Y = np.mgrid[:x_size, :y_size]
Z = np.array([[repeat_score(x,y) for x in range(1,x_size+1)] for y in range(y_size)]).T

# <codecell>

fig, ax = plt.subplots()
p = ax.pcolor(X, Y, Z, 
              cmap=cm.Greys_r, 
              vmin=0, vmax=raster_width)
cb = fig.colorbar(p, ax=ax)

# <codecell>

x, y  = 20, 7
print( seq[y*x_size : y*x_size + raster_width])
print( seq[y*x_size + x : y*x_size + raster_width + x])
sum([start_str[i] == target_str[i] for i in range(raster_width)])

# <headingcell level=3>

# Notes

# <markdowncell>

# I most of the trouble that I had make this was because I am unfamiliar with NumPy arrays and matplotlib.  The lines for Z and p = ax.pcolor(X, Y, Z, cmap=cm.Greys_r, vmin=0, vmax=raster_width) are very sensitive.  The good and the bad of having a graphing platform is that I get scale axes for free.  It will often squish the pixels.  I prefer square pixels.  I need to figure out how to generate a highly non-square graph since the Repeat Map is usually 25 wide x 200 high.

# <headingcell level=1>

# Finished Product

# <codecell>

from Sequence_Utils import debugSequence, weighted_sequence

# <codecell>

class RepeatMap():
    def __init__(self, sequence):
        self.seq = sequence
        self.raster_width = 11
        self.x_size = 25 # frequency range
        self.y_size = int(len(self.seq) / self.raster_width) # number of lines: (cut off the end)
    
    def repeat_score(self, x, y):
        start_str =  self.seq[y*self.raster_width     : (y+1)*self.raster_width]
        target_str = self.seq[y*self.raster_width + x : (y+1)*self.raster_width + x]
        actual_width = min(len(start_str), len(target_str))
        return sum([start_str[i] == target_str[i] for i in range(actual_width)])

    def render(self):
        X, Y = np.mgrid[:self.x_size, :self.y_size]
        Z = np.array([[self.repeat_score(x,y) for x in range(1,self.x_size+1)] for y in range(self.y_size)]).T
        fig, ax = plt.subplots()
        fig.set_size_inches(self.x_size /10, self.y_size /10)
        p = ax.pcolor(X, Y, Z, 
                      cmap=cm.Greys_r,
                      vmin=0, vmax=self.raster_width)
        cb = fig.colorbar(p, ax=ax)
        plt.gca().invert_yaxis()

# <codecell>

rp = RepeatMap(debugSequence(25, 200, 5))
rp.render()

# <codecell>


