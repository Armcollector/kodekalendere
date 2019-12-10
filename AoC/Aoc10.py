from itertools import product
from fractions import Fraction
from math import gcd


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

        if gcd(x,y) == 0:
            print(f,t)

        x//= gcd(x,y)
        y//= gcd(x,y)



        if f not in d:
            d[f] = set([])

        d[f].add((x,y))
   
    return max(len(i) for i in d.values())


print(f("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""))

print(f(""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""))

print(f(""".#..#\n.....\n#####\n....#\n...##"""))