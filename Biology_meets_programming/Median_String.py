__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def hamming(pattern, check):
    match = False
    distance = 0
    for i in range(len(pattern)):
        if check[i] != pattern[i]:
            distance += 1
    return distance

def neighbors(s, d):
    l = []
    if d==0 or len(s)==0:
        return[s]
    for n in 'ACGT':
        d1 = d-1
        if n==s[0]:
            d1 = d
        for m in neighbors(s[1:], d1):
            l.append(n + m)
    return l

def profileNuc(pro,nuc,seq):
    for i in range(len(seq)):
        if seq[i] == nuc:
            pro[i] += 1
    return pro

def enumMers(dna,mers,d):
    for seq in dna:
        for i in range(len(seq)):
            if len(seq[i:i+k]) == k:
                mers.update(neighbors(seq[i:i+k],d))
f = open('ww.txt','r')
ins = f.read().split()
f.close()

k = int(ins[0])
dna = ins[1:]

seqlen = len(dna[0])

mers = set()
enumMers(dna,mers,1)

merds = dict.fromkeys(mers,0)
for mer in mers:
    distances = 0
    for seq in dna:
        min_d = seqlen
        for i in range(seqlen):
            check = seq[i:i+k]
            if len(check) == k:
                distance = hamming(mer,check)
                if distance < min_d:
                    min_d = distance
        distances += min_d
    merds[mer] = distances

minmer = min(merds,key=lambda x: merds[x])

print(minmer)
