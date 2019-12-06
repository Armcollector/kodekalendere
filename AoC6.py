import networkx as nx
from itertools import combinations
g= nx.Graph()

x = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

orbits = [i.split(')') for i in   x.splitlines()]
g.add_edges_from(orbits)
s = 0
for a in g.nodes():
    print(a,'COM',nx.shortest_path(g,a,'COM'))
    s+= len(nx.shortest_path(g,a,'COM')) -1

print(s)
