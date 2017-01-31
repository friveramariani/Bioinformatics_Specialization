__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

spectrum = []

with open(filename) as file:
	for line in file:
		spectrum = map(int,line.split())

spectrum = list(set(spectrum))

def aminoacid_mass_dict():
    '''Returns a dictionary that gives mass of amino acid.'''
    with open('integer_mass_table.txt') as input_data:
        masses = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    mass_dict = {}
    for mass in masses:
        mass_dict[mass[0]] = int(mass[1])

    return mass_dict

def expand(lists,spectrum):
	aa = aminoacid_mass_dict()
	aa_weights = sorted(list(set(aa.values())))
	if lists == []:
		for weight in aa_weights:
			if weight in spectrum:
				lists.append([weight])
		return lists	
	else:
		newlists=[]
		for sublist in lists:
			newlist = []
			for weight in aa_weights:
				if (sum(sublist) + weight) in spectrum:
					newlist.append(sublist+[weight])
			for x in newlist:
				newlists.append(x)
	return newlists

def cyclopeptidesequencing(spectrum):
	peptide = expand([],spectrum)
	while sum(peptide[0]) != max(spectrum):
		peptide = expand(peptide,spectrum)
	return peptide
	'''for res in sorted(peptide,reverse = True):
		print '-'.join(str(num) for num in res),'''

if __name__ == '__main__':
	sequence = cyclopeptidesequencing(spectrum)
	with open('res.txt', 'w') as output_data:
		for res in sorted(sequence,reverse=True):
			output_data.write('-'.join(str(num) for num in res ) + ' ')
