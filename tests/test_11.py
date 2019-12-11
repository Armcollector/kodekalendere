from AoC.Aoc11 import Robot


def test11():
    pass

def test_rotate():
    r = Robot([])

    assert r.facing() == (0,1)

    r.turn(1)