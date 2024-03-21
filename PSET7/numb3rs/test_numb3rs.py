from numb3rs import validate


def main():
    test_first()
    test_sec()
    test_third()
    test_fourth()
    test_fifth()


def test_first():
    assert validate("127.0.0.1") == True

def test_sec():
    assert validate("255.255.255.255") == True

def test_third():
    assert validate("512.512.512.512") == False

def test_fourth():
    assert validate("1.2.3.1000") == False
    assert validate("1000.2.3.2") == False

def test_fifth():
    assert validate("cat") == False

if __name__ == "__main__":
    main()