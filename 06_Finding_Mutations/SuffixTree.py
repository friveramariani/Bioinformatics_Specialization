__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	genome = file.readline()

def build_suffix_tree(genome):
	n = len(genome)
	root = {}
	for i in range(n-1, -1, -1):
		current = root
		for j in range(i, n):
			if genome[j] in current:
				current = current[genome[j]]
			elif '_e' in current:
				update_edges(j, current)
				break
			else:
				current.setdefault('_e', list()).append(j)
				break
	return root

def update_edges(index, node):
	letter = genome[index]
	for i in node['_e']:
		if genome[i] == letter:
			node['_e'].remove(i)
			if not node['_e']:
				del node['_e']
			node[letter] = {'_e': [i+1]}
			update_edges(index+1, node[letter])
			return None
	node['_e'].append(index)
	return None

def edge_len(node):
    l = 0
    for key, value in node.items():
        if key == '_e':
            l += len(node['_e'])
        else:
            l += 1
    return l

def tree_reducer(root_node):
    for key, value in list(root_node.items()):
        if key in ['A', 'C', 'G', 'T', ]:
            if edge_len(value) >= 2:
                tree_reducer(value)
            if edge_len(value) == 1:
                text = key
                current = value
                while edge_len(current) == 1 and '_e' not in current.keys():
                    current = list(current.values())[0]
                    text += list(current.keys())[0]
                del root_node[key]
                root_node[text] = current
                tree_reducer(current)
    return None

def tree_printer(root_node, conn):
    for key, value in root_node.items():
        if key == '_e':
            for index in value:
                conn.write(genome[index:])
        else:
            conn.write(key+'\n')
            tree_printer(value, conn)
    return None

if __name__ == '__main__':
	suffix_tree = build_suffix_tree(genome)
	with open('suffix_out.txt', 'w') as g:
		tree_printer(suffix_tree, g)
	g.close()