__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def mass(seq):
    m = 0
    for lett in seq:
        m += amino_to_mass[lett]
    return m


def prefix_spec(seq):
    spec = list()
    spec.append(mass(seq))
    for i in range(1, len(seq)+1):
        spec.append(mass(seq[:i]))
    return spec


def peptide_to_vector(seq):
    ll = prefix_spec(seq)
    vect = list()
    for i in range(max(ll)):
        if i+1 in ll:
            vect.append('1')
        else:
            vect.append('0')
    return vect


def vector_to_peptide(vect):
    run = 0
    pept = ''
    for i in vect:
        run += 1
        if i == '1':
            pept += mass_to_amino[run]
            run = 0
    return pept


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

    with open('dataset_11813_8 (2).txt', 'r') as f:
        vect = f.readline().strip().split(' ')

    print(vector_to_peptide(vect))