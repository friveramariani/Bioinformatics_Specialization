__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def interpreter(conn):
    temitted = conn.readline().strip()
    conn.readline()
    tpossibles = conn.readline().strip().split()
    conn.readline()
    tpath = conn.readline().strip()
    conn.readline()
    thidden = conn.readline().strip().split()
    conn.readline()
    return temitted, tpossibles, tpath, thidden


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


if __name__ == '__main__':
    with open('dataset_11632_8.txt', 'r') as f:
        emitted, possibles, path, hidden = interpreter(f)
    transition, emission = param(emitted, path, hidden, possibles)
    with open('parameter.txt', 'w') as g:
        write_matrix(hidden, transition, g)
        g.write('--------'+'\n')
        write_matrix(possibles, emission, g)