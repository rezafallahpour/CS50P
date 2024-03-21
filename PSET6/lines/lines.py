import sys

def main():
    count = 0
    start()
    with open("%s"%sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
            if not line.strip().startswith("#") and not line.strip() == "":
                count+=1
        print(count)


def start():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith("py"):
            try:
                with open("%s"%sys.argv[1], "r") as file:
                    return True
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")


if __name__ == "__main__":
    main()