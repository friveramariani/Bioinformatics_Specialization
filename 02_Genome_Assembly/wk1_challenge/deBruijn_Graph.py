__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

def suffix(t):
	return t[1:]

def prefix(t):
	return t[:-1]

def deBruijn_Graph(reads):
	de_bruijn_dict = dict()
	for kmer in sorted(reads):
		if kmer[:-1] in de_bruijn_dict:
			de_bruijn_dict[kmer[:-1]].add(kmer[1:])
		else:
			de_bruijn_dict[kmer[:-1]] = {kmer[1:]}
	de_bruijn = [' -> '.join([item[0], ','.join(item[1])]) for item in sorted(de_bruijn_dict.items())]
	return de_bruijn

def main():
	file_name = sys.argv[1]
	seqs = []
	with open(file_name) as file:
		for line in file:
			seqs.append(line[:-1])

	ans = deBruijn_Graph(seqs)
	print '\n'.join(ans)

if __name__ == '__main__':
	main()
