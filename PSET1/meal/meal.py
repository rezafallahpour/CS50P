def main():
    x = convert(input("What time is it? "))
    if x >= 7 and x <= 8:
        print("breakfast time")
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 18 and x <= 19:
        print("dinner time")

def convert(time):
    a = time.split(":")
    a[1] = float(a[1])/60
    tt = float(a[0]) + float(a[1])
    return float(tt)


if __name__ == "__main__":
    main()