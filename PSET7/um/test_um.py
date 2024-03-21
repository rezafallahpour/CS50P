from um import count



def test_1():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("Hello, um, world") == 1