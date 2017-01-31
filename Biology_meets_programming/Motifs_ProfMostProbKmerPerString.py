__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# Write a function Motifs(Profile, Dna) that takes a profile matrix Profile corresponding to a list of strings
# Dna as input and returns a list of the Profile-most probable k-mers in each string from Dna


def Pr(Text, Profile):
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p

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

p1 = {'A':[0.8, 0.0, 0.0, 0.2],'C':[0.0, 0.6, 0.2, 0.0],
      'G':[0.2, 0.2, 0.8, 0.0],'T':[0.0, 0.2, 0.0, 0.8]}
dn1= ['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
print(Motifs(p1,dn1))
