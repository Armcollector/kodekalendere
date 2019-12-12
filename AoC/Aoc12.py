import re
from itertools import product

def delta(n):
    if n < 0 :
        return -1
    if n == 0:
        return 0
    return 1

class Planet:
    
    def __init__(self, position ):
        self.position = position
        self.velocity = [0,0,0]

    def energy(self ):
        return sum(abs(i) for i in self.position) * sum(abs(i) for i in self.velocity)

    def apply_gravity(self, m2):
        self.velocity = [v1 + delta(v2-v1) for v1,v2 in zip(self.velocity, m2.velocity)]

    def apply_velocity(self):
        self.position = [p + v for p,v in zip(self.position, self.velocity)]

class System:

    def __init__(self,_input):
        self.planets = self.create_planets(_input)

    def create_planets(self, _input):
        return [Planet(i) for i in self.parse_input(_input)]

    def parse_input(self,x):

        return [ [int(i) for i in re.findall('(-*[0-9]+)',l)] for l in x.splitlines() ]

    def total_energy(self):
        return sum( i.energy() for i in self.planets)

    def apply_gravity(self):
        for m1, m2 in product(self.planets, self.planets):
            m1.apply_gravity(m2)
        

if __name__ == '__main__':
    pass
    x = re.match('(-*[0-9]*)',"<x=-7, y=17, z=-11>").groups()
    pass
"""
    <x=-7, y=17, z=-11>
    <x=9, y=12, z=5>
    <x=-9, y=0, z=-4>
    <x=4, y=6, z=0>"""