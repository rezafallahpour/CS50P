from project import add, subtract, multiply, divide



def test_add():
    assert add(45,10) == 55
    assert add(5,10) == 15

def test_subtract():
    assert subtract(45,15) == 30
    assert subtract(10,5) == 5

def test_multiply():
    assert multiply(10,5) == 50
    assert multiply(2,4) == 8

def test_divide():
    assert divide(10,5) == 2


