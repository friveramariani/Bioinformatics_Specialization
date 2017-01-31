__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import sys

kmers = [s for s in"""
ATGCG
GCATG
CATGC
AGGCA
GGCAT
""".split() if s]

def reconstruct_string(kmers):
# Initializes string to be returned with a reconstructed dna string
    reconstructedString = ''
    reconstructedString += kmers[0]
# Compares ith kmer's last k-1 symbols to ith+1 kmer's first k-1 symbols
    for i in range(len(kmers) - 1):
        if kmers[i][-(len(kmers[0]) - 1):] == kmers[i+1][:(len(kmers[0]) - 1)]:
            reconstructedString += kmers[i+1][-1:]
# Returns output
    return reconstructedString

print (reconstruct_string(kmers))