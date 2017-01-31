__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions += [i]

    return positions


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        #print('i is: ',  str(i))
        #print("ExtendedGenome at i is: " + str(ExtendedGenome[i:i+(n//2)]))
        array[i] = PatternCount(symbol, ExtendedGenome[i:i + (n // 2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def Skew(Genome):
    Skew = {}
    Skew[0] = 0
    for i in range(0,len(Genome)):
        if Genome[i] == 'G':
            Skew[i+1] = (Skew[(i+1) -1] + 1)
        elif Genome[i] == 'C':
            Skew[i+1] = (Skew[(i+1) -1] - 1)
        else:
            Skew[i+1] = (Skew[(i+1) -1])


    return Skew

def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    D = Skew(Genome)
    min_value = min(D.values())
    v = [x for x in D.values()]
    positions += [i for i,x in enumerate(v) if x == min_value]
    #print(v)
    return positions

def HammingDistance(s1, s2):
    # your code here
    dif = 0
    for i,ii in zip(s1,s2):
        if i != ii:
            dif += 1

    return dif

def ApproximatePatternMatching(P,T,D):
    #dif = 0
    POS = []
    for i in range(0,(len(T)-len(P))+1):
        dif = 0
        for ii,ii2 in  zip(T[i:(len(P)+i)],P):

            if ii != ii2:
                dif += 1
        if dif <= D:
            POS += [i]
    return POS


def ApproximatePatternCount(Pattern, Text, d):

    count = 0
    for i in range(0,(len(Text)-len(Pattern))+1):
        dif = 0
        for ii,ii2 in  zip(Text[i:(len(Pattern)+i)],Pattern):
             if ii != ii2:
                dif += 1
        if dif <= d:
            count += 1
    return count

str1 = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
str2 = 'GATACACTTCCCGAGTAGGTACTG'
print(MinimumSkew(str2))
