__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

seq = ''
with open(filename) as file:
	for line in file:
		seq += line[:-1]

seq = map(int,seq[1:-1].split())

def count_breakpoints(p):
	p.insert(0,0)
	p.append(len(p))
	count = 0
	i = 0
	while i<len(p)-1:
		x = p[i]
		if p[i+1] != x + 1:
			count += 1
		i += 1
	return count

if __name__=='__main__':
	print count_breakpoints(seq)
