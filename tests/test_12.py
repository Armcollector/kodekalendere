from AoC.Aoc12 import Planet

def test_planet():
    p = Planet()


def test_parse():
    from AoC.Aoc12 import parse_input

    r = parse_input("""<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>""")
    assert r == [[-7,17,-11], [9,12,5], [-9,0,-4], [4,6,0]]