__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

path = data[0]
states = data[2].split()
transition = []
transition.append(map(float,data[5].split()[1:]))
transition.append(map(float,data[6].split()[1:]))
statelookup = {states[i]:i for i in range(len(states))}

def probability_hmm(path,states,transition,statelookup):
	prob = 0.5
	for i in range(len(path) - 1):
		prob *= transition[statelookup[path[i]]][statelookup[path[i + 1]]]
	return prob

if __name__ == '__main__':
	ans = probability_hmm(path,states,transition,statelookup)
	print ans