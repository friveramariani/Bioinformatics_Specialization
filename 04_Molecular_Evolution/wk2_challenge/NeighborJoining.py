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
    def __init__(self, index, leaf, left=None, right=None, le=0, re=0):
        self.index = index
        self.leaf = leaf
        if not leaf:
            self.left = left
            self.right = right
            self.le = le
            self.re = re


def initialize(nn):
    t = list()
    for i in range(nn):
        t.append(Node(i, True))
    return t


def find_neighbours(dist, size):
    current_nodes = [item.index for item in tree]
    total_dist = dict()
    for i in current_nodes:
        running_sum = 0
        for key, value in dist.items():
            if key[0] == i:
                running_sum += value
        total_dist[i] = running_sum
    dist_star = dict()
    for key, value in dist.items():
        dist_star[key] = (size - 2)*value - total_dist[key[0]] - total_dist[key[1]]
    neighbours = min(dist_star, key=dist_star.get)
    delta = (total_dist[neighbours[0]] - total_dist[neighbours[1]])/(size - 2)
    return neighbours, delta


def reduce_tree():
    global tree, int_node, d
    neigh, delt = find_neighbours(d, len(tree))
    a, b = neigh
    for node in tree:
        if node.index == a:
            node_a = node
        elif node.index == b:
            node_b = node
    tree.remove(node_a)
    tree.remove(node_b)
    new_node = Node(int_node, False, node_a, node_b, (d[a, b] + delt)/2, (d[a, b] - delt)/2)
    tree.append(new_node)
    for node in tree:
        ind = node.index
        if ind != int_node:
            d[int_node, ind] = 0.5 * (d[a, ind]+d[b, ind]-d[a, b])
            d[ind, int_node] = d[int_node, ind]
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
        conn.write(str(node.index)+'->'+str(node_a.index)+':'+'{0:.3f}'.format(node.le)+'\n')
        conn.write(str(node.index)+'->'+str(node_b.index)+':'+'{0:.3f}'.format(node.re)+'\n')
        conn.write(str(node_a.index)+'->'+str(node.index)+':'+'{0:.3f}'.format(node.le)+'\n')
        conn.write(str(node_b.index)+'->'+str(node.index)+':'+'{0:.3f}'.format(node.re)+'\n')
        if not node_a.leaf:
            tree_printer(node_a, conn)
        if not node_b.leaf:
            tree_printer(node_b, conn)
    return None

if __name__ == '__main__':
    int_node = n
    tree = initialize(n)
    while len(tree) > 2:
        reduce_tree()
    with open('neighbour_out.txt', 'w') as g:
        a = tree[0].index
        b = tree[1].index
        g.write(str(a)+'->'+str(b)+':'+'{0:.3f}'.format(d[a, b])+'\n')
        g.write(str(b)+'->'+str(a)+':'+'{0:.3f}'.format(d[a, b])+'\n')
        tree_printer(tree[0], g)
        tree_printer(tree[1], g)
