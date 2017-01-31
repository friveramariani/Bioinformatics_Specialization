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

sigma = -5

def middle_col_score(s1,s2,sigma):
	n = len(s1)
	m = len(s2)
	s = [[i*j*(-sigma) for j in xrange(-1,1)] for i in xrange(n+1)]
	s[0][1] = sigma
	backtrack = [0]*(n+1)

	for j in xrange(1,m/2 + 1):
		for i in xrange(0,n+1):
			if i == 0:
				s[i][1] = j*sigma
			else:
				scores = [s[i-1][0] + getscore(s1[i-1],s2[j-1]),s[i][0] + sigma, s[i-1][1] + sigma]
				s[i][1] = max(scores)
				backtrack[i] = scores.index(s[i][1])

		if j != m/2:
			s = [[row[1]]*2 for row in s]

	return [row[1] for row in s], backtrack

def middle_edge(s1,s2,sigma):
	source_to_middle = middle_col_score(seq1, seq2, sigma)[0]
	middle_to_sink, backtrack = map(lambda l: l[::-1], middle_col_score(seq1[::-1], seq2[::-1]+['', '$'][len(seq2) % 2 == 1 and len(seq2) > 1], sigma))
	scores = map(sum, zip(source_to_middle, middle_to_sink))
	max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

	if max_middle == len(scores) - 1:
		next_node = (max_middle, len(seq2)/2 + 1)
	else:
		next_node = [(max_middle + 1, len(seq2)/2 + 1), (max_middle, len(seq2)/2 + 1), (max_middle + 1, len(seq2)/2),][backtrack[max_middle]]

	return (max_middle, len(seq2)/2), next_node


if __name__=='__main__':
	ans =  middle_edge(seq1, seq2, sigma)
	for res in ans:
		print res,