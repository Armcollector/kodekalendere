from AoC.Aoc12 import Planet

def test_planet():
    p = Planet([0,0,0])


def test_parse():
    from AoC.Aoc12 import System

    s = System("")

    r = s.parse_input("""<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>""")
    assert r == [[-7,17,-11], [9,12,5], [-9,0,-4], [4,6,0]]


def test_system():
    from AoC.Aoc12 import System
    p = System("x""""<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>""")

    assert len(p.planets) == 4
    assert all(isinstance(i, Planet) for i in p.planets)

def test_apply_gravity():
    p1 = Planet([3,0,0])
    p2 = Planet([5,0,0])
    
    p1.apply_gravity(p2) 

    assert p1.velocity[0]