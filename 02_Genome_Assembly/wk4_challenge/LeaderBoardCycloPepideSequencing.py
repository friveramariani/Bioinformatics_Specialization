__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

def ProteinWeightDict():
	'''Returns a dictionary that translates Protein to Monoisotopic Mass.'''
	table ='''A   71.03711
	C   103.00919
	D   115.02694
	E   129.04259
	F   147.06841
	G   57.02146
	H   137.05891
	I   113.08406
	K   128.09496
	L   113.08406
	M   131.04049
	N   114.04293
	P   97.05276
	Q   128.05858
	R   156.10111
	S   87.03203
	T   101.04768
	V   99.06841
	W   186.07931
	Y   163.06333''' 

	protein_weight_dict = dict()

	for protein in table.split('\n'):
		protein_weight_dict[protein.strip('\t').split()[0]] = float(protein.strip('\t').split()[1])

	return protein_weight_dict

def append_protein(add_list):
	'''Returns a list containing all peptides from add_list with every possible protein suffix.'''
	newlist = []
	for item in add_list:
		newlist += [item+ch for ch in ProteinWeightDict().keys()]
	return newlist

def spectrum(peptide):
	'''Returns the circular spectrum of a given peptide.'''
	# Initialize as the mass 0 and the mass of the entire peptide.
	spec = [0, sum([int(weight[protein]) for protein in peptide])]
	# Find the masses of the adjacent intermediary subpeptides
	spec += [sum([int(weight[protein]) for protein in (peptide*2)[j:j+i]]) for i in xrange(1,len(peptide)) for j in xrange(len(peptide))]

	return sorted(spec)

def spectrum_score(peptide, exp_spec):
	'''Returns the number of matching masses from the spectrum of peptide when compared with the spectrum exp_spec.'''
	pep_spec = spectrum(peptide)
	# Return -1 if the peptide has more mass than exp_spec.
	if pep_spec[-1] > exp_spec[-1]:
		return -1
	return sum([min(pep_spec.count(protein),exp_spec.count(protein)) for protein in set(pep_spec)])

if __name__ == '__main__':

	with open(filename) as input_data:
		n, spec = [int(line.strip()) if i==0 else map(int,line.strip().split()) for i, line in enumerate(input_data.readlines())]
	
	# Create the protein weight dictionary.
	weight = ProteinWeightDict()
	# Initialize the scores dictionary.
	scores = dict()
	# Build the intial peptides.
	seq = filter(lambda L: L[0] != -1, [[spectrum_score(peptide,spec), peptide] for peptide in append_protein(weight.keys())]) 

	# Build the sequence until the masses all grow too large.
	while seq != []:
		# Store the scores of the current sequence in a dictionary.
		scores = dict()
		for item in seq:
			if item[0] in scores:
				scores[item[0]].append(item[1])
			else:
				scores[item[0]] = [item[1]]

		# Get the n leading scores with ties, remove lower scores from dictionary.
		leaders, leader_scores = [], []
		if sum(len(peptides) for peptides in scores.values()) < n:
			leaders = scores[max(scores.keys())]
		else:
			while len(leaders) < n:
				leaders += scores[max(scores.keys())]
				del scores[max(scores.keys())]		

		# Use this line to reduce runtime, removes excess ties.
		leaders = leaders[:100]

		# Generate a new sequence of scores from the leaders.
		seq = filter(lambda L: L[0] != -1, [[spectrum_score(peptide,spec), peptide] for peptide in append_protein(leaders)])

	# By construction, the scores are listed in descending order, so take the first peptide as the leader peptide.
	leader_peptide = '-'.join([str(int(weight[protein])) for protein in leaders[0]])

	# Print and save the answer.
	print leader_peptide
	with open('res.txt', 'w') as output_data:
		output_data.write(leader_peptide)
