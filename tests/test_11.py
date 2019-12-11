from AoC.Aoc11 import Robot


def test11():
    pass

def test_rotate():
    r = Robot([])

    assert r.facing() == (0,1)

    r.turn(1)

    assert r.facing() == (1,0)

    r.turn(0)
    assert r.facing() == (0,1)

def test_move_forward():
     r = Robot([])

     r.move_forward()
     r.move_forward()
     assert r.position == (0,2)