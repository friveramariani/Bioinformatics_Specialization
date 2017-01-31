__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys
from collections import defaultdict

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

n = int(data[0])

d = []

for line in data[1:]:
	d.append(map(int,line.split(' ')))


def limb_length(index):
    curr_min = float('inf')
    bridge = 0, 0
    for i in range(index):
        for ii in range(i, index):
            curr = d[i][index]+d[index][ii]-d[i][ii]
            curr /= 2
            if curr < curr_min:
                curr_min = curr
                bridge = i, ii
    return int(curr_min), bridge


def path_between(i, j):
    poss_paths = [[(i, 0)]]
    while poss_paths:
        path = poss_paths.pop()
        node = path[-1][0]
        for next_node, dist in final_tree[node]:
            new_path = path[:]
            if next_node == j:
                new_path.append((j, dist))
                return new_path
            elif next_node < n:
                continue
            elif len(new_path) >= 2:
                if next_node != new_path[-2][0]:
                    new_path.append((next_node, dist))
                    poss_paths.append(new_path)
                    continue
            elif len(new_path) == 1:
                new_path.append((next_node, dist))
                poss_paths.append(new_path)
                continue


def adding_branch(index):
    global final_tree
    global int_node
    limb, bridge = limb_length(index)
    i, j = bridge
    path = path_between(i, j)
    distance = d[i][index] - limb
    start_node = i
    for node, dd in path:
        if dd == 0:
            continue
        if distance > dd:
            distance -= dd
            start_node = node
        elif distance == dd:
            final_tree[node].append((index, limb))
            final_tree[index].append((node, limb))
            break
        elif distance < dd:
            new_node = int_node
            int_node += 1
            final_tree[new_node].append((index, limb))
            final_tree[index].append((new_node, limb))
            final_tree[start_node].remove((node, dd))
            final_tree[node].remove((start_node, dd))
            final_tree[start_node].append((new_node, distance))
            final_tree[new_node].append((start_node, distance))
            final_tree[node].append((new_node, dd-distance))
            final_tree[new_node].append((node, dd-distance))
            break
    return None

def tree_printer(tree):
    for key, value in tree.items():
        for next_node, dist in value:
            print(str(key)+'->'+str(next_node)+':'+str(dist)+'\n')
    return None


if __name__=='__main__':
	final_tree = defaultdict(list)
	int_node = n
	final_tree[0].append((1,d[1][0]))
	final_tree[1].append((0,d[1][0]))
	for i in range(2,n):
		adding_branch(i)
    with open('tree_out.txt', 'w') as g:
	tree_printer(final_tree)
