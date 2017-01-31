__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

def Count(Motifs):
    count = {}
    for i in 'ACGT':
        count[i] = []
        for ii in range(len(Motifs[0])):
            count[i].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    #for symbol in count:
        ##count[symbol][kk] = count[symbol][kk]/len(Motifs)
    return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    for i in 'ACGT':
        profile[i] = []
        for ii in range(len(Motifs[0])):
            profile[i].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1
    for symbol in profile:
        for kk in range(0,len(profile[symbol])):
            profile[symbol][kk] = profile[symbol][kk]/len(Motifs)

    return profile

def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    count = 0
    L = Consensus(Motifs)
    for i in Motifs:
        for chr1, chr2 in zip(i,L):
            if chr1 != chr2:
                count += 1
    return count
#To implement a function Pr(Text, Profile), we begin by setting a “probability” variable p equal
# to 1. We then range through the characters of Text one at a time. At position i of Text, we set
# p equal to p times the value of Profile corresponding to symbol Text[i] and column i, which is
# just Profile[Text[i]][i].

def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p

def ProfileMostProbablePattern(Text,k,Profile):

    L = []
    for ii in range(len(Text)- k +1):
        L += [Text[ii:ii+k]]
    L =  list(set(L))

    D = {}
    for iii in range(0,len(L)):
        D[L[iii]] = Pr(L[iii],Profile)
    max_val = max(D.values())
    mx = ''
    for kk in D:
        if D[kk] == max_val:
            mx += kk
    return mx

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
