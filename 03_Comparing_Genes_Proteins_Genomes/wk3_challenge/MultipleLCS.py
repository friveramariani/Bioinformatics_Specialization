__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

seq1 = data[0]
seq2 = data[1]
seq3 = data[2]

def multiple_allignment(s1,s2,s3):
	n = len(s1)
	m = len(s2)
	o = len(s3)

	s = [[[0 for _ in xrange(o+1)] for _ in xrange(m+1)] for _ in range(n+1)]
	backtrack = [[[0 for _ in xrange(o+1)] for _ in xrange(m+1)] for _ in range(n+1)]
	
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			for k in xrange(1,o+1):
				scores = [s[i-1][j-1][k-1] + int(s1[i-1] == s2[j-1] == s3[k-1]), s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j][k-1], s[i][j-1][k-1]]
				backtrack[i][j][k], s[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

	insert_indel = lambda word, i: word[:i] +'-'+ word[i:]

	s1_allign, s2_allign, s3_allign = s1, s2, s3

	max_score = s[n][m][o]

	i,j,k = n,m,o

	while i*j*k != 0:
		if backtrack[i][j][k] == 1:
			i -= 1
			s2_allign = insert_indel(s2_allign,j)
			s3_allign = insert_indel(s3_allign,k)

		elif backtrack[i][j][k] ==2:
			j -= 1
			s1_allign = insert_indel(s1_allign,i)
			s3_allign = insert_indel(s3_allign,k)

		elif backtrack[i][j][k] == 3:
			k -= 1
			s1_allign = insert_indel(s1_allign,i)
			s2_allign = insert_indel(s3_allign,k)

		elif backtrack[i][j][k] == 4:
			i -= 1
			j -= 1
			s3_allign = insert_indel(s3_allign,k)

		elif backtrack[i][j][k] == 5:
			i -= 1
			k -= 1
			s2_allign = insert_indel(s2_allign,j)

		elif backtrack[i][j][k] == 6:
			j -= 1
			k -= 1
			s1_allign = insert_indel(s1_allign,i)

		else:
			i -= 1
			j -= 1
			k -= 1


	while len(s1_allign) != max(len(s1_allign),len(s2_allign),len(s3_allign)):
		s1_allign = insert_indel(s1_allign,0)
	while len(s2_allign) != max(len(s1_allign),len(s2_allign),len(s3_allign)):
		s2_allign = insert_indel(s2_allign,0)
	while len(s3_allign) != max(len(s1_allign),len(s2_allign),len(s3_allign)):
		s3_allign = insert_indel(s3_allign,0)

	return str(max_score), s1_allign, s2_allign, s3_allign


if __name__ == '__main__':
	ans = multiple_allignment(seq1,seq2,seq3)
	for res in ans:
		print res
