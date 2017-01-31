__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

file = sys.argv[1]

def make_edges(seqs):
	edges = []
	for read in seqs:
		edges.append(read[:-1]+ ' -> ' +read[1:])
	return edges

def reconstruct_string(edges):
	string_dict = {line.strip().split(' -> ')[0]:line.strip().split(' -> ')[1] for line in edges}
	head = filter(lambda x: x not in string_dict.values(), string_dict.keys())[0]
	tail = filter(lambda x: x not in string_dict.keys(), string_dict.values())[0]
	reconstructed_str = head[0]
	current_str = head
	while current_str != tail:
		current_str = string_dict[current_str]
		reconstructed_str += current_str[0]
	reconstructed_str += tail[1:]

	return reconstructed_str


if __name__ == '__main__':
	data = []
	with open(file) as input_data:
		for line in input_data:
			data.append(line[:-1])
	k = int(data[0])
	reads = data[1:]
	edges = make_edges(reads)
	ans = reconstruct_string(edges)
	print ans
