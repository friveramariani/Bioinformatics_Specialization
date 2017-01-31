
__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Code Credit: Course's Default.




def Score(Motifs):
    count = 0
    L = Consensus(Motifs)
    for i in Motifs:
        for chr1, chr2 in zip(i,L):
            if chr1 != chr2:
                count += 1
    return count

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
def pm(dna,pf):
    km = []
    sc = []
    k = len(pf['A'])
    for i in range(0,len(dna)-k+1):
        km += [dna[i:i+k]]
    for i in km:
        sc += [Pr(i,pf)]
    return km[sc.index(max(sc))]

def Pr(Text, Profile):
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    #Motifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(pm(Dna[j],P))
        if Score(Motifs) < Score(BestMotifs):
                 BestMotifs = Motifs
    return BestMotifs

k1 = 3
t1 = 5
txt = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']

print(GreedyMotifSearch(txt,k1,t1))