from bank import value

def main():
    test_20()
    test_100()
    test_zero()


def test_zero():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello ggg") == 0


def test_100():
    assert value("What’s up") == 100
    assert value("Wha  ") == 100
    assert value("new") == 100

def test_20():
    assert value("hi") == 20



if __name__ == "__main__":
    main()