__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

file_name = sys.argv[1]

def path(reads):
	string = reads[0]
	for read in reads[1:]:
		string = string + read[-1]
	return string


def main():
	seqs = []
	with open(file_name) as file:
		for line in file:
			seqs.append(line[:-1])
	ans = path(seqs)
	print ans


if __name__ == '__main__':
	main()
