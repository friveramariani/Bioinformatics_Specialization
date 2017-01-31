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

def space_efficient_global_alligment(s1, s2, sigma):

	def linear_space_allignment(top, bottom, left, right):
		
		if left == right:
			return [s1[top:bottom], '-'*(bottom-top)]

		elif top == bottom:
			return ['-'*(right-left), s2[left:right]]

		elif bottom - top == 1 or left - right == 1:
			return backtrack_allignment(s1[top:bottom], s2[left:right], sigma)

		else:
			mid_node, next_node = middle_edge(s1[top:bottom], s2[left:right], sigma)
			mid_node = tuple(map(sum, zip(mid_node, [top, left])))
			next_node = tuple(map(sum, zip(next_node, [top, left])))
			current = [['-', s1[mid_node[0] % len(s1)]][next_node[0] - mid_node[0]], ['-', s2[mid_node[1] % len(s2)]][next_node[1] - mid_node[1]]]
			a = linear_space_allignment(top, mid_node[0], left, mid_node[1])
			b = linear_space_allignment(next_node[0], bottom, next_node[1], right)
			return [a[i] + current[1] + b[i] for i in xrange(2)]
	s1_allign, s2_allign = linear_space_allignment(0,len(s1),0,len(s2))
	score = sum([sigma if '-' in pair else getscore(pair[0],pair[1]) for pair in zip(s1_allign,s2_allign)])
	return str(score), s1_allign, s2_allign

if __name__ == '__main__':
	ans = space_efficient_global_alligment(seq1, seq2, sigma)
	for res in ans:
		print ans
