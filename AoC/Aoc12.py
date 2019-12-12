import re
from itertools import product
import numpy as np

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
        self.logp = []
        self.logv = []

    def energy(self ):
        return sum(abs(i) for i in self.position) * sum(abs(i) for i in self.velocity)

    def apply_gravity(self, m2):
        self.velocity = [v1 + delta(p2-p1) for v1, p1,p2 in zip(self.velocity, self.position, m2.position)]

    def apply_velocity(self):
        self.position = [p + v for p,v in zip(self.position, self.velocity)]

    def __repr__(self):
        return f"pos={self.position}, vel={self.velocity}"

    def log_planet(self):
        self.logp.append(self.position)
        self.logv.append(self.velocity)

    def find_periods(self):
        return np.array(self.logp)

class System:

    def __init__(self,_input):
        self.planets = self.create_planets(_input)
        self.steps = 0

    def create_planets(self, _input):
        return [Planet(i) for i in self.parse_input(_input)]

    def parse_input(self,x):

        return [ [int(i) for i in re.findall('(-*[0-9]+)',l)] for l in x.splitlines() ]

    def total_energy(self):
        return sum( i.energy() for i in self.planets)

    def apply_gravity(self):
        for m1, m2 in product(self.planets, self.planets):
            m1.apply_gravity(m2)

    def apply_velocity(self):
        for m in self.planets:
            m.apply_velocity()
    
    def log_planets(self):
        for m in self.planets:
            m.log_planet()

    def step(self):
        self.log_planets()
        self.apply_gravity()
        self.apply_velocity()
        self.steps +=1

    def __repr__(self):
        s = f"After {self.steps}:\n"
        for i in self.planets:
            s += str(i) +"\n"
        return s

def cycle(a):

    k = 1
    while True:
        if all( a[i] == a[i+k] for i in range(len(a)-k) ):
            return k
        k+=1

if __name__ == '__main__':

    from time import time

    s = System("""<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>""")

    start = time()

    s = System("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""")

    for i in range(10):
        s.step()
    
    print(s.planets[0].find_periods())
        
    print(s)
    print(s.total_energy())
    print(time()-start)


