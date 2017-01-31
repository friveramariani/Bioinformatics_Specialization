__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

text = data[0]
strings = data[1:]

def create_trie(strings):
	root = {}
	for string in strings:
		current = root
		for letter in string:
			current = current.setdefault(letter,{})
		current['-$'] = '-$'
	return root

def trie_matcher(text, root):
	n = len(text)
	for i in range(n):
		current = root
		letter = text[i]
		step = 0
		pos = []
		while letter in current:
			current = current[letter]
			if '-$' in current:
				print str(i) + ' '
				g.write(str(i) + ' ')
				#pos.append(i)
				break
			step += 1
			if i + step >= n:
				break
			else:
				letter = text[i + step]
	return pos

if __name__ == '__main__':
	graph = create_trie(strings)
	g = open('ans.txt', 'w')
	trie_matcher(text, graph)
	g.close()