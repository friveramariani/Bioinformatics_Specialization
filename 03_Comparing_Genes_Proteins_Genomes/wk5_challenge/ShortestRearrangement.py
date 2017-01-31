__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'

import sys
import random

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

p = data[0]
p = map(int,p[1:-1].split(' '))

q = data[1]
q = map(int,q[1:-1].split(' '))


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
			chromosome.pop()
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

def shortestrearrangement(p,q):
	#print p
	print '('+' '.join('+'+str(i) if i>0 else str(i) for i in p)+')'
	red_edges = colorededges(p)
	blue_edges = colorededges(q)
	breakpointgraph = red_edges + blue_edges
	while True:
		red_edges = colorededges(p)
		for i in range(len(red_edges)):
			if red_edges[i][::-1] in blue_edges:
				red_edges[i] = red_edges[i][::-1]
		if sorted(red_edges) == sorted(blue_edges):
			break
		temp_list = []
		for blue_edge in blue_edges:
			if blue_edge not in red_edges:
				temp_list.append(blue_edge)
		node = random.choice(temp_list)
		#node = temp_list[0]
		#from_edge,to_edge = 0,0
		for red_edge in red_edges:
			if node[0] in red_edge:
				to_edge = red_edge
			elif node[1] in red_edge:
				from_edge = red_edge
		if (to_edge[1]==node[0]) & (from_edge[0]==node[1]):
			red_edges.remove(from_edge)
			red_edges.remove(to_edge)
			red_edges.append([to_edge[1],from_edge[0]])
			red_edges.append([to_edge[0],from_edge[1]])
		elif (to_edge[0]==node[0]) & (from_edge[0]==node[1]):
			red_edges.remove(from_edge)
			red_edges.remove(to_edge)
			to_edge = to_edge[::-1]
			red_edges.append([to_edge[1],from_edge[0]])
			red_edges.append([to_edge[0],from_edge[1]])
		elif (to_edge[1]==node[0]) & (from_edge[1]==node[1]):
			red_edges.remove(from_edge)
			red_edges.remove(to_edge)
			from_edge = from_edge[::-1]
			red_edges.append([to_edge[1],from_edge[0]])
			red_edges.append([to_edge[0],from_edge[1]])
		elif (to_edge[0]==node[0]) & (from_edge[1]==node[1]):
			red_edges.remove(from_edge)
			red_edges.remove(to_edge)
			from_edge = from_edge[::-1]
			to_edge = to_edge[::-1]
			red_edges.append([to_edge[1],from_edge[0]])
			red_edges.append([to_edge[0],from_edge[1]])
		breakpointgraph = red_edges + blue_edges
		p = two_breakongenome(p,to_edge[0],to_edge[1],from_edge[1],from_edge[0])
		str_p = ''
		for res in p:
			str_p += '('+' '.join('+'+str(i) if i>0 else str(i) for i in res)+')'
		print str_p
		if len(p) == 1:
			p = p[0]
		
		
		#print p
	return None

if __name__ == '__main__':
	shortestrearrangement(p,q)
