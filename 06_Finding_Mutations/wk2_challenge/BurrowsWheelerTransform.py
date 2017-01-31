__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	string = file.readline()
string = string[:-1]

def bwt(string):
	perms = list()
	for i in range(len(string)):
		perms.append(string[i:] + string[:i])
	perms = sorted(perms)
	ans = ''
	for perm in perms:
		ans += perm[-1]
	return ans

if __name__ == '__main__':
	ans = bwt(string)
	print (ans)