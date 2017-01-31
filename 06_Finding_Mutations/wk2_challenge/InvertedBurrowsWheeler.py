__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open("dataset_299_10.txt") as file:
    string = file.readline()
string = string[:-1]


def inverse_burrows_wheeler(bwt):
    enumerated_bwt = enumerate_word(bwt)
    enumerated_sort = enumerate_word(sorted(bwt))
    inverse_dict = {enumerated_bwt[i]:enumerated_sort[i] for i in range(len(bwt))}
    inverse_bwt = ''
    current_char = enumerated_bwt[0]
    for i in range(len(bwt)):
        current_char = inverse_dict[current_char]
        inverse_bwt += current_char[0]
    return inverse_bwt[1:]+inverse_bwt[0]


def enumerate_word(word):
    char_count = {}
    enumerated = []
    for ch in word:
        if ch not in char_count:
            char_count[ch] = 0
        else:
            char_count[ch] += 1
        enumerated.append(ch+str(char_count[ch]))

    return enumerated


if __name__ == '__main__':
    inverse_bwt = inverse_burrows_wheeler(string)
    print (inverse_bwt)