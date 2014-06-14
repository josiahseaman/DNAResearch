# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pylab import *
import random
from random import choice

# <codecell>

alphabet = ['A', 'C', 'G', 'T']
monomer = 'ACCGCTAGAAAT'
monomer * 10

# <codecell>

def debugSequence(maxFrequency, sectionLength, startFrequency=1):
    seq = ''
    for frequency in range(startFrequency, maxFrequency+1):
        monomer = ''.join([choice(alphabet) for index in range(frequency)])
        copies = ceil(sectionLength / frequency)
        repeat = monomer * copies
        seq += (repeat)
    return seq

# <codecell>

debugSequence(5, 20, 3)

# <codecell>

biases = [('TTT', 80995),
('TCT', 38027),
('TAT', 63937),
('TGT', 19138),
('TTC', 58774),
('TCC', 33430),
('TAC', 44631),
('TGC', 22188),
('TTA', 52382),
('TCA', 32715),
('TAA',  7356),
('TGA',  3623),
('TTG', 47500),
('TCG', 31146),
('TAG',   989),
('TGG', 50991),
('CTT', 43449),
('CCT', 27340),
('CAT', 45879),
('CGT', 73197),
('CTC', 37347),
('CCC', 19666),
('CAC', 34078),
('CGC', 72212),
('CTA', 15409),
('CCA', 31534),
('CAA', 53394),
('CGA', 13844),
('CTG',177210),
('CCG', 76644),
('CAG',104171),
('CGG', 21552),
('ATT',109072),
('ACT', 37842),
('AAT', 75436),
('AGT', 36097),
('ATC', 86796),
('ACC', 80547),
('AAC', 78443),
('AGC', 55551),
('ATA', 24984),
('ACA', 33910),
('AAA',129137),
('AGA', 13152),
('ATG', 96695),
('ACG', 50269),
('AAG', 45459),
('AGG',  7607),
('GTT', 72584),
('GCT', 62479),
('GAT',119939),
('GGT', 93325),
('GTC', 52439),
('GCC', 88721),
('GAC', 70394),
('GGC', 99390),
('GTA', 42420),
('GCA', 77547),
('GAA',143353),
('GGA', 34799),
('GTG', 89265),
('GCG',110308),
('GAG', 68609),
('GGG', 41277),]

# <codecell>

import random
def weighted_choice(items, probs, bincount=10000):
  '''Puts items in bins in proportion to probs
  then uses random.choice() to select items.
 
  Larger bincount for more memory use but
  higher accuracy (on avarage).'''
 
  bins = []
  for item,prob in zip(items, probs):
    bins += [item]*int(bincount*prob)
  while True:
    yield random.choice(bins)

# <codecell>

codons, weights = ([entry[0] for entry in biases], [entry[1] for entry in biases])
total = sum(weights)
probabilities = [w / total for w in weights]
probabilities

# <codecell>

itera = weighted_choice(codons, probabilities)
for dummy in range(10):
    print(itera.__next__())

# <codecell>

generator = weighted_choice(codons, probabilities)

# <codecell>

weighted_sequence = ''.join(generator.__next__() for x in range(1000))
weighted_sequence

# <codecell>

debugSequence(5, 200, 3)

# <codecell>


