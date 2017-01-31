__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


# Reverse complement of a DNA strand:
# Sample Input:
#    AAAACCCGGT

# Sample Output:
#    ACCGGGTTTT


def ReverseCom(seq):
    complement_strand = ''
    D = {'A':'T','T':'A','C':'G','G':'C'}

    for i in seq:
        complement_strand += (D[i])

    return complement_strand[::-1]
