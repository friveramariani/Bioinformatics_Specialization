__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import sys

filename = sys.argv[1]


def interpreter(conn):
    emitted = conn.readline().strip()
    conn.readline()
    possibles = conn.readline().strip().split(' ')
    conn.readline()
    states = conn.readline().strip().split(' ')
    conn.readline()
    transit = dict()
    while True:
        l = conn.readline()
        if l == '' or l[0:2] == '--':
            break
        ll = l.strip().split('\t')
        if len(ll) == len(states)+1:
            dd = dict()
            for i, s in enumerate(states):
                dd[s] = float(ll[i+1])
            transit[ll[0]] = dd
    emission = dict()
    while True:
        l = conn.readline()
        if l == '' or l[0:2] == '--':
            break
        ll = l.strip().split('\t')
        if len(ll) == len(possibles)+1:
            dd = dict()
            for i, s in enumerate(possibles):
                dd[s] = float(ll[i+1])
            emission[ll[0]] = dd
    return emitted, possibles, states, transit, emission


def viterbi(emit, stat, t, e):
    tre = list()
    n = len(emit)
    d = dict()
    for item in stat:
        d[item] = e[item][emit[0]] / len(stat)
    tre.append(d)
    for ind in range(1, n):
        d = dict()
        for item in stat:
            proba = [e[item][emit[ind]] * t[last][item] * tre[ind-1][last] for last in stat]
            d[item] = sum(proba)
        tre.append(d)
    proba = [tre[n-1][last] for last in states]
    final = sum(proba)
    return final


if __name__ == '__main__':
    with open("dataset_11594_8.txt") as f:
        emitted, possibles, states, transit, emission = interpreter(f)
    proba_tot = viterbi(emitted, states, transit, emission)
    print(proba_tot)
