__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

from CountDic import CountDic

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
print(FrequentWords(text,3))