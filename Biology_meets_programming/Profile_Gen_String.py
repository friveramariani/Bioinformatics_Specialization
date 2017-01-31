__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# import the random package
import random
from operator import itemgetter
# then, copy Pr, Normalize, and WeightedDie below this line
def WeightedDie(d):
    ran = random.uniform(0, 1)
    #print(ran,d)
    tot = 0
    for k, v in sorted(d.items(),key=itemgetter(1)):
        if tot <= ran < v + tot:
            return k
        tot += v
def Normalize(P):
    D = {}
    for k,v in P.items():
        D[k] = P[k]/sum(P.values())
    return D
def Pr(Text, Profile):
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
