from time import time

start = time()

with open(r"c:\git\kodekalendere\knowit\dag21\generations.txt", 'r') as f:    
    generasjoner = f.read().splitlines()
    generasjoner = [ [  tuple( int(i) for i in a.split(',')) for a in g.split(';') ] for g in  generasjoner  ]

def solve(generasjoner):

    antall_alver = len(generasjoner[0])
    sets = [set([i]) if i % 2 else set([]) for i in range(antall_alver)]

    for gn, g in enumerate(generasjoner,1):
        
        newset = [ set([]) for i in range(antall_alver)]
        
        for i,(a,b) in enumerate(g):
            newset[a] = newset[a].union(sets[i])    
            newset[b] = newset[b].union(sets[i])

        if 2**(gn+1) >= antall_alver//2:
            for alv, s in enumerate(newset):
                if len(s) == antall_alver//2:
                    return f"{gn}:{alv} er løsningen."

        sets = newset
    
print(solve(generasjoner))
print( time() - start )