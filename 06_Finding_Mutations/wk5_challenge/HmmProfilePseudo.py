import sys

filename = sys.argv[1]

def interpreter(conn):
    first = conn.readline().strip().split()
    ttresh, tpseudo = float(first[0]), float(first[1])
    conn.readline()
    tstates = conn.readline().strip().split()
    conn.readline()
    talignment = list()
    for line in conn:
        talignment.append(line.strip())
    return ttresh, tpseudo, tstates, talignment


def seeder(ttresh, talign):
    n = len(talign)
    ll = len(talign[0])
    tseed = list()
    for ind in range(ll):
        val = float()
        for seq in talign:
            if seq[ind] != '-':
                val += 1
        tseed.append(val/n > (1 - ttresh))
    return tseed


def states_define(nn):
    hidden_states = ['S0', 'I0']
    for i in range(nn):
        hidden_states.append('M'+str(i+1))
        hidden_states.append('D'+str(i+1))
        hidden_states.append('I'+str(i+1))
    hidden_states.append('E')
    return hidden_states


def align_explore(stat, align, see, hid):
    trans_mat = [[0.0 for i in range(len(hid))] for j in range(len(hid))]
    emit_mat = [[0.0 for i in range(len(stat))] for j in range(len(hid))]
    ll = len(align[0])
    for seq in align:
        curr_hid = 'S0'
        for ind in range(ll):
            if see[ind]:
                if seq[ind] in stat:
                    new_hid = 'M'+str(int(curr_hid[1:])+1)
                    trans_mat[hid.index(curr_hid)][hid.index(new_hid)] += 1
                    emit_mat[hid.index(new_hid)][stat.index(seq[ind])] += 1
                    curr_hid = new_hid
                else:
                    new_hid = 'D'+str(int(curr_hid[1:])+1)
                    trans_mat[hid.index(curr_hid)][hid.index(new_hid)] += 1
                    curr_hid = new_hid
            else:
                if seq[ind] in stat:
                    new_hid = 'I'+str(int(curr_hid[1:]))
                    trans_mat[hid.index(curr_hid)][hid.index(new_hid)] += 1
                    emit_mat[hid.index(new_hid)][stat.index(seq[ind])] += 1
                    curr_hid = new_hid
        new_hid = 'E'
        trans_mat[hid.index(curr_hid)][hid.index(new_hid)] += 1
    return trans_mat, emit_mat


def add_pseudo(hid, inc, trans, emit, pseud):
    for i, line in enumerate(trans):
        s = sum(line)
        if s > 0:
            normalized = [x/s for x in line]
            trans[i] = normalized

    for i, line in enumerate(emit):
        s = sum(line)
        if s > 0:
            normalized = [x/s for x in line]
            emit[i] = normalized

    for index, item in enumerate(hid):
        if item == 'E':
            continue
        if item[0] in ['I', 'M']:
            new = [x+pseud for x in emit[index]]
            emit[index] = new
        s = item[1:]
        if int(s) < inc:
            possible_moves = ['I'+s, 'M'+str(int(s)+1), 'D'+str(int(s)+1)]
            for new_item in possible_moves:
                trans[index][hid.index(new_item)] += pseud
        elif int(s) == inc:
            possible_moves = ['I'+s, 'E']
            for new_item in possible_moves:
                trans[index][hid.index(new_item)] += pseud
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
    with open("dataset_11632_4.txt") as f:
        tresh, pseudo, states, alignment = interpreter(f)
    seed = seeder(tresh, alignment)
    incl = sum(seed)
    hidden = states_define(incl)
    transition, emission = align_explore(states, alignment, seed, hidden)
    transition_n, emission_n = add_pseudo(hidden, incl, transition, emission, pseudo)
    hidden[0] = 'S'
    with open('output_profile_p.txt', 'w') as g:
        write_matrix(hidden, transition, g)
        g.write('--------'+'\n')
        write_matrix(states, emission, g)