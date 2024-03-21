from plates import is_valid

def main():
    test_main()
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


def test_main():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False



def test_1():
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_2():
    assert is_valid("AAA222") == True

def test_3():
    assert is_valid("SC50") == True
def test_4():
    assert is_valid("PI3.14") == False

def test_5():
    assert is_valid("ECTO88") == True

if __name__ == "__main__":
    main()