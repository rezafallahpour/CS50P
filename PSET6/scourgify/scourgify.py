import sys
import csv

def main():
    start()
    s = []
    with open("%s"%sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rr = list(row.keys())
            x , y = row[rr[0]].replace('"','').split(", ")
            s.append([x , y, row[rr[1]]])
    with open("%s"%sys.argv[2], 'w', newline='') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file , fieldnames=fieldnames)
        writer.writeheader()
        for x in s:
            writer.writerow({'first': x[0], 'last': x[1], 'house': x[2]})


def start():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith("csv"):
            try:
                with open("%s"%sys.argv[1], "r") as file:
                    return True
            except FileNotFoundError:
                sys.exit("Could not read %s"%sys.argv[1])
        else:
            sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()