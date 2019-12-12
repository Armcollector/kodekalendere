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

    def __repr__(self):
        return f"pos={self.position}, vel={self.velocity}"


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
    
    def step(self):
        self.apply_gravity()
        self.apply_velocity()
        self.step +=1

    def __repr__(self):
        s = f"After {self.steps}:\n"
        for i in self.planets:
            s += str(i) +"\n"
        return s
    
if __name__ == '__main__':

    s = System("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""")

    print(s)