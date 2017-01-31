__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import random

def randomMotifs(dna,k,t):

    kmm = []
    sc = []
    k = 3
    D = {}
    for i in range(0,len(dna)):
        km = []
        for kk in range(len(dna[i])-k+1):
            km += [dna[i][kk:kk+k]]
        D[i] = km
    for m in range(0,t):
        ran = random.randint(0,len(D[0])-1)
        kmm += [D[m][ran]]

    return kmm


def ProfileWithPseudocounts(Motifs):


    t = len(Motifs)
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs) # output variable
    for symbol in profile:
        for kk in range(0,len(profile[symbol])):
            profile[symbol][kk] = profile[symbol][kk]/(len(Motifs) + 4)

    return profile


def CountWithPseudocounts(Motifs):

    count = {}
    for i in 'ACGT':
        count[i] = []
        for ii in range(len(Motifs[0])):
            count[i].append(1)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count



def Score(Motifs):


    count = 0
    L = Consensus(Motifs)
    for i in Motifs:
        for chr1, chr2 in zip(i,L):
            if chr1 != chr2:
                count += 1
    return count


def Consensus(Motifs):



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

    return count


def RandomMotifs(dna,k,t):

    kmm = []
    sc = []
    D = {}
    for i in range(0,len(dna)):
        km = []
        for kk in range(len(dna[i])-k+1):
            km += [dna[i][kk:kk+k]]
        D[i] = km
    for m in range(0,t):
        ran = random.randint(0,len(D[0])-1)
        kmm += [D[m][ran]]

    return kmm

def Motifs(pf,dna):

    k = len(pf['A'])
    D = []
    for i in range(0,len(dna)):
        km = []
        sc = []
        for kk in range(len(dna[i])-k+1):
            km += [dna[i][kk:kk+k]]
        for i in km:
            sc += [Pr(i,pf)]
        D += [km[sc.index(max(sc))]]

    return D


def Pr(Text, Profile):

    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]

    return p


def RandomizedMotifSearch(Dna, k, t):

     M = RandomMotifs(Dna, k, t)
     BestMotifs = M

     while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
