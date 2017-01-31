__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Our goal now is to modify our previous algorithm for the Frequent Words Problem in order to find
# DnaA boxes by identifying frequent k-mers, possibly with mismatches. Given input strings Text and
#  Pattern as well as an integer d, we extend the definition of PatternCount to the function
# ApproximatePatternCount(Pattern, Text, d). This function computes the number of occurrences of
# Pattern in Text with at most d mismatches. For example:

# Sample Input:
# GAGG
# TTTAGAGCCTTCAGAGG

# Sample Output:
# 2

def ApproximatePatternCount(Pattern, Text, d):

    POS = 0
    for i in range(0,(len(Text)-len(Pattern))+1):
        dif = 0
        for ii,ii2 in  zip(Text[i:(len(Pattern)+i)],Pattern):

            if ii != ii2:
                dif += 1
        if dif <= d:
            POS += 1

    return POS