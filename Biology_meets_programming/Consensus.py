# Code Credit: Course's Default

# Sample Input:
# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG
# Sample Output:
# CACCTA

from count import count

def consensus(Motifs):

    k = len(Motifs[0])
    count_mot = count(Motifs)
    consensus_string = ""

    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count_mot[symbol][j] > m:
                m = count_mot[symbol][j]
                frequentSymbol = symbol
        consensus_string += frequentSymbol

    return consensus_string
