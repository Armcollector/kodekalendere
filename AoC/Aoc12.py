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
        return [self.cycle(np.array(self.logp)[:,i]) for i in range(3)] + [self.cycle(np.array(self.logv)[:,i]) for i in range(3)]
  
    def cycle(self, a):

        k = 1
        while True:
            if all( a[i] == a[i+k] for i in range(len(a)-k) ):
                return k
            k+=1

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



if __name__ == '__main__':

    from time import time

    s = System("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""")

    s = System("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""")

    s = System("""<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>""")

    start = time()

    import sympy

    for j in range(1,2500000):
        if j%10000 == 0:
            c = []
            for i in s.planets:
                c+= i.find_periods()
            print(j, "cycle", sympy.lcm(c))
    
        s.step()
   

    
    import sympy

    

        
    print(s)
    print(s.total_energy())
    print(time()-start)


