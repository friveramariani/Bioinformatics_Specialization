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

score_PAM250 = [[2,-2,0,0,-3,1,-1,-1,-1,-2,-1,0,1,0,-2,1,1,0,-6,-3],
		 		[-2,12,-5,-5,-4,-3,-3,-2,-5,-6,-5,-4,-3,-5,-4,0,-2,-2,-8,0],
		 		[0,-5,4,3,-6,1,1,-2,0,-4,-3,2,-1,2,-1,0,0,-2,-7,-4],
		 		[0,-5,3,4,-5,0,1,-2,0,-3,-2,1,-1,2,-1,0,0,-2,-7,-4],
		 		[-3,-4,-6,-5,9,-5,-2,1,-5,2,0,-3,-5,-5,-4,-3,-3,-1,0,7],
		 		[1,-3,1,0,-5,5,-2,-3,-2,-4,-3,0,0,-1,-3,1,0,-1,-7,-5],
		 		[-1,-3,1,1,-2,-2,6,-2,0,-2,-2,2,0,3,2,-1,-1,-2,-3,0],
		 		[-1,-2,-2,-2,1,-3,-2,5,-2,2,2,-2,-2,-2,-2,-1,0,4,-5,-1],
		 		[-1,-5,0,0,-5,-2,0,-2,5,-3,0,1,-1,1,3,0,0,-2,-3,-4],
		 		[-2,-6,-4,-3,2,-4,-2,2,-3,6,4,-3,-3,-2,-3,-3,-2,2,-2,-1],
		 		[-1,-5,-3,-2,0,-3,-2,2,0,4,6,-2,-2,-1,0,-2,-1,2,-4,-2],
		 		[0,-4,2,1,-3,0,2,-2,1,-3,-2,2,0,1,0,1,0,-2,-4,-2],
		 		[1,-3,-1,-1,-5,0,0,-2,-1,-3,-2,0,6,0,0,1,0,-1,-6,-5],
		 		[0,-5,2,2,-5,-1,3,-2,1,-2,-1,1,0,4,1,-1,-1,-2,-5,-4],
		 		[-2,-4,-1,-1,-4,-3,2,-2,3,-3,0,0,0,1,6,0,-1,-2,2,-4],
		 		[1,0,0,0,-3,1,-1,-1,0,-3,-2,1,1,-1,0,2,1,-1,-2,-3],
		 		[1,-2,0,0,-3,0,-1,0,0,-2,-1,0,0,-1,-1,1,3,0,-5,-3],
		 		[0,-2,-2,-2,-1,-1,-2,4,-2,2,2,-2,-1,-2,-2,-1,0,4,-6,-2],
		 		[-6,-8,-7,-7,0,-7,-3,-5,-3,-2,-4,-4,-6,-5,2,-2,-5,-6,17,0],
		 		[-3,0,-4,-4,7,-5,0,-1,-4,-1,-2,-2,-5,-4,-4,-3,-3,-2,0,10]]


def getscore(AA1,AA2):
	return score_PAM250[aa_no[AA1]][aa_no[AA2]]

indel = -5


def local_allignment(s1,s2,indel_penalty):
	n = len(s1)
	m = len(s2)
	s = [[0 for repeat_j in xrange(len(s2)+1)] for repeat_i in xrange(len(s1)+1)]
	backtrack = [['0' for repeat_j in xrange(len(s2)+1)] for repeat_i in xrange(len(s1)+1)]
	for i in xrange(1,n+1):
		s[i][0] = s[i-1][0]
		#backtrack[i][0] = 'Up'
	for j in xrange(1,m+1):
		s[0][j] = s[0][j-1]
		#backtrack[0][j] = 'Left'
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			up_score = s[i-1][j] + indel_penalty
			left_score = s[i][j-1] + indel_penalty
			diag_score = s[i-1][j-1] + getscore(s1[i-1],s2[j-1])
			s[i][j] = max(0,left_score,up_score,diag_score)
			if s[i][j] == 0:
				backtrack[i][j] = '0'
			if s[i][j] == up_score:
				backtrack[i][j] = 'U'
			if s[i][j] == left_score:
				backtrack[i][j] = 'L'
			if s[i][j] == diag_score:
				backtrack[i][j] = 'D'
	max_score = 0
	max_i = 0
	max_j = 0
	for i in xrange(1,n+1):
		for j in range(1,m+1):
			if s[i][j]>max_score:
				max_score=s[i][j]
				max_i = i
				max_j = j

	return max_score,max_i,max_j,backtrack

def backtrack_local(s1,s2,indel_penalty):
	score,maxi,maxj,backtrack = local_allignment(s1,s2,indel_penalty)
	align1 = ''
	align2 = ''
	i,j = maxi,maxj
	while backtrack[i][j] != '0':
		if backtrack[i][j] == 'D':
			align1 += s1[i-1]
			align2 += s2[j-1]
			i -= 1
			j -= 1
		elif backtrack[i][j] == 'L':
			align1 += '-'
			align2 += s2[j-1]
			j -= 1
		elif backtrack[i][j] == 'U':
			align1 += s1[i-1]
			align2 += '-'
			i -= 1

	align1 = align1[::-1]
	align2 = align2[::-1]

	return score,align1,align2

if __name__=='__main__':
	ans =  backtrack_local(seq1,seq2,indel)
	for res in ans:
		print res
