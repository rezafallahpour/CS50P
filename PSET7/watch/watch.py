import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        f = re.search(r'(\/embed)\/(\w*)\"',s)
        g = f.groups()
        return ("https://youtu.be/"+g[1])
    except AttributeError:
        return ("None")

if __name__ == "__main__":
    main()