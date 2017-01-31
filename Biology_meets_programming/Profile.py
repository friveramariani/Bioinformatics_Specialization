__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'



# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.

# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}




def Profile(Motifs):

    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}

    for i in 'ACGT':
        profile[i] = []
        for ii in range(len(Motifs[0])):
            profile[i].append(0)

    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1

    for symbol in profile:
        for kk in range(0,len(profile[symbol])):
            profile[symbol][kk] = profile[symbol][kk]/len(Motifs)

    return profile