__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys


def transcript(dna):
    rna = dna.replace('T','U')
    return rna

def reverse_compliment(dna):
	seq_dict = {'A':'T','G':'C','T':'A','C':'G'}
	reverse = ''.join([seq_dict[base] for base in dna[::-1]])
	return reverse

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

def peptide_encoding(dna,peptide):
	encodings = []
	for i in range(len(dna) - 3*len(peptide) + 1):
		dna_slice = dna[i:i+3*len(peptide)]
		rna_slice = transcript(dna_slice)
		rev_comp_dna_slice = reverse_compliment(dna_slice)
		rev_rna_slice = transcript(rev_comp_dna_slice)
		protein = translate(rna_slice)
		rev_protein = translate(rev_rna_slice)
		if translate(rna_slice) == peptide or translate(rev_rna_slice) == peptide:
			encodings.append(dna_slice)
	return encodings

def main():
	dna = sys.argv[1]
	peptide = sys.argv[2]
	ans = peptide_encoding(dna,peptide)
	for res in ans:
		print res

if __name__ == '__main__':
	main()
