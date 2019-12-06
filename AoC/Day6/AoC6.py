import networkx as nx
from itertools import combinations
g= nx.Graph()

with open(r'AoC\Day6\orbits.txt','r') as f:
    x=f.read()

orbits = [i.split(')') for i in   x.splitlines()]
g.add_edges_from(orbits)
s = 0
for a in g.nodes():
    s+= len(nx.shortest_path(g,a,'COM')) -1

print("Part 1:", s)

print("Part 2:",len(nx.shortest_path(g,'YOU','SAN')) -3)
