import os
from collections import defaultdict

alphabet = ['A', 'C', 'G', 'T', ]
__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


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
    nl = [Node(i, True) for i in range(nn)]
    for j, raw_line in enumerate(conn):
        line = raw_line.strip().split('->')
        node_val = int(line[0])
        if node_val == len(nl):
            nl.append(Node(node_val, False))
        if node_val > len(nl):
            print("Unexpected node")
        if j < nn:
            nl[node_val].add_node(j)
            nl[j].text = line[1]
        if j >= nn:
            nl[node_val].add_node(int(line[1]))
    return nl


def tree_scoring(curr_letter):
    for node in nodelist:
        if node.leaf:
            node.scoring(curr_letter)
    while not nodelist[-1].scored:
        for node in nodelist:
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


if __name__ == '__main__':
    with open('dataset_10335_10.txt', 'r') as f:
        nodelist = interpreter(f)
    seq_len = len(nodelist[0].text)
    for i in range(seq_len):
        tree_scoring(i)
        tree_pruning(nodelist[-1])
        for node in nodelist:
            node.reinit()
    running_sum = 0
    tree_edge_weighter(nodelist[-1])
    with open('parsimony_out.txt', 'w') as g:
        g.write(str(running_sum)+'\n')
        tree_printer(nodelist[-1], g)
