import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):
    try:
        m = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip)
        split = m.groups()
        for i in split:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    except:
        return False




if __name__ == "__main__":
    main()