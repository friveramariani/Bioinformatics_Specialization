__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys
from collections import Counter 

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line)
peptide = data[0][:-1]
exp_spec = map(int,data[1].split())

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

def scoring(peptide,exp_spec):
	aa_mass = aminoacid_mass_dict()
	#theo_spec = cyclic_spectrum(peptide,aa_mass)
	theo_spec = linear_spectrum(peptide,aa_mass)
	theo_count = Counter(theo_spec)
	exp_count = Counter(exp_spec)
	count = 0
	for mass in exp_count.keys():
		if mass in theo_count.keys():
			count += min(exp_count[mass],theo_count[mass])
	return count

def main():
	print scoring(peptide,exp_spec)


if __name__ == '__main__':
	main()
