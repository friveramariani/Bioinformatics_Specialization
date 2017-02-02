__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


from collections import defaultdict, Counter
import os

C = 100


def sort_bucket(string, bucket, order):
    """sort_bucket
    Subfonction of ManberMyers, used for suffix array generation"""
    d = defaultdict(list)
    for i in bucket:
        key = string[i:i+order]
        d[key].append(i)
    result = []
    for k, v in sorted(d.items()):
        if len(v) > 1:
            result += sort_bucket(string, v, order*2)
        else:
            result.append(v[0])
    return result


def suffix_array(string):
    return sort_bucket(string, (i for i in range(len(string))), 1)


def burrows_transform(text):
    """burrows_transform
    Generates the Burrows Wheeler transform of a given text
    Uses the ManberMyers algorithm for suffix array construction"""
    if 'suffix' not in globals():
        suffix = suffix_array(text)
    else:
        global suffix
    bwt = ''
    for i in suffix:
        if i == 0:
            bwt += '$'
        else:
            bwt += text[i-1]
    return bwt


def first_column_index(bwt):
    d = Counter(bwt)
    return {'$': 0, 'A': 1, 'C': d['A']+1, 'G': d['A']+d['C']+1, 'T': d['A']+d['C']+d['G']+1}


def starter(fci):
    return {'A': (1, fci['C']-1), 'C': (fci['C'], fci['G']-1), 'G': (fci['G'], fci['T']-1), 'T': (fci['T'], n-1)}


def checkpoint_array(bwt):
    """checkpoint_array
    Generates a checkpoint array of the BWT
    Initially generates an array every 100bp, can be modified for memory/speed balance (global variable C)"""
    k = n//C
    ch = list()
    ch.append({'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0})
    for i in range(k):
        temp_d = ch[i]
        new_d = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(i*C, (i+1)*C):
            char = bwt[j]
            new_d[char] += 1
        for key, value in list(temp_d.items()):
            new_d[key] += value
        ch.append(new_d)
    return ch


def np(char, pos):
    a = pos//C
    index = check[a][char]
    for i in range(C*a, pos):
        if BWT[i] == char:
            index += 1
    return index+FC[char]


def matcher(char, st, end):
    news = -1
    newe = -1
    match = False
    for i in range(st, end+1):
        if BWT[i] == char:
            if not match:
                match = True
                news = i
            newe = i
    if not match:
        return False
    newsf = np(char, news)
    newef = np(char, newe)
    return newsf, newef


def patt_matcher(patt):
    global output
    red, lett = patt[:-1], patt[-1]
    s, e = start[lett]
    for letter in reversed(red):
        temp = matcher(letter, s, e)
        if not temp:
            return False
        else:
            s = temp[0]
            e = temp[1]
    for t in range(s, e+1):
        output.append(suffix[t])
    return True


if __name__ == '__main__':
    with open('dataset_303_4.txt', 'r') as f:
        genome = f.readline().strip()+'$'
        patterns = list()
        for item in f.readlines():
            patterns.append(item.strip())
    # Definition of global variables used during alignment
    n = len(genome)
    suffix = suffix_array(genome)
    BWT = burrows_transform(genome)
    FC = first_column_index(BWT)
    start = starter(FC)
    check = checkpoint_array(BWT)
    output = list()
    # Alignment itself
    for pattern in patterns:
        patt_matcher(pattern)
    final = sorted(output)
    print(final)
    with open('align_out.txt', 'w') as g:
        for num in final:
            g.write(str(num)+' ')