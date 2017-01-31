__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'



#  We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if
#  there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern;
#  that is, HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear
#  with slight variations leads to the following generalization of the Pattern Matching Problem.

# Approximate Pattern Matching Problem:  Find all approximate occurrences of a pattern in a string.
# Input: Strings Pattern and Text along with an integer d.
# Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

#  Sample Input:
#  ATTCTGGA
#  CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
#  3
# Sample Output:
# 6 7 26 27

def ApproximatePatternMatching(Pattern, Text, d):

    positions = [] # initializing list of positions
    for i in range(0,(len(Text) - len(Pattern)+1)):
        diff = 0
        for i1,i2 in zip(Text[i:(len(Pattern)+i)],Pattern):
            if i1 != i2:
                diff += 1
        if diff <= d:
            positions += [i]
    return positions