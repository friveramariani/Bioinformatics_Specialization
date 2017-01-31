__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

string = sys.argv[1]

def aminoacid_mass_dict():
    '''Returns a dictionary that gives mass of amino acid.'''
    with open('integer_mass_table.txt') as input_data:
        masses = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    mass_dict = {}
    for mass in masses:
        mass_dict[mass[0]] = mass[1]

    return mass_dict


def linear_spectrum(peptide,aa_mass):
	aa_mass = aminoacid_mass_dict()
	prefix_mass = [0 for x in range(len(peptide) + 1)]
	for i in range(1,len(peptide)+1):
		prefix_mass[i] = prefix_mass[i-1] + int(aa_mass[str(peptide[i-1])])
	linear = []
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			linear.append(prefix_mass[j] - prefix_mass[i])
	linear.append(0)	
	return sorted(linear)

def cyclic_spectrum(peptide,aa_mass):
	aa_mass = aminoacid_mass_dict()
	prefix_mass = [0 for x in range(len(peptide) + 1)]
	for i in range(1,len(peptide)+1):
		prefix_mass[i] = prefix_mass[i-1] + int(aa_mass[str(peptide[i-1])])
	cyclic = []
	peptide_mass = prefix_mass[-1]
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			cyclic.append(prefix_mass[j] - prefix_mass[i])
			if i>0 and j<len(peptide):
				cyclic.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
	cyclic.append(0)
	return sorted(cyclic)

def spectrum(peptide):
	aa_mass = aminoacid_mass_dict()
	return cyclic_spectrum(peptide,aa_mass)


def main():
	ans = spectrum(string)
	for res in ans:
		print res,

if __name__ == '__main__':
	main()
