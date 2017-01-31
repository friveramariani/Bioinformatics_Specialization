__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def immediate_neighbors(pattern):
    dna = ['A', 'G', 'T', 'C']
    neighborhood = set([pattern])
    #print('Line two: ' + str(neighborhood))
    for i in range(len(pattern)):
        for letter in dna:
            neighborhood.add(''.join([pattern[:i] + letter + pattern[i+1:]]))
    return neighborhood


def neighbors(pattern, d):
    neighborhood = set([pattern])
    for i in range(d):
        for x in neighborhood:
            neighborhood = neighborhood.union(immediate_neighbors(x))
    return neighborhood

#print(immediate_neighbors('ATT'))
#print(neighbors('ATT',1))


def KM(p,l):
    L = []
    for i in range(0,len(p)-l+1):
        L += [p[i:i+l]]
    return L
#print(KM('ATTTGGC',3))

def motif_enumeration(dna,k,d):
    K = []
    D = {}
    S = set()
    for i in dna:
        S = set()
        K = KM(i,k)
        #print(K)
        for i2 in K:
           #print(i2)
           S = S.union(neighbors(i2,d))
        #print(S)
        D[i] = S
    return list(set.intersection(*D.values()))
    #print(set.intersection(*D.values()))


DN = ['GTTAGTGTAGACGGGGTAAGGGCTC',
'TATTGCAGATGTTGAACGGGTTCGG',
'TGTAAACGAGCGGGTCATGCAATGT',
'CATCTGTCCGACGGGCTGGTTCATA',
'CCCACAAGTGGTGCGACTCAACGAG',
'AGCGCGGTCGGCCGTTATTAACGAG']
KK = 5
DD = 1
pp = (motif_enumeration(DN,KK,DD))
for i in pp:
    print(i, end = ' ')
