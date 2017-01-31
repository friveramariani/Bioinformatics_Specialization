__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

from itertools import product
import sys


def eulerian_cycle(edge_dict):
    current_node = edge_dict.keys()[0]
    path = [current_node]
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break
    while len(edge_dict) > 0:
        for i in xrange(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path

def universal_string(k):
	universal_dict = {}
	for kmer in [''.join(item) for item in product('01', repeat=k)]:
		if kmer[:-1] in universal_dict:
			universal_dict[kmer[:-1]].append(kmer[1:])
		else:
			universal_dict[kmer[:-1]] = [kmer[1:]]
	path = eulerian_cycle(universal_dict):
    print path

if __name__ == '__main__':
	k = sys.argv[1]
	universal_string(k)
