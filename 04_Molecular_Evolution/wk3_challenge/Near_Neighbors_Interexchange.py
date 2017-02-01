__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import os
from collections import defaultdict
from copy import copy, deepcopy


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


def interpreter(conn):
    edge = conn.readline().strip().split(' ')
    nl = dict()
    for raw_line in conn:
        line = raw_line.strip().split('->')
        a = int(line[0])
        if a not in nl:
            nl[a] = Node(a, False)
        b = int(line[1])
        if b not in nl:
            nl[b] = Node(b, False)
        nl[a].add_node(b)
    return edge, nl


def tree_printer(nodelist, conn):
    for _, node in nodelist.items():
        for child in node.children:
            conn.write(str(node.index)+'->'+str(child)+'\n')
    conn.write('\n')
    return None


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
        new_tree[first_children[1]].remove_node(aa)
        new_tree[first_children[1]].add_node(bb)
        new_tree[second_children[ii]].remove_node(bb)
        new_tree[second_children[ii]].add_node(aa)
        treelist.append(new_tree)
    return treelist


if __name__ == '__main__':
    with open('dataset_10336_6.txt', 'r') as f:
        edge, nodelist = interpreter(f)
    a, b = int(edge[0]), int(edge[1])
    treelist = exchanger(a, b, nodelist)
    with open('neighbour_out.txt', 'w') as g:
        for nodes in treelist:
            tree_printer(nodes, g)