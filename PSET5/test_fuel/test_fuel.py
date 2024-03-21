from fuel import convert, gauge
import pytest

def main():
    test_new()
    test_val()
    test_zer()
    test_1()
    test_5()
    test_99()



def test_new():
    assert convert("12/15") == 80
def test_val():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
def test_zer():
    with pytest.raises(ValueError):
        convert('cat/dog')
def test_1():
    assert gauge(1) == "E"
def test_5():
    assert gauge(50) == "50%"
def test_99():
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()
