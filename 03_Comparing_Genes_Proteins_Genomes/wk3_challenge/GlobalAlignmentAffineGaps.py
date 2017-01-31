__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

seq1 = data[0]
seq2 = data[1]


aa_no = {'A':0,'C':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,'K':8,'L':9,'M':10,'N':11,'P':12,'Q':13,'R':14,'S':15,'T':16,'V':17,'W':18,'Y':19}

score_BLOSUM = [[4,0,-2,-1,-2,0,-2,-1,-1,-1,-1,-2,-1,-1,-1,1,0,0,-3,-2],
		 		[0,9,-3,-4,-2,-3,-3,-1,-3,-1,-1,-3,-3,-3,-3,-1,-1,-1,-2,-2],
		 		[-2,-3,6,2,-3,-1,-1,-3,-1,-4,-3,1,-1,0,-2,0,-1,-3,-4,-3],
		 		[-1,-4,2,5,-3,-2,0,-3,1,-3,-2,0,-1,2,0,0,-1,-2,-3,-2],
		 		[-2,-2,-3,-3,6,-3,-1,0,-3,0,0,-3,-4,-3,-3,-2,-2,-1,1,3],
		 		[0,-3,-1,-2,-3,6,-2,-4,-2,-4,-3,0,-2,-2,-2,0,-2,-3,-2,-3],
		 		[-2,-3,-1,0,-1,-2,8,-3,-1,-3,-2,1,-2,0,0,-1,-2,-3,-2,2],
		 		[-1,-1,-3,-3,0,-4,-3,4,-3,2,1,-3,-3,-3,-3,-2,-1,3,-3,-1],
		 		[-1,-3,-1,1,-3,-2,-1,-3,5,-2,-1,0,-1,1,2,0,-1,-2,-3,-2],
		 		[-1,-1,-4,-3,0,-4,-3,2,-2,4,2,-3,-3,-2,-2,-2,-1,1,-2,-1],
		 		[-1,-1,-3,-2,0,-3,-2,1,-1,2,5,-2,-2,0,-1,-1,-1,1,-1,-1],
		 		[-2,-3,1,0,-3,0,1,-3,0,-3,-2,6,-2,0,0,1,0,-3,-4,-2],
		 		[-1,-3,-1,-1,-4,-2,-2,-3,-1,-3,-2,-2,7,-1,-2,-1,-1,-2,-4,-3],
		 		[-1,-3,0,2,-3,-2,0,-3,1,-2,0,0,-1,5,1,0,-1,-2,-2,-1],
		 		[-1,-3,-2,0,-3,-2,0,-3,2,-2,-1,0,-2,1,5,-1,-1,-3,-3,-2],
		 		[1,-1,0,0,-2,0,-1,-2,0,-2,-1,1,-1,0,-1,4,1,-2,-3,-2],
		 		[0,-1,-1,-1,-2,-2,-2,-1,-1,-1,-1,0,-1,-1,-1,1,5,0,-2,-2],
		 		[0,-1,-3,-2,-1,-3,-3,3,-2,1,1,-3,-2,-2,-3,-2,0,4,-3,-1],
		 		[-3,-2,-4,-3,1,-2,-2,-3,-3,-2,-1,-4,-4,-2,-3,-3,-2,-3,11,2],
		 		[-2,-2,-3,-2,3,-3,2,-1,-2,-1,-1,-2,-3,-1,-2,-2,-2,-1,2,7]]


def getscore(AA1,AA2):
	return score_BLOSUM[aa_no[AA1]][aa_no[AA2]]

sigma = -11
epsilon = -1

def global_allignment_affine_gaps(s1,s2,sigma,epsilon):
	n = len(s1)
	m = len(s2)

	s = [[[0 for i in xrange(m+1)] for j in range(n+1)] for k in xrange(3)]
	backtrack = [[[0 for i in xrange(m+1)] for j in range(n+1)] for k in xrange(3)]

	for i in range(1,n+1):
		s[0][i][0] = sigma + (i-1)*epsilon
		s[1][i][0] = sigma + (i-1)*epsilon
		s[2][i][0] = 10*sigma

	for j in range(1,m+1):
		s[0][0][j] = 10*sigma
		s[1][0][j] = sigma + (j-1)*epsilon
		s[2][0][j] = sigma + (j-1)*epsilon

	for i in range(1,n+1):
		for j in range(1,m+1):
			low_scores = [s[0][i-1][j] + epsilon,s[1][i-1][j] + sigma]
			s[0][i][j] = max(low_scores)
			backtrack[0][i][j] = low_scores.index(s[0][i][j])
			
			up_scores = [s[2][i][j-1] + epsilon,s[1][i][j-1] + sigma]
			s[2][i][j] = max(up_scores)
			backtrack[2][i][j] = up_scores.index(s[2][i][j])
			
			mid_scores = [s[0][i][j],s[1][i-1][j-1] + getscore(s1[i-1],s2[j-1]),s[2][i][j]]
			s[1][i][j] = max(mid_scores)
			backtrack[1][i][j] = mid_scores.index(s[1][i][j])

	max_scores = [s[0][i][j],s[1][i][j],s[2][i][j]]
	max_score = max(max_scores)
	backtrack_matrix = max_scores.index(max_score)

	insert_indel = lambda word, i: word[:i] + '-' + word[i:]

	s1_allign = s1
	s2_allign = s2

	while i*j != 0:
		if backtrack_matrix == 0:
			if backtrack[0][i][j] == 1:
				backtrack_matrix = 1
			i -= 1
			s2_allign  = insert_indel(s2_allign,j)
		elif backtrack_matrix == 1:
			if backtrack[1][i][j] == 0:
				backtrack_matrix = 0
			elif backtrack[1][i][j] == 2:
				backtrack_matrix = 2
			else:
				i -= 1
				j -= 1
		else:
			if backtrack[2][i][j] == 1:
				backtrack_matrix = 1
			j -= 1
			s1_allign = insert_indel(s1_allign,i)

	for _ in xrange(i):
		s2_allign = insert_indel(s2_allign,0)

	for _ in xrange(j):
		s1_allign = insert_indel(s1_allign,0) 

	return max_score,s1_allign,s2_allign

if __name__ == '__main__':
	ans = global_allignment_affine_gaps(seq1,seq2,sigma,epsilon)
	for res in ans:
		print res
