import numpy as np 

def count_ngram(string, n):
    count = {} 
    tokens = string.split()
    for i in range(len(tokens)-3):
        trigram = tuple(tokens[i:i+3])
        if trigram not in count:
            count[trigram] = 0
        count[trigram] += 1 
    return count 

def precision(samples, n=2):
    pn_vals = [] 
    for i in range(len(samples)):
        candn = count_ngram(samples[i]["Candidate"],n)
        refs = samples[i]["References"]
        ref = [count_ngram(refs[j],n) for j in range(len(refs))]
        pn = 0 
        for trig in candn: 
            maxref = 0 
            for j in range(len(ref)):
                if trig in ref[j]:
                    maxref = max(maxref, ref[j][trig])
            # print(trig, maxref, candn[trig])
            pn += min(candn[trig], maxref)
        pn = pn / sum([v for k,v in candn.items()])
        pn_vals.append(pn)
    return pn_vals
