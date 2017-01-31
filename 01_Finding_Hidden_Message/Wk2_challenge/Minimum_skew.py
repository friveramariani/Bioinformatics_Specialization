__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

#  Minimum Skew Problem:  Find a position in a genome where the skew diagram attains a minimum.
#  Input: A DNA string Genome. 
#  Output: All integer(s) i minimizing Skew[i] among all values of i (from 0 to len(Genome)).

# Sample Input:
#    TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

# Sample Output:
#    11 24

from Skew import skew

def minimum_skew(Genome):

    positions = []
    D = skew(Genome)
    min_value = min(D.values())
    V = [x for x in D.values()]

    positions += [i for i,x in enumerate(V) if x == min_value]

    return positions
