def main():
    word = input("Greeting: ")
    vv = value(word)
    print("$%i"%vv)


def value(greeting):
    word = greeting.lower()
    if word.startswith("hello"):
        return 0
    elif word.startswith("h"):
        return 20
    elif word.startswith("w"):
        return 100
    else:
        return 100

if __name__ == "__main__":
    main()