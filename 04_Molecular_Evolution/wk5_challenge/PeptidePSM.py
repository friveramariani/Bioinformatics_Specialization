__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def mass(seq):
    m = 0
    for lett in seq:
        m += amino_to_mass[lett]
    return m


def prefix_spec(seq):
    vect = list()
    for i in range(1, len(seq)+2):
        vect.append(mass(seq[:i]))
    return vect


def scorer(seq, spectrum):
    if mass(seq) != len(spectrum)-1:
        return float("-inf")
    else:
        ts = 0
        vector = prefix_spec(seq)
        for pre in vector:
            ts += spectrum[pre]
        return ts


def interpreter(conn):
    tspeclist = list()
    while True:
        tspec = conn.readline().strip().split(' ')
        if len(tspec) == 1:
            tprot = tspec[0]
            break
        tspecint = [int(x) for x in tspec]
        tspecint.insert(0, 0)
        tspeclist.append(tspecint)
    ttresh = int(conn.readline().strip())
    return tspeclist, tprot, ttresh


def pepfinder(spect, proteo, t):
    min_pep_l = int((len(spect)-1) / 186) + 1
    max_pep_l = int((len(spect)-1) / 57)
    best_s = float("-inf")
    best_p = ''

    for ll in range(min_pep_l, max_pep_l+1):
        for index in range(len(proteo)-ll):
            pep = proteo[index:index+ll]
            s = scorer(pep, spect)
            if s > best_s:
                best_s = s
                best_p = pep

    if best_s >= t:
        return best_p
    else:
        return False

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

    with open('dataset_11866_5.txt', 'r') as f:
        speclist, proteome, thresh = interpreter(f)

    out = list()
    for spec in speclist:
        temp = pepfinder(spec, proteome, thresh)
        if temp:
            out.append(temp)
    for pep in out:
        print(pep)
