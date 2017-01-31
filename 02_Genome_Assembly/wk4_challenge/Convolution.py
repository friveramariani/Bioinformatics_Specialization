__author__ = 'Felix E. Rivera-Mariani, friveamariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		spectrum = map(int,line.split())

def convolution(spec):
	convolution_list = [str(i-j) for i in spec for j in spec if i-j > 0]
	return convolution_list

def main():
	ans = convolution(spectrum)
	for res in ans:
		print res,
	with open('res.txt', 'w') as output_data:
		output_data.write(' '.join(convolution(spectrum)))


if __name__ == '__main__':
	main()
