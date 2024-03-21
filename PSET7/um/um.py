import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    u1 = re.findall(r"^(um).*",s)
    u2 = re.findall(r" (um).*",s)
    return len(u1)+len(u2)


if __name__ == "__main__":
    main()