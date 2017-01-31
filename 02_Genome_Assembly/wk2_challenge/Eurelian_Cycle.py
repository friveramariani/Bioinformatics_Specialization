__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

file = sys.argv[1]

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

if __name__ == '__main__':
    with open(file) as input_data:
        edges = {}
        for edge in [line.strip().split(' -> ') for line in input_data.readlines()]:
            if ',' in edge[1]:
                edges[int(edge[0])] = map(int,edge[1].split(','))
            else:
                edges[int(edge[0])] = [int(edge[1])]
    #print edges
    path = eulerian_cycle(edges)
    print '->'.join(map(str,path))
    with open('ans.txt', 'w') as output_data:
        output_data.write('->'.join(map(str,path)))
