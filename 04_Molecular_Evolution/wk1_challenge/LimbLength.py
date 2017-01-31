__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

n = int(data[0])

j = int(data[1])

distance_matrix = []

for line in data[2:]:
	distance_matrix.append(map(int,line.split(' ')))
#print distance_matrix,j,n


def limblength(distance_matrix,j,n):
	min_num = float('Inf')
	for i in range(n):
		for k in range(n):
			if i != j and k != j:
				dis = (distance_matrix[i][j] + distance_matrix[j][k] - distance_matrix[i][k])/2
				min_num = min(min_num,dis)

	return min_num


if __name__ == '__main__':
	print limblength(distance_matrix,j,n) 