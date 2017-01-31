__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

def create_trie(strings):
	root = {}
	for string in strings:
		current = root
		for letter in string:
			current = current.setdefault(letter,{})
		current['-$'] = '-$'
	return root

def print_trie(start, node):
	for key, value in node.items():
		global n
		if key == '-$':
			continue
		else:
			n += 1
			print (str(start)+'->'+str(n)+':'+key+'\n')
			#g.write(str(start)+'->'+str(n)+':'+key+'\n')
			print_trie(n, value)

if __name__ == '__main__':
	n = 0
	graph = create_trie(data)
	#g = open('trie_out.txt', 'w')
	print_trie(0, graph)
	#g.close()
