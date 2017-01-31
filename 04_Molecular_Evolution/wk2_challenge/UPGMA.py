__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	n = int(file.readline().strip())
	d = dict()
	for i, lin in enumerate(file):
		for j, value in enumerate(lin.strip().split(' ')):
			if i!= j:
				d[(i, j)] = float(value)


class Node(object):
    def __init__(self, index, leaf, left=None, right=None, age=0):
        self.index = index
        self.leaf = leaf
        if leaf:
            self.age = 0
            self.elements = 1
        if not leaf:
            self.left = left
            self.right = right
            self.age = age
            self.elements = left.elements+right.elements


def initialize(nn):
    t = list()
    for i in range(nn):
        t.append(Node(i, True))
    return t


def reduce_tree():
    global tree, int_node, d
    a, b = min(d, key=d.get)
    for node in tree:
        if node.index == a:
            node_a = node
        elif node.index == b:
            node_b = node
    tree.remove(node_a)
    tree.remove(node_b)
    new_node = Node(int_node, False, node_a, node_b, d[a, b]/2)
    tree.append(new_node)
    el_a = node_a.elements
    el_b = node_b.elements
    for node in tree:
        ind = node.index
        if ind != int_node:
            d[int_node, ind] = (d[a, ind]*el_a + d[b, ind]*el_b)/(el_a+el_b)
            d[ind, int_node] = (d[a, ind]*el_a + d[b, ind]*el_b)/(el_a+el_b)
    for key, value in list(d.items()):
        i, j = key
        if i == a or i == b or j == a or j == b:
            del d[key]
    int_node += 1
    return None


def tree_printer(node, conn):
    if node.leaf:
        return None
    else:
        node_a = node.left
        node_b = node.right
        g.write(str(node.index)+'->'+str(node_a.index)+':'+'{0:.3f}'.format(node.age-node_a.age)+'\n')
        g.write(str(node.index)+'->'+str(node_b.index)+':'+'{0:.3f}'.format(node.age-node_b.age)+'\n')
        g.write(str(node_a.index)+'->'+str(node.index)+':'+'{0:.3f}'.format(node.age-node_a.age)+'\n')
        g.write(str(node_b.index)+'->'+str(node.index)+':'+'{0:.3f}'.format(node.age-node_b.age)+'\n')
        if not node_a.leaf:
            tree_printer(node_a, conn)
        if not node_b.leaf:
            tree_printer(node_b, conn)
    return None

if __name__ == '__main__':
	int_node = n
	tree = initialize(n)
	while len(tree) > 1:
		reduce_tree()
	with open('ultra_tree_out.txt', 'w') as g:
		tree_printer(tree[0], g)
