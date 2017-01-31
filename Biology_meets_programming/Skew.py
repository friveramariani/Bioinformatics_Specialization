__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Every time we encounter a G, Skew[i] is equal to Skew[i-1]+1; every time we encounter a C,
# Skew[i] is equal to Skew[i-1]-1; otherwise, Skew[i] is equal to Skew[i-1].

# Sample Input:
#     CATGGGCATCGGCCATACGCC

# Sample Output:
#     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2


def skew(Genome):
    Skew = {}
    Skew[0] = 0                                 # Initialize the list with first value of zero.
    for i in range(0,len(Genome)):
        if Genome[i] == 'G':
            Skew[i+1] = (Skew[(i+1) -1] + 1)
        elif Genome[i] == 'C':
            Skew[i+1] = (Skew[(i+1) -1] - 1)
        else:
            Skew[i+1] = (Skew[(i+1) -1])


    return Skew
