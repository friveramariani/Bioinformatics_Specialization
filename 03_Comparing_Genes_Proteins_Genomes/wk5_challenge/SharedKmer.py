__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys
from collections import defaultdict
filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])
k = int(data[0])
p = data[1]
q = data[2]

def rev_comp(sequence):
	rev_comp = ''
	for nucleotide in sequence:
		if nucleotide == 'A':
			rev_comp = rev_comp + 'T'
		elif nucleotide == 'T':
			rev_comp = rev_comp + 'A'
		elif nucleotide == 'G':
			rev_comp = rev_comp + 'C'
		elif nucleotide == 'C':
			rev_comp = rev_comp + 'G'
	rev_comp = rev_comp[::-1]
	return rev_comp

def sharedkmer(dna1,dna2):
	dna1_dict = defaultdict(list)
	for i in xrange(len(dna1) - k + 1):
		dna1_dict[dna1[i:i+k]].append(i)
	shared_kmer_indices = set()
	for j in xrange(len(dna2) - k + 1):
		shared_kmer_indices |= set(map(lambda x: (x,j), dna1_dict[dna2[j:j+k]]))
		shared_kmer_indices |= set(map(lambda x: (x,j), dna1_dict[rev_comp(dna2[j:j+k])]))
	return shared_kmer_indices

if __name__ == '__main__':
	ans = sharedkmer(p,q)
	for res in ans:
		print res
