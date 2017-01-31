__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


#  Write a function RandomMotifs(Dna, k, t) that uses random.randint to choose a random k-mer from each of t different
#  strings Dna, and returns a list of t strings.


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


t = 5
p1 = {'A':[0.8, 0.0, 0.0, 0.2],'C':[0.0, 0.6, 0.2, 0.0],
      'G':[0.2, 0.2, 0.8, 0.0],'T':[0.0, 0.2, 0.0, 0.8]}
dn1= ['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
print(randomMotifs(dn1,p1,t))