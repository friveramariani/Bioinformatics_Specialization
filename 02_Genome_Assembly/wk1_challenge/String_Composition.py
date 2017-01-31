__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


'''
CODE CHALLENGE: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
Sample Input:
5
CAATCCAAC
Sample Output:
CAATC
AATCC
ATCCA
TCCAA
CCAAC
'''

k = 5
text = 'CAATCCAAC'
print (*(sorted([text[i:i+k] for i in range(len(text) - k + 1)])), sep = '\n')