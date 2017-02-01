__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import os
from collections import defaultdict

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
    return nl


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

if __name__ == '__main__':
    with open('dataset_10335_12.txt', 'r') as f:
        nodelist = interpreter(f)
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
    with open('parsimony_fromunrooted_out.txt', 'w') as g:
        g.write(str(running_sum)+'\n')
        tree_printer(nodelist[last_node], g)