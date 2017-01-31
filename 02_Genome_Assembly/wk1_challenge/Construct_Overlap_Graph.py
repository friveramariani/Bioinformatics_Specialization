__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


kmers = [s for s in"""
ATGCG
GCATG
CATGC
AGGCA
GGCAT
""".split() if s]

def construct_overlap_graph(kmers):
    graph = []
    for i in range(len(kmers)):
        nodes = []
        for j in range(len(kmers)):
            if _suffix(kmers[i]) == _prefix(kmers[j]) and i != j:
                nodes.append(kmers[j])
        if len(nodes) != 0:
            nodeDescriptor = kmers[i] + ' -> ' + ",".join(nodes)
            graph.append(nodeDescriptor)
    return graph

def _prefix(text):
    return text[:len(text)-1]

def _suffix(text):
    return text[-(len(text) - 1):]

overlapGraph = (construct_overlap_graph(kmers))
print ("\n".join(overlapGraph))

