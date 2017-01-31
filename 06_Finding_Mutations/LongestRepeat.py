__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
    genome = file.readline()

current_max = 0
current_text = ''

def suffix_tree_builder(genome):
    n = len(genome)
    root = dict()
    for i in range(n-1, -1, -1):
        current = root
        for j in range(i,n):
            if genome[j] in current:
                current = current[genome[j]]
            elif '_e' in current:
                update_edges(j,current)
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

def repeat_finder(node, index, text):
    stop = True
    for key, value in node.items():
        if key in ['A', 'C', 'G', 'T']:
            repeat_finder(value, index+1, text+key)
            stop = False
    if stop:
        global current_max
        global current_text
        if index > current_max:
            current_max = index
            current_text = text
    return None


if __name__ == '__main__':
    genome += '$'
    suffix_tree = suffix_tree_builder(genome)
    repeat_finder(suffix_tree, 0, '')
    print(current_text)
