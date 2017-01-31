__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# To rescale a collection of probabilities (the sides of the die) so that these probabilities sum
# to 1, we will write a function called Normalize(Probabilities). This function takes a
# dictionary Probabilities whose keys are k-mers and whose values are the probabilities of
# these k-mers (which do not necessarily sum to 1). The function should divide each value in
# Probabilities by the sum of all values in  Probabilities, then return the resulting dictionary


# Sample Input:
# {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
# Sample Output:
# {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}

def Normalize(P):

    D = {}
    for k,v in P.items():
        D[k] = P[k]/sum(P.values())
    return D

d = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
print(Normalize(d))