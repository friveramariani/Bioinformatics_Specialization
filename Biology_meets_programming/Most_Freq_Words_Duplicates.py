__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

# This problem wants us to remove all duplicates from MostFrequentWords ouptut:

# Sample Input:
#      ACGTTGCATGTCGCATGATGCATGAGAGCT

#      4

# Sample Output:
#    CATG GCAT

from MostFrequentWord import FrequentWords

without_duplicate = list(set(FrequentWords(Text,k)))  # set function removes all duplicates.