__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# Code Credit: Course's Default.

# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# {'A': [1, 2, 1, 0, 0, 2], 'C': [2, 1, 4, 2, 0, 0], 'G': [1, 1, 0, 2, 1, 1], 'T': [1, 1, 0, 1, 4, 2]}




def count(Motifs):

    count_dict = {}
    for i in 'ACGT':
        count_dict[i] = []
        for ii in range(len(Motifs[0])):
            count_dict[i].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count_dict[symbol][j] += 1

    return count_dict
