__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Sample Imput:
#   CGATATATCCATAG

# Sample Output:
# {0: 1, 1: 1, 2: 3, 3: 2, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 3, 11: 1}




from PatternCount import PatternCount

def CountDict(Text, k):
    '''
    :param Text: string of DNA
    :param k: length of sub-string from DNA, Integer.
    :return:  A dictionary, key refers the all the starting positions of sub string
    and values return how many times that sub-string appearns in DNA.
    '''
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[Pattern] = PatternCount(Pattern, Text)   # Counting pattern in text
    return Count


k = 3

text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
print(CountDict(text,k))
