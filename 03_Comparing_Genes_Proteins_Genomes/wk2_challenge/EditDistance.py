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


def edit_distance(s1,s2):
	n = len(s1)
	m = len(s2)
	dp = np.zeros((n+1,m+1),dtype = int)
	for i in range(1,n+1):
		dp[i][0] = i
	for j in range(1,m+1):
		dp[0][j] = j
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

	return dp[n][m]


if __name__ == '__main__':
	print edit_distance(seq1,seq2)
