__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


from operator import itemgetter


def interpreter(conn):
    it = int(conn.readline().strip())
    conn.readline()
    temitted = conn.readline().strip()
    conn.readline()
    tpossibles = conn.readline().strip().split()
    conn.readline()
    thidden = conn.readline().strip().split()
    conn.readline()
    transit = list()
    while True:
        l = conn.readline()
        if l == '' or l[0:2] == '--':
            break
        ll = l.strip().split('\t')
        if len(ll) == len(thidden)+1:
            dd = [float(ll[i+1]) for i in range(len(thidden))]
            transit.append(dd)
    temission = list()
    while True:
        l = conn.readline()
        if l == '' or l[0:2] == '--':
            break
        ll = l.strip().split('\t')
        if len(ll) == len(tpossibles)+1:
            dd = [float(ll[i+1]) for i in range(len(tpossibles))]
            temission.append(dd)
    return it, temitted, tpossibles, thidden, transit, temission


def normalize(matrix):
    for i, line in enumerate(matrix):
        s = sum(line)
        if s > 0:
            normalized = [x/s for x in line]
            matrix[i] = normalized
        if s == 0:
            l = len(line)
            matrix[i] = [1.0/l for _ in range(l)]
    return matrix


def param(emitt, tpath, hid, poss):
    trans_mat = [[0.0 for i in range(len(hid))] for j in range(len(hid))]
    emit_mat = [[0.0 for i in range(len(poss))] for j in range(len(hid))]
    for i, letter in enumerate(emitt):
        emit_mat[hid.index(tpath[i])][poss.index(letter)] += 1
        if i > 0:
            trans_mat[hid.index(tpath[i-1])][hid.index(tpath[i])] += 1
    trans = normalize(trans_mat)
    emit = normalize(emit_mat)
    return trans, emit


def write_matrix(first, matrix, conn):
    conn.write('\t'+'\t'.join(first)+'\n')
    for i, line in enumerate(matrix):
        s = sum(line)
        if s > 0:
            normalized = map(lambda x: x/s, line)
            line = normalized
        stringed = map(lambda x: '{0:.3f}'.format(x), line)
        conn.write(hidden[i]+'\t'+'\t'.join(stringed)+'\n')
    return None


def viterbi(emit, stat, p, t, e):
    tre = list()
    n = len(emit)
    d = dict()
    for index, item in enumerate(stat):
        d[item] = (e[index][p.index(emit[0])], 'so')
    tre.append(d)
    for ind in range(1, n):
        d = dict()
        for index, item in enumerate(stat):
            proba = [(e[index][p.index(emit[ind])] * t[last_ind][index] * tre[ind-1][last][0], last) for last_ind, last in enumerate(stat)]
            d[item] = max(proba, key=itemgetter(0))
        tre.append(d)
    d = dict()
    proba = [(tre[n-1][last][0], last) for last in stat]
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
    with open('dataset_11632_10.txt', 'r') as f:
        iterations, emitted, possibles, hidden, transition, emission = interpreter(f)
    for _ in range(iterations):
        new_path = backtracker(viterbi(emitted, hidden, possibles, transition, emission))
        transition, emission = param(emitted, new_path, hidden, possibles)
    with open('viterbi_learn.txt', 'w') as g:
        write_matrix(hidden, transition, g)
        g.write('--------'+'\n')
        write_matrix(possibles, emission, g)