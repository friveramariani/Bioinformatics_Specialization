__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


from math import log10
from copy import copy
from operator import itemgetter


def interpreter(conn):
    tnew_seq = conn.readline().strip()
    conn.readline()
    first = conn.readline().strip().split()
    ttresh, tpseudo = float(first[0]), float(first[1])
    conn.readline()
    tstates = conn.readline().strip().split()
    conn.readline()
    talignment = list()
    for line in conn:
        talignment.append(line.strip())
    return tnew_seq, ttresh, tpseudo, tstates, talignment


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


def normalize(matrix):
    for i, line in enumerate(matrix):
        s = sum(line)
        if s > 0:
            normalized = [x/s for x in line]
            matrix[i] = normalized
    return matrix


def add_pseudo(hid, inc, trans, emit, pseud):
    normalize(trans)
    normalize(emit)
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
    normalize(trans)
    normalize(emit)
    return trans, emit


def generate_viterbi(sequence, inc, hid, tran, emit):
    """Generates the max probability for the given sequence in the Viterbi graph
    The probabities are given as a list of dictionaries, indexed by columns
    Each dictionnary is index by the current state, value is a tuple with :
    the current max probability, the backtracking column and backtracking state
    Needs to be re-written with tran and emit as dictionnaries for clarity!
    """
    viterbi = list()
    column = dict()
    column['S0'] = (0, 0, 'Source')
    column['D1'] = (log10(tran[hid.index('S0')][hid.index('D1')]), 0, 'S0')
    for i in range(1, inc):
        column['D'+str(i+1)] = (log10(tran[hid.index('D'+str(i))][hid.index('D'+str(i+1))]) + column['D'+str(i)][0], 0, 'D'+str(i))
    viterbi.append(copy(column))
    for j, lett in enumerate(sequence):
        column = dict()
        if not j:
            column['I0'] = (log10(tran[hid.index('S0')][hid.index('I0')]) + log10(emit[hid.index('I0')][states.index(lett)]), 0, 'S0')
            column['M1'] = (log10(tran[hid.index('S0')][hid.index('M1')]) + log10(emit[hid.index('M1')][states.index(lett)]), 0, 'S0')
            column['D1'] = (column['I0'][0] + log10(tran[hid.index('I0')][hid.index('D1')]), 1, 'I0')
            for stat in hid[4:-1]:
                l = stat[0]
                ind = int(stat[1:])
                if l == 'I':
                    fath = 'D'+str(ind)
                    column[stat] = (viterbi[j][fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]) + log10(emit[hid.index(stat)][states.index(lett)]), 0, fath)
                if l == 'M':
                    fath = 'D'+str(ind-1)
                    column[stat] = (viterbi[j][fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]) + log10(emit[hid.index(stat)][states.index(lett)]), 0, fath)
                if l == 'D':
                    temp = str(ind-1)
                    fathers = [tt+temp for tt in ['I', 'M', 'D']]
                    proba = [(column[fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]), j+1, fath) for fath in fathers]
                    column[stat] = max(proba, key=itemgetter(0))
            viterbi.append(copy(column))
        else:
            column['I0'] = (viterbi[j]['I0'][0] + log10(tran[hid.index('I0')][hid.index('I0')]) + log10(emit[hid.index('I0')][states.index(lett)]), j, 'I0')
            column['M1'] = (viterbi[j]['I0'][0] + log10(tran[hid.index('I0')][hid.index('M1')]) + log10(emit[hid.index('M1')][states.index(lett)]), j, 'I0')
            column['D1'] = (column['I0'][0] + log10(tran[hid.index('I0')][hid.index('D1')]), 1, 'I0')
            for stat in hid[4:-1]:
                l = stat[0]
                ind = int(stat[1:])
                if l == 'I':
                    temp = str(ind)
                    fathers = [tt+temp for tt in ['I', 'M', 'D']]
                    proba = [(viterbi[j][fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]) + log10(emit[hid.index(stat)][states.index(lett)]), j, fath) for fath in fathers]
                if l == 'M':
                    temp = str(ind-1)
                    fathers = [tt+temp for tt in ['I', 'M', 'D']]
                    proba = [(viterbi[j][fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]) + log10(emit[hid.index(stat)][states.index(lett)]), j, fath) for fath in fathers]
                if l == 'D':
                    temp = str(ind-1)
                    fathers = [tt+temp for tt in ['I', 'M', 'D']]
                    proba = [(column[fath][0] + log10(tran[hid.index(fath)][hid.index(stat)]), j+1, fath) for fath in fathers]
                column[stat] = max(proba, key=itemgetter(0))
            viterbi.append(copy(column))
    return viterbi


if __name__ == '__main__':
    with open('dataset_11632_6.txt', 'r') as f:
        new_seq, tresh, pseudo, states, alignment = interpreter(f)
    seed = seeder(tresh, alignment)
    incl = sum(seed)
    hidden = states_define(incl)
    transition, emission = align_explore(states, alignment, seed, hidden)
    transition_n, emission_n = add_pseudo(hidden, incl, transition, emission, pseudo)
    vit = generate_viterbi(new_seq, incl, hidden, transition_n, emission_n)
    path = list()
    final_states = [tt+str(incl) for tt in ['M', 'D', 'I']]
    proba = [(vit[-1][fath][0] + log10(transition_n[hidden.index(fath)][hidden.index('E')]), len(new_seq), fath) for fath in final_states]
    exit_state = max(proba, key=itemgetter(0))
    pointer = exit_state[1], exit_state[2]
    while True:
        path.append(pointer[1])
        back = vit[pointer[0]][pointer[1]]
        pointer = back[1], back[2]
        if pointer[1] == 'S0':
            break
    with open('hidden_path.txt', 'w') as g:
        g.write(' '.join(path[::-1]))