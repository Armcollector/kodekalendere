from itertools import product
from fractions import Fraction


def f(x):


    asteroids = set({})

    for i,r in enumerate(x.splitlines()):
        for j, a in enumerate(r):
            if a != '.':
                asteroids.add((j,i))

    #asteroids = { ( int((x+0.5)*2), int((y+0.5)*2)) for x,y in asteroids } 
    
    d = {}            
    for f,t in product(asteroids,repeat=2):
        x = f[0]-t[0]
        y = f[1]-t[1]

        if f == t:
            continue

        if f not in d:
            d[f] = set([])

        if y != 0:
            d[f].add(Fraction(x,y))
        else:
            if x > 0:
                d[f].add((1,0))
            else:
                d[f].add((-1,0))

    print(d[(0,0)])
    return max(len(i) for i in d.values())




print(f("""#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c"""))

# assert f(""".#..#
# .....
# #####
# ....#
# ...##"""
# ) == 8