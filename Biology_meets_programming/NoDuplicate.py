__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    #return FrequentPatterns
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates
    #return FrequentPatternsNoDupulicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    ItemsNoDuplicates = list(set(Items)) # output variable
    # your code here
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(Text, k):
    Count = {} # output variable
    #Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    # your code here
    #count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
    #return count


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
k = 4
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
print(FrequentWords(text,k))
