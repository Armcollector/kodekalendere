from itertools import product
from fractions import Fraction
from math import gcd




def select_asteroid(x):


    asteroids = extract_asteroids(x)

    d = {}            
    for f,t in product(asteroids,repeat=2):
        x,y = diff(f, t)

        if f == t:
            continue

        x, y = reduce(x, y)

        if f not in d:
            d[f] = set([])

        d[f].add((x,y))
    
    
    _m = max((len(v),k) for k,v in d.items())
    return _m

def reduce(x, y):
    g = gcd(x,y)
    x//= g
    y//= g
    return x, y

def extract_asteroids(x):
    asteroids = set({})

    for i,r in enumerate(x.splitlines()):
        for j, a in enumerate(r):
            if a == '#':
                asteroids.add((j,i))
    return asteroids



def laser(x):
    asteroids = extract_asteroids(x)
    #f = select_asteroid(x)[1]
    f = (8,3)
    d = {}    

    for t in asteroids:
        print(f, t)
        
        x,y = diff(f, t)
        angle = reduce(x,y)


def diff(f, t):
    x = f[0]-t[0]
    y = f[1]-t[1]
    return x,y 
        
    


    
 



x = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##"""

laser(x)