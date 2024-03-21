import sys
import csv
from tabulate import tabulate


def main():
    start()
    s = []
    with open("%s"%sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(reader)
        for row in reader:
            rr = list(row.keys())
            s.append([row[rr[0]], row[rr[1]], row[rr[2]]])
    headers = [rr[0], rr[1], rr[2]]
    print(tabulate(s,headers, tablefmt="grid"))



def start():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith("csv"):
            try:
                with open("%s"%sys.argv[1], "r") as file:
                    return True
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()