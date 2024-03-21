
def main():
    while True:
        inp = input("Fraction: ")
        try:
            x = convert(inp)
            z = gauge(x)
            print(z)
            break
        except:
            continue

def convert(fraction):
    numbers = fraction.split("/")
    x = int(numbers[0])
    y = int(numbers[1])
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    z = float(x/y)*100
    z = round(z)
    return z

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return '%i%%'%percentage

if __name__ == "__main__":
    main()