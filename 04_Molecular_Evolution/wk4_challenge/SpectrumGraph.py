__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		masses = map(int,line[:-1].strip().split(' '))
		masses.append(0)
		masses = sorted(masses)


def aminoacid_mass_dict():
    '''Returns a dictionary that gives mass of amino acid.'''
    with open('integer_mass_table.txt') as input_data:
        masses = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    mass_dict = {}
    for mass in masses:
        mass_dict[int(mass[1])] = mass[0]

    return mass_dict

def spectrumgraph(masses):
	mass_dict = aminoacid_mass_dict()
	for i in range(len(masses)):
		for j in range(i+1,len(masses)):
			#print masses[j] - masses[i]
			if masses[j] - masses[i] in mass_dict.keys():
				print str(masses[i])+'->'+str(masses[j])+':'+str(mass_dict[masses[j] - masses[i]])




if __name__ == '__main__':
	print (spectrumgraph(masses))
