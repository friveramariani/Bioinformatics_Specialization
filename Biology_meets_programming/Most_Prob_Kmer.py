__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
#  Input: A string Text, an integer k, and a 4 x k matrix Profile.
#  Output: A Profile-most probable k-mer in Text.

# Sample Input:

# ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT

# 5

# 0.2 0.2 0.3 0.2 0.3
# 0.4 0.3 0.1 0.5 0.1
# 0.3 0.3 0.5 0.2 0.4
# 0.1 0.2 0.1 0.1 0.2

# Sample Output:

# CCGAG


from Pr import pr

def ProfileMostProbablePattern(dna,pf):

    km = []
    sc = []
    k = len(pf['A'])
    for i in range(0,len(dna)-k+1):
        km += [dna[i:i+k]]
    for i in km:
        sc += [Pr(i,pf)]

    return km[sc.index(max(sc))]
