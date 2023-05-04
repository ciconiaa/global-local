from Bio import motifs
from Bio.Seq import Seq
seq = [
       Seq(input("Put your 1st sequence\n")),
       Seq(input("Put your 2nd sequence\n")),
       Seq(input("Put your 3rd sequence\n")),
       Seq(input("Put your 4th sequence\n")),
       Seq(input("Put your 5th sequence\n")),
       ]

import numpy as np
n = len(seq)
m = motifs.create(seq)

print("A:", np.divide(m.counts['A'],n))
print("T:", np.divide(m.counts['T'],n))
print("G:", np.divide(m.counts['G'],n))
print("C:", np.divide(m.counts['C'],n))
