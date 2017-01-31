__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'



# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome

# Sample Input:
#     ATAT
#     GATATATGCATATACTT

# Sample Output:
#  1 3 9



def PatternMatching(Pattern, Genome):

    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions += [i]

    return positions
