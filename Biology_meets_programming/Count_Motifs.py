__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

def count(Motifs):

    count_dict = {}

    for i in 'ACGT':
        count_dict[i] = []
        for ii in range(len(Motifs[0])):
            count_dict[i].append(1)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            symbol = Motifs[i][j]
            count_dict[symbol][j] += 1

    for symbol in count_dict:
        for kk in range(0,len(count_dict[symbol])):
            count_dict[symbol][kk] = count_dict[symbol][kk]/(2*len(Motifs)-1)

    return count_dict
