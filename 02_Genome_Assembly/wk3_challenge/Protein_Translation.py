__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

string = sys.argv[1]

def protein_dict():
    '''Returns a dictionary that translates DNA to Protein.'''
    # Get the raw codon table.
    with open('rna_codon_table.txt') as input_data:
        dna_to_protein = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    dna_dict = {}
    for translation in dna_to_protein:
        dna_dict[translation[0]] = translation[1]

    return dna_dict

def translate(sequence):
	triplets = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
	protein = ''
	codon = protein_dict()
	for triplet in triplets:
		if codon[triplet] == 'Stop':
			break
		else:
			protein += codon[triplet]
	return protein


if __name__ == '__main__':
	print translate(string)
