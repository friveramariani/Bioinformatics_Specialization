__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

from compiler.ast import flatten
import sys

filename = sys.argv[1]

with open(filename) as file:
	kmers = [line.strip() for line in file.readlines()]


edges = {}
for kmer in kmers:
	if kmer[:-1] in edges:
		edges[kmer[:-1]].append(kmer[1:])
	else:
		edges[kmer[:-1]] = [kmer[1:]]

balanced, unbalanced = [], []
out_values = reduce(lambda a,b: a+b, edges.values())
for node in set(out_values+edges.keys()):
	out_value = out_values.count(node)
	if node in edges:
		in_value = len(edges[node])
	else:
		in_value = 0
	if in_value == out_value == 1:
		balanced.append(node)
	else:
		unbalanced.append(node)

get_contigs = lambda s, c: flatten([c+e[-1] if e not in balanced else get_contigs(e,c+e[-1]) for e in edges[s]])
contigs = sorted(flatten([get_contigs(start,start) for start in set(unbalanced) & set(edges.keys())]))

print '\n'.join(contigs)
with open('ans.txt', 'w') as output_data:
	output_data.write('\n'.join(contigs))
