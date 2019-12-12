import re

class Planet:
    
    def __init__(self):
        self.position = None
        self.velocity = None

class System:

    def __init__(self,_input):
        self.planets = self.create_planets(_input)

    def create_planets(self, _input):
        pass

    def parse_input(self,x):

        return [ [int(i) for i in re.findall('(-*[0-9]+)',l)] for l in x.splitlines() ]

if __name__ == '__main__':
    pass
    x = re.match('(-*[0-9]*)',"<x=-7, y=17, z=-11>").groups()
    pass
"""
    <x=-7, y=17, z=-11>
    <x=9, y=12, z=5>
    <x=-9, y=0, z=-4>
    <x=4, y=6, z=0>"""