__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open("dataset_301_7.txt") as file:
    data = []
    for line in file:
        data.append(line[:-1])

bwt = data[0]
patterns = map(str,data[1].split())

def get_pattern_count_beter_bw(bwt, patterns):
    symbols = set(bwt)
    current_count = {ch:0 for ch in symbols}
    count = {0:{ch:current_count[ch] for ch in symbols}}
    for i in range(len(bwt)):
        current_count[bwt[i]] += 1
        count[i+1] = {ch:current_count[ch] for ch in symbols}
    sorted_bwt = sorted(bwt)
    first_occurrence = {ch:sorted_bwt.index(ch) for ch in set(bwt)}

    return [better_bw_matching(bwt, first_occurrence, count, pattern) for pattern in patterns]


def better_bw_matching(bwt, first_occurrence, count, pattern):
    top, bottom = 0, len(bwt) - 1
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom+1]:
                top = first_occurrence[symbol] + count[top][symbol]
                bottom = first_occurrence[symbol] + count[bottom+1][symbol] - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == '__main__':
    pattern_count = map(str, get_pattern_count_beter_bw(bwt, patterns))
    print (' '.join(pattern_count))
    with open('better_bw_matching_out.txt', 'w') as output_data:
        output_data.write(' '.join(pattern_count))