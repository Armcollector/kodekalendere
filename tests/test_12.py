from AoC.Aoc12 import Planet

def test_planet():
    p = Planet()


def test_parse():
    from AoC.Aoc12 import parse_input

    r = parse_input("<x=-7, y=17, z=-11>")
    assert r == [-7,17,-11]