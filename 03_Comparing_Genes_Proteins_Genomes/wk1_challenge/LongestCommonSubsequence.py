__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys
import numpy as np

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

seq1 = data[0]
seq2 = data[1]

def lcsbacktrack(v,w):
	n = len(v)
	m = len(w)
	s = np.zeros((n+1,m+1),dtype=int)
	backtrack = []
	#notation for backtrack
	#'v' for vertical
	#'d' for diagonal
	#'h' for horizontal
	for i in range(n):
		temp = []
		for j in range(m):
			if v[i] == w[j]:
				s[i+1][j+1] = s[i][j] + 1
			else:
				s[i+1][j+1] = max(s[i][j+1],s[i+1][j])
			if s[i+1][j+1] == s[i][j] + 1 and v[i] == w[j]:
				temp.append('d')
			elif s[i+1][j+1] == s[i+1][j]:
				temp.append('v')
			elif s[i+1][j+1] == s[i][j+1]:
				temp.append('h')
		backtrack.append(temp)
	
	longest_sseq = ''
	i,j = len(v), len(w)
	while i*j != 0:
		if s[i][j] == s[i-1][j]:
			i -= 1
		elif s[i][j] == s[i][j-1]:
			j -= 1
		else:
			longest_sseq = v[i-1] + longest_sseq
			i -= 1
			j -= 1
	return longest_sseq



if __name__ == '__main__':
	print lcsbacktrack(seq1,seq2)
