__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import sys
from math import log10
from operator import itemgetter

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
                dd[s] = log10(float(ll[i+1]))
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
                dd[s] = log10(float(ll[i+1]))
            emission[ll[0]] = dd
    return emitted, possibles, states, transit, emission


def viterbi(emit, stat, t, e):
    tre = list()
    n = len(emit)
    d = dict()
    for item in stat:
        d[item] = (e[item][emit[0]] - log10(len(stat)), 'so')
    tre.append(d)
    for ind in range(1,n):
        d = dict()
        for item in stat:
            proba = [(e[item][emit[ind]] + t[last][item] + tre[ind-1][last][0], last) for last in stat]
            d[item] = max(proba, key=itemgetter(0))
        tre.append(d)
    d = dict()
    proba = [(tre[n-1][last][0], last) for last in states]
    d['sink'] = max(proba, key=itemgetter(0))
    tre.append(d)
    return tre


def backtracker(tre):
    s = ''
    curr = 'sink'
    for i in range(len(tre)-1, 0, -1):
        last = tre[i][curr][1]
        s += last
        curr = last
    return s[::-1]

if __name__ == '__main__':
    with open("dataset_11594_6.txt") as f:
        emitted, possibles, states, transit, emission = interpreter(f)
    tree = viterbi(emitted, states, transit, emission)
    out = backtracker(tree)
    print(out)