__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# Credits: Course's default codes.

#  Sample Input:
#   AAAAGGGG
#   A
#  Sample Output:
#  {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}


from PatternCount import PatternCount
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i + (n // 2)])
    return array
