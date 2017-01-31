__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'



# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'G': [2, 2, 1, 3, 2, 2], 'A': [2, 3, 2, 1, 1, 3], 'C': [3, 2, 5, 3, 1, 1], 'T': [2, 2, 1, 2, 5, 3]}



def CountWithPseudocounts(Motifs):

    count = {}
    for i in 'ACGT':
        count[i] = []
        for ii in range(len(Motifs[0])):
            count[i].append(1)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count
