__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Codes provided by course

# Implementation of pattern count.


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


#Pattern = "CGCG"
#text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"

#print(PatternCount(Pattern,text))
