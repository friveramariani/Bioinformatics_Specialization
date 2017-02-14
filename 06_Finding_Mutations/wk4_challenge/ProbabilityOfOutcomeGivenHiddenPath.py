__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def interpreter(conn):
    emitted = conn.readline().strip()
    conn.readline()
    possibles = conn.readline().strip().split(' ')
    conn.readline()
    path = conn.readline().strip()
    conn.readline()
    states = conn.readline().strip().split(' ')
    conn.readline()
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
    return emitted, possibles, path, states, emission

if __name__ == '__main__':
    with open('dataset_11594_4.txt', 'r') as f:
        emitted, possibles, path, states, emission = interpreter(f)
    p = 1
    for index, letter in enumerate(emitted):
        p *= emission[path[index]][letter]
    print(p)