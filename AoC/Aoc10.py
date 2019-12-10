from itertools import product
from fractions import Fraction
from math import gcd




def f(x):


    asteroids = newmethod748(x)

    d = {}            
    for f,t in product(asteroids,repeat=2):
        x = f[0]-t[0]
        y = f[1]-t[1]

        if f == t:
            continue

        if gcd(x,y) == 0:
            print(f,t)
        g = gcd(x,y)
        x//= g
        y//= g



        if f not in d:
            d[f] = set([])

        d[f].add((x,y))
    
    


    return max(len(v) for v in d.values())

def newmethod748(x):
    asteroids = set({})

    for i,r in enumerate(x.splitlines()):
        for j, a in enumerate(r):
            if a != '.':
                asteroids.add((j,i))
    return asteroids



def laser(x):
    asteroids = newmethod748(x)

    d = {}            
    for f,t in product(asteroids,repeat=2):
        x = f[0]-t[0]
        y = f[1]-t[1]

        if f == t:
            continue

        if gcd(x,y) == 0:
            print(f,t)
        g = gcd(x,y)
        x//= g
        y//= g



        if f not in d:
            d[f] = set([])

        d[f].add((x,y))
    
    


    return max(len(i) for i in d.values())