__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
    genome = file.readline()
genome = genome[:-1]

def suffixarray(genome):
    substrings = {}
    n = len(genome)
    for i in range(n-1, -1, -1):
        substrings[genome[i:]] = i
    keys =  sorted(substrings)
    for key in keys:
        print str(substrings[key]) + ', ',

if __name__ == '__main__':
    suffixarray(genome)
