__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


from operator import itemgetter
from copy import deepcopy


def interpreter(conn):
    tpep = conn.readline().strip()
    tspec = conn.readline().strip().split(' ')
    tspecint = [int(x) for x in tspec]
    tspecint.insert(0, 0)
    tk = int(conn.readline().strip())
    return tpep, tspecint, tk


def pep_diff_array(seq):
    pep_array = list()
    diff_array = dict()
    running = 0
    pep_array.append(running)
    for lett in seq:
        mas = amino_to_mass[lett]
        running += mas
        pep_array.append(running)
        diff_array[running] = mas
    return pep_array, diff_array


def init_calc(ii, jj):
    if ii != jj:
        return float('-inf')
    else:
        if ii == 0:
            return 0
        elif ii > mass:
            return float('-inf')
        else:
            return spectrum[ii] + first_layer[ii-diff[ii]][jj-diff[jj]][0]


if __name__ == '__main__':
    with open('dataset_11866_14.txt', 'r') as f:
        peptide, spectrum, modif = interpreter(f)
        mass = len(spectrum) - 1

    with open('integer_mass_table.txt') as e:
        mass_to_amino = dict()
        amino_to_mass = dict()
        for item in e:
            temp = item.strip().split(' ')
            try:
                mass_to_amino[int(temp[1])] = temp[0]
                amino_to_mass[temp[0]] = int(temp[1])
            except IndexError:
                pass

    unmod_mass, diff = pep_diff_array(peptide)
    layers = list()
    # First layer corresponding to unmodified peptides, only non -inf score for the matching peptide
    first_layer = dict()
    for i in unmod_mass:
        first_layer[i] = [(init_calc(i, j), 0) for j in range(mass+1)]
    layers.append(first_layer)

    for k in range(1, modif+1):
        layer = dict()
        for i in unmod_mass:
            layer[i] = list()
            if i == 0:
                layer[i] = [(float('-inf'), 0) for j in range(mass+1)]
            else:
                for j in range(mass+1):
                    d = diff[i]
                    pre = list()
                    if j >= d:
                        pre.append((layer[i-d][j-d][0], 0))
                    for jj in range(j):
                        if j-jj != d:
                            pre.append((layers[k-1][i-d][jj][0], j-jj-d))
                    if pre:
                        anc = max(pre, key=itemgetter(0))
                        anc = (anc[0]+spectrum[j], anc[1])
                    else:
                        anc = (float('-inf'), 0)
                    layer[i].append(anc)
        layers.append(deepcopy(layer))

    endpoints = [(layers[i][max(unmod_mass)][mass], i) for i in range(modif+1)]
    max_value = max(endpoints, key=lambda x: x[0][0])
    mod_done = max_value[1]
    node = max_value[0]
    path = list()
    curr_j = mass

    for back in unmod_mass[::-1]:
        if back:
            dist = node[1]
            path.append(dist)
            d = diff[back]
            if dist == 0:
                curr_j -= d
                node = layers[mod_done][back-d][curr_j]
            else:
                curr_j = curr_j - d - dist
                mod_done -= 1
                node = layers[mod_done][back-d][curr_j]

    peptide_modif = ''
    for ind, mod in enumerate(path[::-1]):
        peptide_modif += peptide[ind]
        if mod:
            peptide_modif += '({0:+d})'.format(mod)
    print(peptide_modif)