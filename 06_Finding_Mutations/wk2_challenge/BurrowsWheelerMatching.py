__author__ = 'Felix E. Rivera-Mariani, friveramariani@gmail.com, www.friveram.com'


def bwmatching(s,patterns):
    """
    CODE CHALLENGE: Implement BWMATCHING.
    Input: A string BWT(Text), followed by a collection of Patterns.
    Output: A list of integers, where the i-th integer corresponds to the number of substring
    matches of the i-th member of Patterns in Text.
    """    
    def pattern_count(first_column,last_column,pattern,last_to_first):
        top = 0
        bottom = len(last_column) - 1
        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]
                if symbol in last_column[top:bottom+1]:
                    top_index = last_column.find(symbol,top,bottom+1)
                    bottom_index = last_column.rfind(symbol,top,bottom+1)
                    top = last_to_first[top_index]
                    bottom = last_to_first[bottom_index]
                else:
                    return 0
            else:
                return bottom - top + 1
        return 0    
    l = len(s)
    # produce a list tuple (char,index) for the last column
    last_char_rank = [(s[i],i) for i in range(l)]
    # produce the list tuple (char,rank) for the first column
    first_char_rank = sorted(last_char_rank)
    # build the last_to_first conversion array
    
    first_to_last = [ i for (c,i) in first_char_rank]
    last_to_first = [None]*l
    for first,last in enumerate(first_to_last):
        last_to_first[last] = first
    first_column = sorted(s)
    last_column = s
    
#    for i in range(l):
#        r = str(first_column[i])+('*'*(l-2))+str(last_column[i])
#        rr = str(last_column[first_to_last[i]])+('*'*(l-2))+str(first_column[last_to_first[i]])
#        assert rr == r
    
    return [pattern_count(first_column,last_column,pattern,last_to_first) for pattern in patterns]

fname = 'dataset_300_8.txt'
with open(fname, "r") as f:
    text = f.read().strip().split('\n')
    s = text[0]
    p = text[1].split(' ')
with open("12_bwmatching_result.txt", "w") as f:
    f.write(' '.join(map(str,bwmatching(s,p))))