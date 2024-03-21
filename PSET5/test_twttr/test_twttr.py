from twttr import shorten


def test_main():
    assert shorten("reza") == "rz"
    assert shorten("REZA") == "RZ"
    assert shorten("1234") == "1234"
    assert shorten("/.?,") == "/.?,"