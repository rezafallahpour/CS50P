def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:1].isalpha() and len(s)>=2 and len(s) <= 6 and not s[0:-2].isdecimal() and s.isalnum():
        for i in range(len(s)):
            if i+1 < len(s) and s[i+1] == "0" and not s[i].isdecimal():
                return False
        return True
    else:
        return False



main()