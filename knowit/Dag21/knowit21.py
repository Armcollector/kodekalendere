with open(r"c:\git\kodekalendere\knowit\dag21\generations.txt", 'r') as f:    
    generasjoner = f.read().splitlines()
    generasjoner = [ [  tuple( int(i) for i in a.split(',')) for a in g.split(';') ] for g in  generasjoner  ]


antall_alver = len(generasjoner[0])


sets = [set([i]) if i % 2 else set([]) for i in range(antall_alver)]

cnt = sum(  1 if i %2 else 0 for i in range(antall_alver) )

print(cnt)


for gn, g in enumerate(generasjoner,1):
    
    newset = [ set([]) for i in range(antall_alver)]
    
    for i,(a,b) in enumerate(g):
        newset[a] = newset[a].union(sets[i])
        
        if len(newset[a]) == cnt:
            print("found", gn,a)
        
        newset[b] = newset[b].union(sets[i])

        if len(newset[b]) == cnt:
            print("found", gn,b)

    sets = newset
    
print(sets)
