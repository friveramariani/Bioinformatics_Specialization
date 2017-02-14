__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child, acid):
        self.children[child] = acid


def interpreter(conn):
    tspec = conn.readline().strip().split(' ')
    tspecint = [int(x) for x in tspec]
    tspecint.insert(0, 0)
    return tspecint


def graph_build(spec, conn):
    graph = {i: Node(i) for i in spec}
    for i in spec:
        for j in spec:
            if i < j:
                diff = j-i
                if diff in mass_to_amino:
                    conn.write(str(i)+'->'+str(j)+':'+mass_to_amino[diff]+'\n')
                    graph[i].add_child(j, mass_to_amino[diff])
    return graph


def mass(seq):
    m = 0
    for lett in seq:
        m += amino_to_mass[lett]
    return m

def ideal_spec(seq):
    spec = list()
    spec.append(0)
    spec.append(mass(seq))
    for i in range(1, len(seq)):
        spec.append(mass(seq[:i]))
        spec.append(mass(seq[i:]))
    spec = list(set(spec))
    spec.sort()
    return spec

if __name__ == '__main__':
    
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

    with open('dataset_11813_4 (2).txt', 'r') as f:
        spectrum = interpreter(f)
        final = max(spectrum)

    with open('file_out.txt', 'w') as g:
        spec_graph = graph_build(spectrum, g)

    possibles = [(spec_graph[0], '')]
    out_pep = []
    while possibles:
        curr = possibles.pop()
        if not curr[0].children:
            if curr[0].value == final:
                out_pep.append(curr[1])
        else:
            for child, acid in curr[0].children.items():
                possibles.append((spec_graph[child], curr[1]+acid))

    for item in out_pep:
        spec_out = ideal_spec(item)
        if spec_out == spectrum:
            print(item)