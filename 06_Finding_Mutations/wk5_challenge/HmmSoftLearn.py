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
    return final, tre


def reverse_viterbi(emit, stat, t, e):
    tre = list()
    n = len(emit)
    d = dict()
    for item in stat:
        d[item] = 1
    tre.append(d)
    for ind in range(n-1, 0, -1):
        d = dict()
        for item in stat:
            proba = [e[last][emit[ind]] * t[item][last] * tre[-1][last] for last in stat]
            d[item] = sum(proba)
        tre.append(d)
    proba = [e[last][emit[0]] * tre[n-1][last] / len(last) for last in states]
    final = sum(proba)
    ttre = tre[::-1]
    return final, ttre


if __name__ == '__main__':
    with open('dataset_11632_12.txt', 'r') as f:
        emitted, possibles, states, transit, emission = interpreter(f)
    proba_tot, forward = viterbi(emitted, states, transit, emission)
    proba_tot2, backward = reverse_viterbi(emitted, states, transit, emission)
    proba_matrix = list()
    for i in range(len(emitted)):
        d = {stat: forward[i][stat] * backward[i][stat] / proba_tot for stat in states}
        proba_matrix.append(d)
    with open('soft_learn.txt', 'w') as g:
        g.write('\t'.join(states) + '\n')
        for dd in proba_matrix:
            g.write('\t'.join(['{0:.4f}'.format(dd[stat]) for stat in states]) + '\n')