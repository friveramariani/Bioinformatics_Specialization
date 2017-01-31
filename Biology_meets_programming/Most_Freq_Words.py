__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Credit: Most codes provided by course.
# Sample Input:
#      ACGTTGCATGTCGCATGATGCATGAGAGCT
#      4

# Sample Ouput:
#   GCAT CATG GCAT CATG GCAT CATG


def FrequentWords(Text, k):
    FrequentPatterns = []

    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())   # Count the maximum value from CountDict's values
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns


def CountDict(Text, k):
    Count = {}

    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)

    return Count


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
