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

indel = -5

def global_allignment(s1,s2,indel_penalty):
	n = len(s1)
	m = len(s2)
	s = [[0 for repeat_j in xrange(len(s2)+1)] for repeat_i in xrange(len(s1)+1)]
	backtrack = [['0' for repeat_j in xrange(len(s2)+1)] for repeat_i in xrange(len(s1)+1)]
	for i in xrange(1,n+1):
		s[i][0] = s[i-1][0] + indel_penalty
		backtrack[i][0] = 'U'
	for j in xrange(1,m+1):
		s[0][j] = s[0][j-1] + indel_penalty
		backtrack[0][j] = 'L'
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			up_score = s[i-1][j] + indel_penalty
			left_score = s[i][j-1] + indel_penalty
			diag_score = s[i-1][j-1] + getscore(s1[i-1],s2[j-1])
			s[i][j] = max(left_score,up_score,diag_score)
			if diag_score >= up_score:
				if diag_score >= left_score:
					backtrack[i][j] = 'D'
				elif diag_score < left_score:
					backtrack[i][j] = 'L'
			elif diag_score < up_score:
				if up_score >= left_score:
					backtrack[i][j] = 'U'
				else:
					backtrack[i][j] = 'L'

	return s[n][m],backtrack

def backtrack_allignment(seq1,seq2,indel):
	backtrack = global_allignment(seq1,seq2,indel)[1]
	insert_indel = lambda word, i: word[:i] + '-' + word[i:]
	seq1_aligned, seq2_aligned = seq1, seq2
	i, j = len(seq1), len(seq2)
	while 1:
		if backtrack[i][j] == '0':
			break
		if backtrack[i][j] == 'U':
			i -= 1
			seq2_aligned = insert_indel(seq2_aligned, j)
		elif backtrack[i][j] == 'L':
			j -= 1
			seq1_aligned = insert_indel(seq1_aligned, i)
		else:
			i -= 1
			j -= 1
	for repeat in xrange(i):
		seq2_aligned = insert_indel(seq2_aligned, 0)
	for repeat in xrange(j):
		seq1_aligned = insert_indel(seq1_aligned, 0)
	return global_allignment(seq1,seq2,indel)[0],seq1_aligned,seq2_aligned


if __name__ == '__main__':
	result =  backtrack_allignment(seq1,seq2,indel)
	for res in result:
		print res
