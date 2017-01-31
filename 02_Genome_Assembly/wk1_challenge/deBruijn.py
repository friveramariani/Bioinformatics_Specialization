__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

def composition(seq,num):
	reads = []
	for i in range(len(seq) - num + 1):
		reads.append(seq[i:i+num])
	return reads

def suffix(t):
	return t[1:]

def prefix(t):
	return t[:-1]

def deBruijn(reads):
	de_bruijn_dict = dict()
	for kmer in sorted(reads):
		if kmer[:-1] in de_bruijn_dict:
			de_bruijn_dict[kmer[:-1]].add(kmer[1:])
		else:
			de_bruijn_dict[kmer[:-1]] = {kmer[1:]}
	de_buijn = [' -> '.join([item[0], ','.join(item[1])]) for item in sorted(de_bruijn_dict.items())]
	return de_buijn


def main():
	file_name = sys.argv[1]
	with open(file_name) as file:
		k = int(file.readline())
		sequence = file.readline()[:-1]

	seqs = composition(sequence,k)
	ans = deBruijn(seqs)
	print '\n'.join(ans)
	
if __name__ == '__main__':
	main()
