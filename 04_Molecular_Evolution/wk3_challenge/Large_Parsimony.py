__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import os
from collections import defaultdict
from copy import copy, deepcopy

alphabet = ['A', 'C', 'G', 'T', ]


def dist(a, b):
    if a == b:
        return 0
    else:
        return 1


def seq_dist(a, b):
    summ = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            summ += 1
    return summ


def exchanger(aa, bb, tree):
    first_node = tree[aa]
    second_node = tree[bb]
    first_children = copy(first_node.children)
    second_children = copy(second_node.children)
    first_children.remove(bb)
    second_children.remove(aa)
    fixed_node = first_children[0]
    treelist = list()
    for ii in range(2):
        new_node1 = Node(aa, False)
        new_node1.add_node(bb)
        new_node1.add_node(fixed_node)
        new_node1.add_node(second_children[ii])
        new_node2 = Node(bb, False)
        new_node2.add_node(aa)
        new_node2.add_node(first_children[1])
        new_node2.add_node(second_children[(ii+1)%2])
        new_tree = deepcopy(tree)
        new_tree[aa] = new_node1
        new_tree[bb] = new_node2
        if not new_tree[first_children[1]].leaf:
            new_tree[first_children[1]].remove_node(aa)
            new_tree[first_children[1]].add_node(bb)
        if not new_tree[second_children[ii]].leaf:
            new_tree[second_children[ii]].remove_node(bb)
            new_tree[second_children[ii]].add_node(aa)
        treelist.append(new_tree)
    return treelist


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Node(object):
    def __init__(self, index, leaf):
        self.index = index
        self.leaf = leaf
        self.children = []
        self.edges = []
        self.text = ''
        self.score = defaultdict(int)
        self.scored = False

    def reinit(self):
        self.score = defaultdict(int)
        self.scored = False
        return None

    def is_ripe(self):
        if self.leaf:
            return True
        else:
            for item in self.children:
                if not nodelist[item].scored:
                    return False
        return True

    def add_node(self, c_index):
        self.children.append(c_index)
        self.edges.append(0)
        return None

    def remove_node(self, c_index):
        self.children.remove(c_index)
        self.edges.pop()
        return None

    def scoring(self, curr_letter):
        if self.leaf:
            for letter in alphabet:
                if letter == self.text[curr_letter]:
                    self.score[letter] = 0
                else:
                    self.score[letter] = float('inf')
        else:
            for letter in alphabet:
                for item in self.children:
                    self.score[letter] += min([nodelist[item].score[i]+dist(letter, i) for i in alphabet])
        self.scored = True
        return None


def interpreter(conn):
    nn = int(conn.readline().strip())
    nl = dict()
    running = 0
    for raw_line in conn:
        line = raw_line.strip().split('->')
        if is_int(line[0]):
            a = int(line[0])
            if a not in nl:
                nl[a] = Node(a, False)
            if is_int(line[1]):
                b = int(line[1])
                if b not in nl:
                    nl[b] = Node(b, False)
                nl[a].add_node(b)
            else:
                seq = line[1]
                nl[running] = Node(running, True)
                nl[running].text = seq
                nl[a].add_node(running)
                running += 1
    return nn, nl


def tree_scoring(curr_letter):
    for _, node in nodelist.items():
        if node.leaf:
            node.scoring(curr_letter)
    while not nodelist[new_root].scored:
        for _, node in nodelist.items():
            if not node.scored:
                if node.is_ripe():
                    node.scoring(curr_letter)
    return None


def tree_pruning(node, parent_letter=''):
    if node.leaf:
        return None
    mini = float('inf')
    choice = ''
    for letter in alphabet:
        s = node.score[letter]
        if parent_letter != letter:
            s += 1
        if s < mini:
            mini = s
            choice = letter
    node.text += choice
    for i in node.children:
        tree_pruning(nodelist[i], choice)
    return None


def tree_edge_weighter(node):
    global running_sum
    if node.leaf:
        return None
    for index, item in enumerate(node.children):
        dd = seq_dist(node.text, nodelist[item].text)
        running_sum += dd
        node.edges[index] = dd
        tree_edge_weighter(nodelist[item])
    return None


def tree_printer(node, conn):
    if node.leaf:
        return None
    for index, item in enumerate(node.children):
        child = nodelist[item]
        conn.write(node.text+'->'+child.text+':'+str(node.edges[index])+'\n')
        conn.write(child.text+'->'+node.text+':'+str(node.edges[index])+'\n')
        tree_printer(child, conn)
    return None


def tree_rooting(node):
    if node.leaf:
        return None
    ii = node.index
    for child in node.children:
        if ii in nodelist[child].children:
            nodelist[child].remove_node(ii)
        tree_rooting(nodelist[child])


def find_all_edges(tree):
    l = []
    for i, value in tree.items():
        if i >= n_leaves:
            for j in value.children:
                if j >= n_leaves and j > i:
                    l.append((i, j))
    return l

if __name__ == '__main__':
    with open('dataset_10336_8.txt', 'r') as f:
        n_leaves, nodelist = interpreter(f)
    saved_tree = deepcopy(nodelist)
    seq_len = len(nodelist[0].text)
    # Tree rooting process
    new_root = len(nodelist)
    last_node = new_root - 1
    connected_node = max(nodelist[last_node].children)
    nodelist[new_root] = Node(new_root, False)
    nodelist[new_root].add_node(last_node)
    nodelist[new_root].add_node(connected_node)
    nodelist[last_node].remove_node(connected_node)
    nodelist[connected_node].remove_node(last_node)
    tree_rooting(nodelist[new_root])

    # Tree scoring
    for i in range(seq_len):
        tree_scoring(i)
        tree_pruning(nodelist[new_root])
        for _, node in nodelist.items():
            node.reinit()
    running_sum = 0
    tree_edge_weighter(nodelist[new_root])

    # Tree uprooting
    top_edge_weight = sum(nodelist[new_root].edges)
    del nodelist[new_root]
    nodelist[last_node].add_node(connected_node)
    nodelist[last_node].edges[-1] = top_edge_weight
    g = open('large_pars_out1.txt', 'w')
    g.write(str(running_sum)+'\n')
    tree_printer(nodelist[last_node], g)
    g.write('\n')

    current_min = running_sum
    still_working = True

    # Tree exchange
    while still_working:
        still_working = False
        exchanges = find_all_edges(saved_tree)
        for a, b in exchanges:
            treelist = exchanger(a, b, saved_tree)
            for tree in treelist:
                temp_tree = deepcopy(tree)
                nodelist = tree
                new_root = len(nodelist)
                last_node = new_root - 1
                connected_node = max(nodelist[last_node].children)
                nodelist[new_root] = Node(new_root, False)
                nodelist[new_root].add_node(last_node)
                nodelist[new_root].add_node(connected_node)
                nodelist[last_node].remove_node(connected_node)
                nodelist[connected_node].remove_node(last_node)
                tree_rooting(nodelist[new_root])

                # Tree scoring
                for i in range(seq_len):
                    tree_scoring(i)
                    tree_pruning(nodelist[new_root])
                    for _, node in nodelist.items():
                        node.reinit()
                running_sum = 0
                tree_edge_weighter(nodelist[new_root])
                if running_sum < current_min:
                    current_min = running_sum
                    new_saved_tree = temp_tree
                    tree_to_print = deepcopy(nodelist)
                    still_working = True
        if still_working:
            g.write(str(current_min)+'\n')
            tree_printer(tree_to_print[len(tree_to_print)-1], g)
            g.write('\n')
            saved_tree = deepcopy(new_saved_tree)
