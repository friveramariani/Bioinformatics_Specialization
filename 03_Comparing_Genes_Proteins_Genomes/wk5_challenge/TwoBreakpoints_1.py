__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

#seq = map(int,seq[1:-1].split())
seq = data[0]
ind = map(int,data[1].split(', '))
i,j,k,l = ind

seqs = seq[1:-1].split(' ')
seqs = map(int,seqs)
#num_seqs = []
#for se in seqs:
#	num_seqs.append(map(int,se.split(',')))

def chromosometocycle(chromosome):
	nodes = []
	for i in chromosome:
		if i > 0:
			nodes.append(2*i - 1)
			nodes.append(2*i)
		else:
			nodes.append(-2*i)
			nodes.append(-2*i - 1)
	return nodes

def cycletochromosome(nodes):
	chromosome = []
	for j in range(1,len(nodes)/2+1):
		if nodes[2*j - 2] < nodes[2*j - 1]:
			chromosome.append(nodes[2*j - 1]/2)
		else:
			chromosome.append(-nodes[2*j - 2]/2)
	return chromosome

def colorededges(p):
	edges = []
	if type(p[0]) == int:
		chromosome = p
		chromosome.append(chromosome[0])
		nodes = chromosometocycle(chromosome)
		for j in range(1,len(chromosome)):
			edges.append([nodes[2*j-1],nodes[2*j]])
		chromosome.pop()
		return edges
	else:
		for chromosome in p:
			temp = chromosome[0]
			chromosome.append(temp)
			nodes = chromosometocycle(chromosome)
			for j in range(1,len(chromosome)):
				edges.append([nodes[2*j-1],nodes[2*j]])
		return edges

def get_blacked_edges(col_edges):
	blacked_edges = []
	for node in col_edges:
		temp = []
		for num in node:
			if num%2 == 0:
				temp.append(num/2)
			else:
				temp.append(-(num+1)/2)
		blacked_edges.append(temp)
	return blacked_edges

def graphtogenome(col_edges):
	blacked_edges = get_blacked_edges(col_edges)
	chromosome_list = []
	while blacked_edges != []:
		start,end = blacked_edges[0]
		blacked_edges.remove(blacked_edges[0])
		loop_end = -1*start
		chromosome = [start]
		while end != loop_end:
			for i in range(len(blacked_edges)):
				if blacked_edges[i][0] == -1*end:
					start,end = blacked_edges[i]
					blacked_edges.remove(blacked_edges[i])
					break
				elif blacked_edges[i][1] == -1*end:
					blacked_edges[i] = blacked_edges[i][::-1] 
					start,end = blacked_edges[i]
					blacked_edges.remove(blacked_edges[i])
					break
			
			chromosome.append(start)
		chromosome_list.append(chromosome)
	return chromosome_list

def two_breakongenomegraph(col_edges,i,j,k,l):
	if [i,j] in col_edges:
		col_edges.remove([i,j])
	else:
		col_edges.remove([j,i])
	if [k,l] in col_edges:
		col_edges.remove([k,l])
	else:
		col_edges.remove([l,k])
	col_edges.append([i,k])
	col_edges.append([j,l])
	return col_edges

def two_breakongenome(p,i,j,k,l):
	colored_edges = colorededges(p)
	genomegraph = two_breakongenomegraph(colored_edges,i,j,k,l)
	ans = graphtogenome(genomegraph)
	return ans



if __name__ == '__main__':

	#ans =  cycletochromosome(seq)
	#print ans
	#print '('+' '.join(str(i) for i in ans)+')'
	#print '('+' '.join('+'+str(i) if i>0 else str(i) for i in ans)+')'
	ans = two_breakongenome(seqs,i,j,k,l)
	str_ans = ''
	for res in ans:
		str_ans += '('+' '.join('+'+str(i) if i>0 else str(i) for i in res)+')'
		#str_ans += str(tuple(res))+', '
	print str_ans
